#!/usr/bin/env python
# Client Node that listens for BumpEvents, and for now just prints the data when it "hears" that

import roslib; roslib.load_manifest('nahchoina') 
import rospy 

from std_msgs.msg import String
from sensor_msgs.msg import LaserScan

from nahchoina.srv import *
from kobuki_msgs.msg import *

#if state=pressed call handle bump event
def CliffMonitorCB(data):
   rospy.wait_for_service('cliffEvent') #Blocks until server is ready to take in info
   myCliffData = CliffData()
   myCliffData.CliffState = data.state
#   print myBumpData.bumperState
#   print data.state
   try:
      cliffEventFunc = rospy.ServiceProxy('cliffEvent', CliffData)
      result = cliffEventFunc(myCliffData.CliffState)
      return result
   except rospy.ServiceException, e:
      print "Service call failed: %s"%e      

def CliffMonitor():
    rospy.init_node('CliffMonitor', anonymous=True)
    rospy.Subscriber('/mobile_base/events/cliff',CliffEvent,CliffMonitorCB)
    rospy.spin()


if __name__ == '__main__':
#   try:
   CliffMonitor()
#   except rospy.ROSinterruptionException: pass


