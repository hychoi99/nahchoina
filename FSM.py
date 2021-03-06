#!/usr/bin/env python

import roslib; roslib.load_manifest('nahchoina')
from nahchoina.srv import *
from nahchoina.msg import *
from vector import Vector
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import *
import rospy
import math
import time

class FSMMaster3():

    #the class for handling Finite State Machines in ROS
    #note this is provided only as psuedocode
    #and carries no promises of quality
    #and few promises of coherence

    def __init__(self):
        self.linear = 0
        self.angular = 0
	self.LaserLinear = 0
	self.LaserAngular = 0
	self.TargetLinear = 0
	self.TargetAngular = 0
        self.curstate = 'move'
        self.states = {}   
        self.transitionTable = {}
        self.bumper = -1
	self.bumpstate = 0  
        self.AddFSMState('move',self.Move)
        self.AddFSMState('avoid',self.Avoid)
        self.AddFSMState('bumpreact',self.BumpReact)
	self.AddFSMState('cliffreact',self.CliffReact)
	self.AddFSMState('chase',self.Chase)
  #      self.outputVector = Vector(0,0)

        #A transition set for a given state lists 
        #basically: if we're in the moveandavoid state
        #and we receive a bump event, we want to switch to the bumpreact state
        #otherwise we want to stay in the moveandavoid state
        movetransitions = {'bump':'bumpreact','allclear':'move','laserclear':'move','laseravoid':'avoid','cliff':'cliffreact',
'target': 'chase', 'cliff':'cliffreact'}
        self.AddFSMTransition('move',movetransitions)
        avoidtransitions = {'bump':'bumpreact','allclear':'move','laserclear':'move','laseravoid':'avoid','cliff':'cliffreact', 'target': 'avoid'}
        self.AddFSMTransition('avoid',avoidtransitions)
        #similarly, if we are in the bumpreact state, and we get an all clear
        #we want to switch to the moveandavoid state
        #otherwise stay in bumpreact
        bumpreacttransitions = {'bump':'bumpreact',
'allclear':'move','cliff':'cliffreact','laserclear':'bumpreact','laseravoid':'bumpreact','target': 'bumpreact'}
        self.AddFSMTransition('bumpreact',bumpreacttransitions)
        
	#Similar to wheel drop, when raised above the ground, should be in cliffreact. When lowered, back to move.
	cliffreacttransitions ={'allclear':'move','cliff':'cliffreact','laserclear':'cliffreact','laseravoid':'cliffreact','bump':'cliffreact',
'target': 'cliffreact'}
        self.AddFSMTransition('cliffreact',cliffreacttransitions)

	chasetransitions = {'allclear':'move','cliff':'cliffreact','laserclear':'chase','laseravoid':'avoid','bump':'bumpreact', 'target':'chase','bump':'bumpreact'}	
	self.AddFSMTransition('chase', chasetransitions)
    #states are a dictionary of name/function pairs  stored in a dictionary
    #i.e. {'moveandavoid':self.MoveAndAvoid}
    def RunFSM(self):
        while(True):
            curstatefunction = self.states[self.curstate]
            curstatefunction()
            #self.Steer()
            if self.curstate == 'bumpreact':
                while self.bumpstate == 1:
			self.Steer()
		time.sleep(1)
	    else:
		self.Steer()

    #states are a dictionary of name/function pairints stored in a dictionary
    #i.e. {'moveandavoid':self.MoveAndAvoid}
    def AddFSMState(self,name,function):
        self.states[name] = function

    #each state gets its own transition table
    #a transition table is a list of states to switch to
    #given a "event"
    def AddFSMTransition(self,name,transitionDict):
        #yes we are making a dictionary the value bound to a dictionary key
        self.transitionTable[name] = transitionDict     
    
    #move part calls laseravoid event if something is nearby
    def Move(self):
#	print "im moving"
	self.linear = 0.14
	self.angular = 0

    def Avoid(self):
            #process steering vectors produced by LaserScanCallback
            # to generate a self.steering.linear
            # and self.steering.angular
#	print "im avoid"
  	self.linear = self.LaserLinear
	self.angular = self.LaserAngular
	#print self.LaserLinear, self.LaserAngular

    def BumpReact(self):
            ### if we are in the 'bumpreact' state
            ### we want to just have angular velocity
            ### we want the robot to move back and away from object
        if self.bumper == 0: #left bumper
            self.linear = -.2
            self.angular = -math.pi/2
        elif self.bumper == 1: #middle bumper
            self.linear = -.2
            self.angular = math.pi
        elif self.bumper == 2: #right bumper
            self.linear = -.2
            self.angular = math.pi/2
        elif self.bumper == 3: #cliff sensor
            self.linear = 0
            self.angular = 0
        else:                   #it should never reach this point....
            self.linear = 0
            self.angular = 0
            self.bumper = -1

	#cliff react. should stop all turtlebot movements
    def CliffReact(self):
	self.linear = 0
	self.angular = 0
	#event = 'cliff'
	#self.HandleEvent(event)

    def Chase(self):
	self.linear = self.TargetLinear
	self.angular = self.TargetAngular		
	
    #we run Steer() instead of Spin.  Steer publishes the actual twist message
    #to control the turtle
    def Steer(self):
        outdata = Twist()
        outdata.linear.x = self.linear
        outdata.angular.z = self.angular
        pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist) #publish type twist
        pub.publish(outdata)

            
    #if a client sends us a bump
    def HandleBumpEvent(self,req):
    	if req.state == 1: #when some thing has been triggered by client
        	if req.bumpers == 3: #3 means that cliff sensor has been triggered. See BumpData.srv
        	    event = 'bump'
        	    self.bumper == 3
        	elif req.bumpers == 0 or req.bumpers == 1 or req.bumpers == 2: #bumper triggered
        	    event = 'bump'
        	    self.bumper = req.bumpers #assign bumper number to global variable

    	else:
        	event='allclear' #when state = 0, everything's all clear
        	
	self.bumpstate = req.state
        self.HandleEvent(event)

	# hnadles cliff event
    def HandleCliffEvent(self,CliffDataMessage):
            
 	if (CliffDataMessage.CliffState):
		event = 'cliff'
		self.bumpstate = 1
	else:
		event = 'allclear'
		self.bumpstate = 0

        self.HandleEvent(event)
        #events cause transitions between state
        #knowing which state to transition to
        #depends on the state we transition from


#############################################################
    def HandleLaserEvent(self,LaserDataMessage):
	event = LaserDataMessage.event
	#print "before", self.linear
	self.LaserLinear = LaserDataMessage.linear
	#print "after", self. linear
	self.LaserAngular = LaserDataMessage.angular
	self.HandleEvent(event)
####################################################################
    def HandleTargetEvent(self, TargetDataMessage): #'targetaquired' 'allclear' '
	event = TargetDataMessage.event
	self.TargetLinear = TargetDataMessage.linear
	self.TargetAngular = TargetDataMessage.angular
	#print str(self.TargetLinear)
	#print str(self.TargetAngular)
	self.HandleEvent(event)
	
	
    #events cause transitions between state
    #knowing which state to transition to
    #depends on the state we transition from
    def HandleEvent(self, event):
	outdata = Led()
	pub2 = rospy.Publisher('/mobile_base/commands/led1', Led)
	if event == 'bump':
		outdata.value = 1
	elif event == 'laseravoid':
		outdata.value = 2
	elif event == 'target':
		outdata.value = 3
	else:
		outdata.value = 0
	pub2.publish(outdata)
        curtransitionTable = self.transitionTable[self.curstate]
        self.curstate = curtransitionTable[event]
	print self.curstate


def StartFSMMaster3():
    FSM = FSMMaster3()
    rospy.init_node('FSMMaster3')
    #don't forget to also subscribe to the LaserScan topic for MoveAndAvoid
    
    s = rospy.Service('BumpEvent', BumpData, FSM.HandleBumpEvent)
 #   rospy.Subscriber('/scan', LaserScan, FSM.LaserScanCallback)
    s2 = rospy.Service('cliffEvent', CliffData, FSM.HandleCliffEvent)

    rospy.Subscriber('/LaserMon', SteeringMessage, FSM.HandleLaserEvent)
    rospy.Subscriber('/TargetMon', SteeringMessage, FSM.HandleTargetEvent)
    #you can add a second and third and fourth service here
    

    #steering information is sent to the robot here, via a Twist topic 
    FSM.RunFSM()
if __name__ == "__main__":
     StartFSMMaster3()


