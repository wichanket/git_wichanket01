#!/usr/bin/env python3

import rospy
import time
from std_srvs.srv import Empty, EmptyResponse

def go_home(request):
    rospy.loginfo("Going to home.")
    time.sleep(2)
    rospy.loginfo("Arrived.")
    return EmptyResponse()

def go_to_kitchen(request):
    rospy.loginfo("Going to kitchen.")
    time.sleep(2)
    rospy.loginfo("Arrived.")
    return EmptyResponse()

def stop(request):
    rospy.loginfo("Stop!")
    return EmptyResponse()

def navigation_server():
    #creat node
    rospy.init_node('navigation_server')
   #creat service call funtion
    go_home_service = rospy.Service('/go_home', Empty, go_home)
    go_to_kitchen_service = rospy.Service('/go_to_kitchen', Empty, go_to_kitchen)
    stop_service = rospy.Service('/stop', Empty, stop)
    
    rospy.loginfo("Navigation server is ready.")
    rospy.spin()

if __name__ == '__main__':
    navigation_server()