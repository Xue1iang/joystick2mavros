#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from mavros_msgs.msg import OverrideRCIn

# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Twist commands
# axis 1 aka left stick vertical
# axis 0 aka left stick horizonal
def callback(data):
 global pub
 ch1 = int(data.axes[1]*100.0+1500)
 new_msg = OverrideRCIn()
 new_msg.channels = [1500,1500,1500,1500,1500,ch1,1500,1500]
 print new_msg
 pub.publish(new_msg)

# Intializes everything
def start():
 # starts the node
 rospy.init_node('Joy2MAVROS')
 # publishing 
 global pub
 pub = rospy.Publisher('/mavros/rc/override', OverrideRCIn, queue_size=1)
 # subscribed to joystick inputs on topic "joy"
 rospy.Subscriber("joy", Joy, callback)


if __name__ == '__main__':
 start()
 rospy.spin()
