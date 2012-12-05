#!/usr/bin/python

PKG = 'imu_serial' # this package name
import roslib; roslib.load_manifest(PKG)
from sensor_msgs.msg import LaserScan
import rospy
#from Numeric import ones

def imu_serial():
    pub = rospy.Publisher('laser_scan', LaserScan)
    rospy.init_node('imu_serial')
    laser_msg = LaserScan()

    laser_msg.header.frame_id = 'laser'
    laser_msg.angle_min = -1.5
    laser_msg.angle_max = 1.5
    laser_msg.angle_increment = 0.1
    laser_msg.time_increment = 0.1
    laser_msg.scan_time = 0.1
    laser_msg.range_min = 0.5
    laser_msg.range_max = 1.5    
    laser_msg.ranges = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 9.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.1, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 5.0, 1.0]
    laser_msg.intensities = laser_msg.ranges 

    r = rospy.Rate(100) # 10hz
    while not rospy.is_shutdown():
        laser_msg.header.stamp = rospy.get_rostime()
        pub.publish(laser_msg)
        r.sleep()


if __name__ == '__main__':
  try:
        imu_serial()
  except rospy.ROSInterruptException: pass



