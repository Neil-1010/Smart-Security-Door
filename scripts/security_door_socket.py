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
    print('Started. Server is listening for connections...')

    rospy.init_node('door_listener')
    pub = rospy.Publisher('/detect_result',Bool, queue_size =1)

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
            print("Received response: " +str(data))

            # =========================================
            # Recognize registered users based on conditions
            if data in known_face_names:
                print("Welcome, "+str(data)+"!")
            # if data == "Chun Fang":
            #     pub.publish(Bool(True))
            #     print("Hi, Chun Fang!")
            # elif data == "Neil":
            #     pub.publish(Bool(True))
            #     print("Hi, Neil!")
            else:
                pub.publish(Bool(False))
            # =========================================

        except KeyboardInterrupt:
            if client_socket:
                client_socket.close()
            break
        except socket.timeout:
            pass

    server_socket.close()