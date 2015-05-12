#!/usr/bin/env python
import math
import roslib; roslib.load_manifest('lab_6')
import rospy
from cv_bridge import CvBridge, CvBridgeError
import cv
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image

class cv_vision_node:

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
       	 	#cv.ShowImage(self.cv_window_name, cv_image)
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
					print i,j, mat[j,i]
		
		aveH = aveH/count
		aveW = aveW/count
		
		overlay = cv.CreateImage(cv.GetSize(cv_img),8,3)
		cv.Circle(overlay, (int(aveW), int(aveH)), 2, (255,255,255),20)
		cv.Add(cv_img,overlay,cv_img)
		return cv_img


if __name__ == '__main__':
      vn = cv_vision_node()
      try:
        rospy.spin()
      except KeyboardInterrupt:
        print "Shutting down vison node."
      cv.DestroyAllWindows()

