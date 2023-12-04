#server code
import socket, cv2, pickle, struct
import threading
import queue
import pyshine as ps
from datetime import datetime

# Create a socket to listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the host IP address and port to bind the server socket
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:', host_ip)
port = 9999
socket_address = (host_ip, port)
server_socket.bind(socket_address)

# Start listening for incoming connections
server_socket.listen()
print("Listening at", socket_address)

# Create a queue to store video frames from clients
frame_queue = queue.Queue()

# Function to display received frames with timestamps
def show_frames():
    while True:
        if not frame_queue.empty():
            addr, frame = frame_queue.get()
            
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            # Add a timestamp to the frame using pyshine
            frame = ps.putBText(frame, now, 10, 10, vspace=10, hspace=1, font_scale=0.7,
                                background_RGB=(255, 0, 0), text_RGB=(255, 250, 250))
            cv2.imshow(f"FROM {addr}", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break

# Create a thread for displaying frames
display_thread = threading.Thread(target=show_frames)
display_thread.start()

# Function to handle a client's connection
def handle_client(addr, client_socket):
    # Define the video codec fourcc (XVID) for the video writer
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    now = datetime.now()
    # Format the current date and time into a string with the format "ddmmyyyyHHMMSS"
    time_str = now.strftime("%d%m%Y%H%M%S")
    # Create a unique video file name by combining "Rec" and the formatted time string with the ".avi" extension
    time_name = 'Rec' + time_str + '.avi'
    # Define the frames per second (fps) for the video
    fps = 30
    # Initialize a variable to keep track of whether the frame shape has been determined
    frame_shape = False

    try:
        print('CLIENT {} CONNECTED!'.format(addr))
        # Check if the client socket is valid
        if client_socket:
            # Initialize an empty byte string to store received data
            data = b""
            # Calculate the size of the payload (expected size of each frame) using struct.calcsize
            payload_size = struct.calcsize("Q")

            while True:
                # Continue receiving data until the size of data matches the expected payload size
                while len(data) < payload_size:
                    # Receive a packet of data from the client (4 KB at a time)
                    packet = client_socket.recv(4 * 1024)

                    if not packet:
                        break

                    # Append the received packet to the data
                    data += packet
                # Extract the packed message size from the data
                packed_msg_size = data[:payload_size]
                # Remove the packed message size from the data
                data = data[payload_size:]
                # Unpack the message size using struct.unpack to get the actual frame size
                msg_size = struct.unpack("Q", packed_msg_size)[0]

                # Continue receiving data until the size of data matches the size of the frame
                while len(data) < msg_size:
                    data += client_socket.recv(4 * 1024)

                # Extract the frame data from the received data
                frame_data = data[:msg_size]
                # Remove the frame data from the data
                data = data[msg_size:]
                #deserializing
                frame = pickle.loads(frame_data)
                frame_queue.put((addr, frame))

                if not frame_shape:
                    video_file_name = str(addr) + time_name

                    # Create a VideoWriter to write the video to a file
                    out = cv2.VideoWriter(video_file_name, fourcc, fps, (frame.shape[1], frame.shape[0]), True)
                    frame_shape = True
                out.write(frame)
            client_socket.close()
    except Exception as e:
        print(f"CLIENT {addr} DISCONNECTED")
        pass
# Main loop to accept incoming client connections
while True:
    client_socket, addr = server_socket.accept()

    # Create a thread to handle each client's connection
    thread = threading.Thread(target=handle_client, args=(addr, client_socket))
    thread.start()

    print("TOTAL CLIENTS :", threading.active_count() - 2)


###################################################################################################################################################


