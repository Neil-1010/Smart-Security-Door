import rospy
import message_filters
from std_msgs.msg import Bool, String
import subprocess

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
        # Keyword represents the 'access passcode'
        # A valid access shall require correct keyword and valid facial recognition
        if self.keyword == "hello" and self.detection == "Yes":
            subprocess.check_output(['rosrun', 'sound_play', 'say.py', "You may enter"])
        elif self.detection == "No":
            subprocess.check_output(['rosrun', 'sound_play', 'say.py', "Please try again"])


if __name__ == '__main__':
    
    # Initiate door_output node
    rospy.init_node('door_output')

    server = Server()
    server.compute()
    
    # Establish connections
    sub = rospy.Subscriber('/result', String, server.keyword_callback) 
    sub2 = rospy.Subscriber('/detect_result', String, server.detection_callback)
    
    rospy.spin()