import rospy
from sensor_msgs.msg import Image
from opencv_apps.msg import FaceArrayStamped
from std_msgs.msg import Bool
import socket

if __name__ == '__main__':

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost',8000)
    server_socket.bind(server_address)
    server_socket.listen(1)

    # Initiate server socket
    print('Started. Server is listening for connections...')

    # Initiate door_listener node
    rospy.init_node('door_listener')
    
    # Publish data via detect_result topic
    pub = rospy.Publisher('/detect_result',Bool, queue_size =1)

    # Register authorized users
    known_face_names = [
    "Chun Fang",
    "Neil"
    ]

    while True:
        client_socket = None
        try:
            client_socket, client_address = server_socket.accept()
            response = client_socket.recv(1024)
            data = response.decode()

            # Display response from time to time
            print("Received response: " +str(data))

            # Recognize registered users based on conditions
            if data in known_face_names:
                print("Welcome, "+str(data)+"!")
                pub.publish(Bool(True))
            else:
                pub.publish(Bool(False))

        except KeyboardInterrupt:
            if client_socket:
                client_socket.close()
            break
        except socket.timeout:
            pass

    server_socket.close()