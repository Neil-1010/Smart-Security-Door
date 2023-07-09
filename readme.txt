Warm greetings from our Smart Security Door!

To get started, kindly follow the instructions below:

=> To implement the smart security door, you need to upload the photos of registered/authorized users under the folder directory "./scripts/WorkSpace/registered_users"
=> Then, direct to ./scripts/WorkSpace, edit codes in face_reg_socket.py

====================================================
// Run the roscore to initiate
roscore

// Run speech_recognition module
rosrun rchomeedu_speech google_sr.py

// Run sound play module
rosrun sound_play soundplay_node.py
rosrun sound_play say.py "hello word" [optional]
 
// Run smart security door program
cd catkin_ws/src/security_door_project/scripts/
python security_door_socket.py

// Run facial recognition module
cd catkin_ws/src/security_door_project/scripts/WorkSpace
source test/bin/activate
python face_reg_socket.py

// Run the output program
cd catkin_ws/src/security_door_project/scripts/
python security_door_output.py
====================================================