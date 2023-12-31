# Real-time-multi-client-Video-Streaming-with-python


INTRODUCTION :
	The project aims to establish a video streaming service where a client can send video frames to a server. The server displays the received frames in real-time with timestamps and saves them to a 
	video file.
			 	
SETTING UP AND RUNNING THE PROJECT:
      
    • To set up and run the project, follow these steps:-
    
        ◦ Ensure Python3 is installed.
        ◦ Install necessary libraries using pip install opencv-python, imutils, pyshine.
        ◦ We have to import socket, cv2, pickle, struct, threading, queue, pyshine as ps, and from datetime import datetime in server side
        ◦ We have to import socket, cv2, pickle, struct, imutils in client side
        ◦ Run the server code on the server machine.
        ◦ Modify the host_ip variable in the client code to the server's IP address.
        ◦ Run the client code on the client machine.
      
      
SERVER CODE:
      
    The server-side code handles client connections, displays video frames, and records the video stream.
      
    • Server Initialization:-
	      The server socket is created, bound to the host IP and port, and starts listening for 	incoming connections.
	
    • Video Frame Display:-
	      Real-time video frames are displayed using OpenCV and pyshine, with timestamps 	added to each frame.
	
    • Client Connection Handling:-
	      Each client connection is handled in a separate thread. The server receives video 	frames, displays them, and records them to a video file.

  RUNNING THE SERVER CODE	:
     Run command :- python3 server.py
      
  SERVER IP ADDRESS:
	   When we run the command python3 server.py it displays 'HOSTIP' address in the time of listening.You can add this IP address to client code.so server can have videos from client.
	
	
 CLIENT CODE:

    The client-side code captures video frames and sends them to the server.  
                          
    • Socket connection:-
      The client establishes a socket connection to the server, serializes video frames, and sends them to server

    • Configuring the Video Source (camera variable):-
      In the client code, there is a variable named `camera` that determines the video source. You can set it to either `True` or `False` to specify the video source:
      
    • ‘camera = True’   :-    📹️ USE THE COMPUTER'S CAMERA AS THE VIDEO SOURCE.
    • ‘camera = False’  :-    ▶️ USE A VIDEO FILE AS THE VIDEO SOURCE.
      
      By manually changing this variable to either true or false, you can switch between capturing video from the client camera or a video file.
	


   RUNNING THE CLIENT CODE	:

      After configuring the `camera` variable, run the client code on the client machine.
      
      Run command :- python3 client.py
      
	
VIDEO CAPTURE:
	The client captures video frames either from the camera or a video file using OpenCV and resizes them.

TESTING AND RESULTS:
      The project was tested successfully with both camera and video file inputs. Real-time video streaming from the client to the server was achieved.
      
CONCLUSION:
      The project demonstrates a basic video streaming system.
