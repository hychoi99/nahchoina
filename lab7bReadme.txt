Nahian Jahangir 
Hyung Yui Choi
Nathan Smith

Since we last saw it, the Turtlebot has evolved into a better robot with a variety of 
features.

-LAB 6 (Up to Chase)
The turtlebot still retains all of its functions from Lab 6. It's able to move around,
avoid objects, turn when bumped, stop when cliff sensors detect nothing, and chase 
objects that have a certain shade of pink. When it targets something pink, it will give
chase until it reaches a certain distance away from the object and stops in place. 
Target acquired.

Run the following in terminal/s: (Remember to source in every open terminal
"source ~/jackachoipt2-workspace/setup.bash")
	-roscore
	-rosrun depthimage_to_laserscan depthimage_to_laserscan image:=/camera/depth
/image_raw
You must now run the launch file which should run all the nodes which is just
	-roslaunch nahchoina chase.launch
		In the event that it DOES NOT, follow this procedure:
		-roslaunch openni_launch openni.launch
		-roslaunch turtlebot bringup minimal.launch
		-rosrun nahchoina BumpMoniter.py
		-rosrun nahchoina CliffMoniter.py
		-rosrun nahchoina LaserMon.py
		-rosrun nahchoina TargetMon.py
		-rosrun nahchoina FSMMaster3.py

-LAB 7b (Navigation)
The turtlebot now can navigate through a room! Give the turtlebot a map of the room and 
it will find the most optimal path from start to end. This is done through A*, code 
provided by John Rieffel. 

To begin navigation 
	-rosrun nahchoina GridConvert.py. 
To change the map, type
	-rosrun map_server map_server <map_file>.yaml
	WARNING: The directory that the yaml file is in is also where the .png file is in.





