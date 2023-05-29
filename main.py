#!/usr/bin/env python3

import rospy
from std_srvs.srv import Empty

def call_service(service_name):
    #Check server
    rospy.wait_for_service(service_name)
    try:
        service = rospy.ServiceProxy(service_name, Empty)
        response = service()
        return response
    #error response
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)

def main():
    rospy.init_node('main_node')
    #Call service funtion
    call_service('/go_to_kitchen')
    call_service('/stop')
    call_service('/go_home')
    call_service('/stop')

if __name__ == '__main__':
    main()