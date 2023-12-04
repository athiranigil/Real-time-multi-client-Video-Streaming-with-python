# In this code client is sending video to server

# Import necessary libraries for working with sockets, OpenCV, serialization, and structuring data
import socket,cv2, pickle,struct
# Import the 'imutils' library for resizing frames
import imutils

# Set the 'camera' variable to True (you can change this to False to use a video file instead)
camera = False
# Check if camera is being used
if camera == True:
	vid = cv2.VideoCapture(0)
else:
	vid = cv2.VideoCapture('/home/athira/im/cat.mp4')

# Create a socket for the client using IPv4 and TCP protocol
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Define the IP address and port of the server to connect to
host_ip = '12.0.2.5' # Here according to your server
port = 9999

client_socket.connect((host_ip,port))

# Check if the client socket was successfully created
# Enter a loop that captures frames from the camera/video and sends them to the server
if client_socket: 
	while (vid.isOpened()):
		try:
			img, frame = vid.read()
			frame = imutils.resize(frame,width=380)
			# Serializing (pickling) the resized frame using the pickle module.
			a = pickle.dumps(frame)
			# Creating a message by packing the length of the serialized frame data (as a Q format, representing an unsigned long long) followed by the serialized frame data itself.
			message = struct.pack("Q",len(a))+a
			client_socket.sendall(message)
			# Displaying the original frame in a window titled "TO: <server IP>".
			cv2.imshow(f"TO: {host_ip}",frame)
			key = cv2.waitKey(1) & 0xFF
			if key == ord("q"):
				client_socket.close()
		except:
			print('VIDEO FINISHED!')
			break

