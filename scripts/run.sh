#!/bin/bash

roscore &

roslaunch usb_cam usb_cam-test.launch &
roslaunch opencv_apps face_recognition.launch image:=/usb_cam/image_raw &

rosrun rchomeedu_speech google_sr.py &

rosrun sound_play soundplay_node.py &

python catkin_ws/src/security_door_project/scripts/security_door_listener.py catkin_ws/src/security_door_project/scripts/security_door_output.py

wait