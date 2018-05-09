// Generated by gencpp from file ImageProcess_Node/DetectLaneGoal.msg
// DO NOT EDIT!


#ifndef IMAGEPROCESS_NODE_MESSAGE_DETECTLANEGOAL_H
#define IMAGEPROCESS_NODE_MESSAGE_DETECTLANEGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <sensor_msgs/Image.h>

namespace ImageProcess_Node
{
template <class ContainerAllocator>
struct DetectLaneGoal_
{
  typedef DetectLaneGoal_<ContainerAllocator> Type;

  DetectLaneGoal_()
    : road_image()  {
    }
  DetectLaneGoal_(const ContainerAllocator& _alloc)
    : road_image(_alloc)  {
  (void)_alloc;
    }



   typedef  ::sensor_msgs::Image_<ContainerAllocator>  _road_image_type;
  _road_image_type road_image;




  typedef boost::shared_ptr< ::ImageProcess_Node::DetectLaneGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ImageProcess_Node::DetectLaneGoal_<ContainerAllocator> const> ConstPtr;

}; // struct DetectLaneGoal_

typedef ::ImageProcess_Node::DetectLaneGoal_<std::allocator<void> > DetectLaneGoal;

typedef boost::shared_ptr< ::ImageProcess_Node::DetectLaneGoal > DetectLaneGoalPtr;
typedef boost::shared_ptr< ::ImageProcess_Node::DetectLaneGoal const> DetectLaneGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ImageProcess_Node::DetectLaneGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ImageProcess_Node::DetectLaneGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ImageProcess_Node

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'ImageProcess_Node': ['/home/seopaul/Auto-Mobile-Robot/devel/share/ImageProcess_Node/msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ImageProcess_Node::DetectLaneGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ImageProcess_Node::DetectLaneGoal_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ImageProcess_Node::DetectLaneGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ImageProcess_Node::DetectLaneGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ImageProcess_Node::DetectLaneGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ImageProcess_Node::DetectLaneGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ImageProcess_Node::DetectLaneGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "420c5a2819193dac99e8a245e08c3594";
  }

  static const char* value(const ::ImageProcess_Node::DetectLaneGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x420c5a2819193dacULL;
  static const uint64_t static_value2 = 0x99e8a245e08c3594ULL;
};

template<class ContainerAllocator>
struct DataType< ::ImageProcess_Node::DetectLaneGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ImageProcess_Node/DetectLaneGoal";
  }

  static const char* value(const ::ImageProcess_Node::DetectLaneGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ImageProcess_Node::DetectLaneGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# Define the goal\n\
sensor_msgs/Image road_image\n\
\n\
================================================================================\n\
MSG: sensor_msgs/Image\n\
# This message contains an uncompressed image\n\
# (0, 0) is at top-left corner of image\n\
#\n\
\n\
Header header        # Header timestamp should be acquisition time of image\n\
                     # Header frame_id should be optical frame of camera\n\
                     # origin of frame should be optical center of cameara\n\
                     # +x should point to the right in the image\n\
                     # +y should point down in the image\n\
                     # +z should point into to plane of the image\n\
                     # If the frame_id here and the frame_id of the CameraInfo\n\
                     # message associated with the image conflict\n\
                     # the behavior is undefined\n\
\n\
uint32 height         # image height, that is, number of rows\n\
uint32 width          # image width, that is, number of columns\n\
\n\
# The legal values for encoding are in file src/image_encodings.cpp\n\
# If you want to standardize a new string format, join\n\
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.\n\
\n\
string encoding       # Encoding of pixels -- channel meaning, ordering, size\n\
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h\n\
\n\
uint8 is_bigendian    # is this data bigendian?\n\
uint32 step           # Full row length in bytes\n\
uint8[] data          # actual matrix data, size is (step * rows)\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
";
  }

  static const char* value(const ::ImageProcess_Node::DetectLaneGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ImageProcess_Node::DetectLaneGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.road_image);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct DetectLaneGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ImageProcess_Node::DetectLaneGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ImageProcess_Node::DetectLaneGoal_<ContainerAllocator>& v)
  {
    s << indent << "road_image: ";
    s << std::endl;
    Printer< ::sensor_msgs::Image_<ContainerAllocator> >::stream(s, indent + "  ", v.road_image);
  }
};

} // namespace message_operations
} // namespace ros

#endif // IMAGEPROCESS_NODE_MESSAGE_DETECTLANEGOAL_H
