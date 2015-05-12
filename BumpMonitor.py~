#!/usr/bin/env python

#Client for the bumpevent service


import roslib; roslib.load_manifest('nahchoina')
import sys
import rospy
from nahchoina.srv import *
from kobuki_msgs.msg import BumperEvent,WheelDropEvent

def Bumpdata(data):
	rospy.wait_for_service('BumpEvent')
	try:

		bump = rospy.ServiceProxy('BumpEvent', BumpData)
		
		#see BumpData.srv
		if type(data) == BumperEvent:
			return bump(data.bumper,3,data.state)

		elif type(data) == WheelDropEvent:
			return bump(3,data.wheel,data.state)

	except rospy.ServiceException, e:
	        print "Service call failed: %s"%e

def BumpMonitor():
	rospy.init_node('BumpMonitor', anonymous=True)
	rospy.Subscriber('/mobile_base/events/bumper', BumperEvent, Bumpdata)
	rospy.Subscriber('/mobile_base/events/wheel_drop', WheelDropEvent, Bumpdata)
	rospy.spin()

if __name__ == "__main__":
	try:
	        BumpMonitor()
    	except rospy.ROSInterruptException: pass
