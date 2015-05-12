#!/usr/bin/env python

#Gets a map data and reduces its resolution into a square grid map

import roslib; roslib.load_manifest('nahchoina')
import sys
import rospy
import signal
import time
#from twitter import *
import subprocess
from math import *
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from nav_msgs.msg import OccupancyGrid,MapMetaData
from AstarPathFinder import *

def Mapdata(data):
	
	globalX = 0
	globalY = 0
	squareSize = 20 #number of pixels in each grid (squareSize x squareSize)
	dataIndex = 0
	origMap = []
	column = []
	newMap = []
	newCols = []
#	my_auth = twitter.OAuth(2889674099-y022Ug1Tlz3TBcDQuvVQ1QmhRVPxL6PrMktl5tu, TScW2srn8eiM0Wf9onhbFLnsgeG0s5408o5GWfxuSVXfv, TVS0qhgD9mHPemENWvifDUMmV, vyUobnnz3myqZu0624Q2d1809WfgJlBY6jAtYsFzcVfPVuYyED)
#	twit = twitter.Twitter(auth = my_auth)

	#gets the 1D map data array from the pgm file 
	#and converts it into a 2D array. Something that is
	#conceptually easier to understand
	print data.info.height, data.info.width
	for y in range(data.info.height):
		for x in range(data.info.width):
			column.append(data.data[dataIndex])
			dataIndex += 1
		column.reverse()
		origMap.append(column)
		column = []


	#simplifies the map into a (squareSize x squareSize) map
	while globalX < data.info.width - squareSize: #
		while globalY < data.info.height - squareSize: #removes the edge cases where the grid square won't fit

			threshold = [0,0,0]

			for localX in range(squareSize):
				for localY in range(squareSize):
					if origMap[globalY + localY][globalX + localX] == -1: #-1 means 
						threshold[2] += 1
					elif origMap[globalY + localY][globalX + localX] == 100:
						threshold[1] += 1
					else:
						threshold[0] += 1
			if threshold[0] > threshold[1] and threshold[0] > threshold[2]:
				majority = 0
			else:
				majority = 1
			globalY += squareSize
			newCols.append(majority)

		globalX += squareSize
		globalY = 0
		newMap.append(newCols)
		newCols = []

    #Print new map in terminal
	for x in range(len(newMap)):
		if x == 0:
			print ' ', x,
		else:
			print x,
	print
	for y in range(len(newMap[0])):
		print len(newMap[0])-1 - y, 
		for x in range(len(newMap)):
			if newMap[(x+1)*-1][(y+1)*-1] == 1:
				print 'X',
			else:
				print ' ',
		print

	runner = AStarRunner(newMap)
	start_loc = (12,10)
	end_loc = (15,14)
	path = runner.search(start_loc, end_loc)
	print path
	pathtotwist = PathToTwist(0,path)
	pathtotwist.twistConverter()

class PathToTwist:

    def __init__ (self, curDir, path):
        self.curDir = curDir
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
	twitcount = 0
	for direction in self.twistList:
	#	twit.statuses.update(status="test" + twitcount)
		twit_msg = 'test' + str(twitcount)
		command = 'twitter -esmithn@union.edu set %s' % twit_msg
		timeout = time.time() + 5.7 * 2
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
		subprocess.call(command, shell=True)
		twitcount += 1
    		time.sleep(1)
	
    def directionFinder(self, currentPos, goalPos):
	
		(curX, curY) = currentPos
		(goalX, goalY) = goalPos

		deltaX = goalX - curX
		deltaY = goalY - curY


		turnLeft = -3*pi/2 + 0.2
		turnRight = 3*pi/2 - 0.2 
		
		angular = 0
		twit_msg = 'moving forward'
		#Moving East
		if deltaX == 1:
			if self.curDir == 0:
				angular = turnLeft
				twit_msg = 'Turning left'
			elif self.curDir == 1:
				angular = 0
				Twit_msg = 'moving forward'
			elif self.curDir == 2:
				angular = turnRight
				twit_msg = 'Turning Right'
			elif self.curDir == 3:
				angular = 2*turnRight
			else:
				return 'error'
			self.curDir = 1

		#Moving West
		elif deltaX == -1:
			if self.curDir == 0:
				angular = turnRight
				twit_msg = 'Turning Right'
			elif self.curDir == 1:
				angular = 2*turnRight
			elif self.curDir == 2:
				angular = turnLeft
				twit_msg = 'Turning left'
			elif self.curDir == 3:
				angular = 0
				Twit_msg = 'moving forward'
			else:
				return 'error'
			self.curDir = 3

		#Moving North
		elif deltaY == 1:
			if self.curDir == 0:
				angular = 0
				Twit_msg = 'moving forward'
			elif self.curDir == 1:
				angular = turnRight
				twit_msg = 'Turning Right'
			elif self.curDir == 2:
				angular = 2*turnRight
			elif self.curDir == 3:
				angular = turnLeft
				twit_msg = 'Turning left'
			else:
				return 'error'
			self.curDir = 0

		#Moving South
		elif deltaY == -1:
			if self.curDir == 0:
				angular = 2*turnRight
			elif self.curDir == 1:
				angular = turnLeft
				twit_msg = 'Turning left'
			elif self.curDir == 2:
				angular = 0
				Twit_msg = 'moving forward'
			elif self.curDir == 3:
				angular = turnRight
				twit_msg = 'Turning Right'
			else:
				return 'error'
			self.curDir = 2
		
		command = 'twitter -esmithn@union.edu set %s' % twit_msg
		subprocess.call(command, shell=True)
		return angular

#subscribes to the loaded map data
def MapMonitor():
	rospy.init_node('MapMonitor', anonymous=True)
	rospy.Subscriber('/map', OccupancyGrid, Mapdata)
	rospy.spin()

if __name__ == "__main__":
	MapMonitor()
