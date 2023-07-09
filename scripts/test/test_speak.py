import rospy
import subprocess


if __name__ == '__main__':
    rospy.init_node('speak')

    rospy.loginfo("This node has been started")

    subprocess.check_output(['rosrun', 'sound_play', 'say.py', "hello word"])