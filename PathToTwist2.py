#!/usr/bin/env python


import roslib; roslib.load_manifest('nahchoina')
import sys
import rospy
import signal
import time
from natwit/twitter import *
from math import *
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class PathToTwist:

    def __init__ (self, curDir, path):
        self.curDir = curDir
	my_auth = twitter.OAuth(2889674099-y022Ug1Tlz3TBcDQuvVQ1QmhRVPxL6PrMktl5tu, TScW2srn8eiM0Wf9onhbFLnsgeG0s5408o5GWfxuSVXfv, TVS0qhgD9mHPemENWvifDUMmV, vyUobnnz3myqZu0624Q2d1809WfgJlBY6jAtYsFzcVfPVuYyED)
	twit = twitter.Twitter(auth = my_auth)
        self.path = path
        self.twistList = []

    def __str__ (self):
        return str(curDir)


    def twistConverter(self):

    	for n in range(len(self.path)-1):
    		angular = self.directionFinder(self.path[n], self.path[n+1])
    		linear = 0.1

    		if angular == 0:
			self.twistList.append((linear, 0))
		else:
			self.twistList.append((0,angular))
			self.twistList.append((linear,0))

	self.Steer()

    def Steer(self):

    	print self.twistList
	outdata = Twist()
	pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist) #publish 'cmd_vel' of type twist
	for direction in self.twistList:
		timeout = time.time() + 5.7
		(linear, angular) = direction
		outdata.linear.x = linear
		outdata.angular.z = angular
		if angular == 0:
			while True:
				if time.time() > timeout:
					break
    				pub.publish(outdata)#publish the 
			print 'broke'
		else:
			pub.publish(outdata)
		print linear, angular
    		time.sleep(1)
	
    def directionFinder(self, currentPos, goalPos):
	
		(curX, curY) = currentPos
		(goalX, goalY) = goalPos

		deltaX = goalX - curX
		deltaY = goalY - curY

		turnLeft = -3*pi/2 + 0.2
		turnRight = 3*pi/2 - 0.2 
		
		angular = 0

		#Moving East
		if deltaX == 1:
			if self.curDir == 0:
				angular = turnLeft
			elif self.curDir == 1:
				angular = 0
			elif self.curDir == 2:
				angular = turnRight
			elif self.curDir == 3:
				angular = 2*turnRight
			else:
				return 'error'
			self.curDir = 1

		#Moving West
		elif deltaX == -1:
			if self.curDir == 0:
				angular = turnRight
			elif self.curDir == 1:
				angular = 2*turnRight
			elif self.curDir == 2:
				angular = turnLeft
			elif self.curDir == 3:
				angular = 0
			else:
				return 'error'
			self.curDir = 3

		#Moving North
		elif deltaY == 1:
			if self.curDir == 0:
				angular = 0
			elif self.curDir == 1:
				angular = turnRight
			elif self.curDir == 2:
				angular = 2*turnRight
			elif self.curDir == 3:
				angular = turnLeft
			else:
				return 'error'
			self.curDir = 0

		#Moving South
		elif deltaY == -1:
			if self.curDir == 0:
				angular = 2*turnRight
			elif self.curDir == 1:
				angular = turnLeft
			elif self.curDir == 2:
				angular = 0
			elif self.curDir == 3:
				angular = turnRight
			else:
				return 'error'
			self.curDir = 2

		return angular


def test(direction, path):
	rospy.init_node('PathToTwist')
	testPath = [(1,2),(1,3),(2,3),(2,4),(1,4)]
	tester = PathToTwist(direction,path)
	tester.twistConverter()

if __name__ == "__main__":
    test()


