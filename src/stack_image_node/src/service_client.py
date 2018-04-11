#!/usr/bin/env python
import rospy
from time import sleep
from stack_image_node.srv import *


def main():
    rospy.init_node('image_client')
    rospy.wait_for_service('image_request')

    image_request = rospy.ServiceProxy('image_request', Save)
    msg = ['on', 'off']

    while True:
        for i in msg:
            print('[INFO]Send ' + i + ' message!')
            result = image_request(i)
            sleep(5)
            if result.result is True:
                print('[INFO]Processing completed!\n')
            else:
                print('[WARNING]Saving fail!\n')

main()
