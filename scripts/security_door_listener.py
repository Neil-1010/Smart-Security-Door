import rospy
from sensor_msgs.msg import Image
from opencv_apps.msg import FaceArrayStamped
from std_msgs.msg import Bool

open_door = False
count_detect = 0

def callback_receive_data(msg):
    global count_detect, open_door
    if len(msg.faces) > 0:
        if msg.faces[0].label == "chunfang":
            count_detect += 1
    else:
        open_door = False
        count_detect = 0
        
    if count_detect >= 1:
        open_door = True

    if(open_door):
        pub.publish(Bool(True))
    else:
        pub.publish(Bool(False))
    # if len(msg.faces) > 0:
    #     if msg.faces[0].label == "chunfang":
    #         count_detect += 1
    #     if count_detect == 10:
    #         open_door = True
    #         rospy.loginfo("open")
    # else:
    #     open_door = False
    #     rospy.loginfo("no")

if __name__ == '__main__':
    rospy.init_node('door_listener')
    sub = rospy.Subscriber('/face_recognition/output',FaceArrayStamped, callback_receive_data)
    pub = rospy.Publisher('/detect_result',Bool, queue_size =1)
    rospy.spin()