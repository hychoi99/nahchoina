#!/usr/bin/env python
import math
import roslib; roslib.load_manifest('nahchoina')
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
def gotImageCB(data):
       print 'hello'
       myHeader = data.header
       #print  myHeader.seq,myHeader.stamp,myHeader.frame_id
       #print data.height, data.width
       #print  data.encoding, data.is_bigendian
       maxdiff = 0
       for curpix in range(data.height*data.width):
               curred = ord(data.data[3*curpix])*1.0/255  #the data is 8-bit integers, which python seems to think are characters.
               curgreen = ord(data.data[3*curpix + 1])*1.0/255  #so ord converts a char to an int
               curblue = ord(data.data[3*curpix + 2])*1.0/255
               print curred,curgreen,curblue

def SetupVision():
   rospy.init_node('vision',anonymous=True)
   rospy.Subscriber("/camera/rgb/image_color",Image,gotImageCB)
   rospy.spin()

if __name__ == '__main__':
   try:
       SetupVision()
   except rospy.ROSInterruptException: pass

