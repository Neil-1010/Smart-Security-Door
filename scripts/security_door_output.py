import rospy
import message_filters
from std_msgs.msg import Bool, String
import subprocess

correct = False

class Server:
    def __init__(self):
        self.keyword = ""
        self.detection = False

    def keyword_callback(self,msg):
        self.keyword = msg.data
        rospy.loginfo(self.keyword)
        self.compute()

    def detection_callback(self,msg):
        self.detection = msg.data
    
    def compute(self):
        global correct
        if self.keyword == "hello" and self.detection == True:
            if correct == False:
                subprocess.check_output(['rosrun', 'sound_play', 'say.py', "Correct"])
            correct = True
        else:
            if correct == True:
                subprocess.check_output(['rosrun', 'sound_play', 'say.py', "Try Again"])
            correct = False


if __name__ == '__main__':
    rospy.init_node('door_output')
    server = Server()
    server.compute()
    sub = rospy.Subscriber('/result', String, server.keyword_callback) 
    sub2 = rospy.Subscriber('/detect_result', Bool, server.detection_callback)
    
    rospy.spin()