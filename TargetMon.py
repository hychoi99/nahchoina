#!/usr/bin/env python

#Target Monitor Node

import math
import roslib; roslib.load_manifest('nahchoina')
import sys
import rospy
from nahchoina.msg import *
from nahchoina.srv import *
from kobuki_msgs.msg import BumperEvent,WheelDropEvent
from vector import Vector
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge, CvBridgeError
import cv
import cv2
from sensor_msgs.msg import Image

class TargetMon:

	def __init__(self):
		rospy.init_node('cvVision')

        	""" Give the OpenCV display window a name. """
        	self.cv_window_name = "OpenCV Image"

        	""" Create the window and make it re-sizeable (second parameter = 0) """
        	cv.NamedWindow(self.cv_window_name, 0)

        	""" Create the cv_bridge object """
        	self.bridge = CvBridge()

        	""" Subscribe to the raw camera image topic """
        	self.image_sub = rospy.Subscriber("/camera/rgb/image_color", Image, self.gotImageCB)

	def gotImageCB(self,data):
       		#print 'hello'
		try:
            		""" Convert the raw image to OpenCV format """
            		cv_image = self.bridge.imgmsg_to_cv(data, "bgr8")
        	except CvBridgeError, e:
          		print e
  
        
        	""" Get the width and height of the image """
        	(width, height) = cv.GetSize(cv_image)

        	""" Overlay some text onto the image display """
        	#text_font = cv.InitFont(cv.CV_FONT_HERSHEY_DUPLEX, 2, 2)
        	#cv.PutText(cv_image, "OpenCV Image", (50, height / 2), text_font, cv.RGB(255, 255, 0))

 		outimg = self.CountPinkPixels(cv_image)
 
        	""" Refresh the image on the screen """
       	 	cv.ShowImage(self.cv_window_name, cv_image)
       	 	cv.ShowImage(self.cv_window_name, outimg)
        	cv.WaitKey(3)

	#from http://www.davidhampgonsalves.com/opencv-python-color-tracking
	def CountPinkPixels(self,cv_img):
                cv.Smooth(cv_img, cv_img, cv.CV_BLUR, 3);

	        hsv_img = cv.CreateImage(cv.GetSize(cv_img), 8, 3)
	        cv.CvtColor(cv_img, hsv_img, cv.CV_BGR2HSV)

	        #limit all pixels that don't match our criteria, in this case we are  
        	#looking for purple but if you want you can adjust the first value in  
            	#both turples which is the hue range(120,140).  OpenCV uses 0-180 as  
            	#a hue range for the HSV color model 
            	thresholded_img =  cv.CreateImage(cv.GetSize(hsv_img), 8, 1)
            	cv.InRangeS(hsv_img, (120, 80, 80), (180, 255, 255), thresholded_img)
		#print type(thresholded_img)
		mat = cv.GetMat(thresholded_img)
		#mat = hsv_img.getNumpy()
		(width,height) = cv.GetSize(thresholded_img)
		aveW = 0
		aveH = 0
		count = 0
		for j in range(0,height):			
			for i in range(0,width):
				if (mat[j,i] == 255.0):
					count += 1
					aveH += j 
					aveW += i
					#print i,j, mat[j,i]
		
		#print count
	  	if count != 0:
    			aveH = aveH/count
    			aveW = aveW/count
    
    		linear = 0
    		angular = 0
    #if there isn't enough pink, don't chase
    		if count < 700:
			print "no pink"
        		event = 'allclear'
        		linear = .08
        		angular = 0
		elif count > 4000:
			print "too much pink"
			event = 'target'
			linear = 0
			angular = 0
    		else:
        #divided the image into 5 sections
        #the center section makes the bot move straight
			print "here's pink!!!"
        		event = 'target'
        		if aveW > 0 and aveW < 128:
            			angular = math.pi / 8
        		elif aveW >= 128 and aveW < 256:
            			angular = math.pi / 11
        		elif aveW >= 256 and aveW < 384:
            			angular = 0
        		elif aveW >= 384 and aveW < 512:
           		 	angular = math.pi / -11
       	 		elif aveW >= 512 and aveW < 640:
            			angular = math.pi / -8
        		elif aveW == 0 and aveH == 0:
            			event = 'allclear'
            			angular = 0
        		linear = .07

    #Message Sending
    		msg = SteeringMessage()
    		msg.event = event
    		msg.linear = linear
    		msg.angular = angular
    		pub = rospy.Publisher('/TargetMon', SteeringMessage, queue_size = 10)
    		pub.publish(msg)
		overlay = cv.CreateImage(cv.GetSize(cv_img),8,3)
		cv.Circle(overlay, (int(aveW), int(aveH)), 2, (255,255,255),20)
		cv.Add(cv_img,overlay,cv_img)
    		return cv_img

	#def TargetMon():
	#	rospy.init_node('TargetMon',anonymous=True)
	#	rospy.Subscriber('/camera/rgb/image_color', Image, gotImageCB)
	#	rospy.spin()

if __name__ == '__main__':
      vn =TargetMon()
      try:
        rospy.spin()
      except KeyboardInterrupt:
        print "Shutting down vison node."
      cv.DestroyAllWindows()
