// Generated by gencpp from file open_manipulator_msgs/KinematicsPose.msg
// DO NOT EDIT!


#ifndef OPEN_MANIPULATOR_MSGS_MESSAGE_KINEMATICSPOSE_H
#define OPEN_MANIPULATOR_MSGS_MESSAGE_KINEMATICSPOSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Pose.h>

namespace open_manipulator_msgs
{
template <class ContainerAllocator>
struct KinematicsPose_
{
  typedef KinematicsPose_<ContainerAllocator> Type;

  KinematicsPose_()
    : group_name()
    , pose()
    , move_time(0.0)  {
    }
  KinematicsPose_(const ContainerAllocator& _alloc)
    : group_name(_alloc)
    , pose(_alloc)
    , move_time(0.0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _group_name_type;
  _group_name_type group_name;

   typedef  ::geometry_msgs::Pose_<ContainerAllocator>  _pose_type;
  _pose_type pose;

   typedef double _move_time_type;
  _move_time_type move_time;





  typedef boost::shared_ptr< ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator> const> ConstPtr;

}; // struct KinematicsPose_

typedef ::open_manipulator_msgs::KinematicsPose_<std::allocator<void> > KinematicsPose;

typedef boost::shared_ptr< ::open_manipulator_msgs::KinematicsPose > KinematicsPosePtr;
typedef boost::shared_ptr< ::open_manipulator_msgs::KinematicsPose const> KinematicsPoseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator1> & lhs, const ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator2> & rhs)
{
  return lhs.group_name == rhs.group_name &&
    lhs.pose == rhs.pose &&
    lhs.move_time == rhs.move_time;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator1> & lhs, const ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace open_manipulator_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator> >
{
  static const char* value()
  {
    return "0a4a4aa6474f91f273e46b9154c8ebc8";
  }

  static const char* value(const ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x0a4a4aa6474f91f2ULL;
  static const uint64_t static_value2 = 0x73e46b9154c8ebc8ULL;
};

template<class ContainerAllocator>
struct DataType< ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator> >
{
  static const char* value()
  {
    return "open_manipulator_msgs/KinematicsPose";
  }

  static const char* value(const ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string    	        group_name\n"
"geometry_msgs/Pose  pose\n"
"float64             move_time\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Pose\n"
"# A representation of pose in free space, composed of position and orientation. \n"
"Point position\n"
"Quaternion orientation\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point\n"
"# This contains the position of a point in free space\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Quaternion\n"
"# This represents an orientation in free space in quaternion form.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"float64 w\n"
;
  }

  static const char* value(const ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.group_name);
      stream.next(m.pose);
      stream.next(m.move_time);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct KinematicsPose_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::open_manipulator_msgs::KinematicsPose_<ContainerAllocator>& v)
  {
    s << indent << "group_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.group_name);
    s << indent << "pose: ";
    s << std::endl;
    Printer< ::geometry_msgs::Pose_<ContainerAllocator> >::stream(s, indent + "  ", v.pose);
    s << indent << "move_time: ";
    Printer<double>::stream(s, indent + "  ", v.move_time);
  }
};

} // namespace message_operations
} // namespace ros

#endif // OPEN_MANIPULATOR_MSGS_MESSAGE_KINEMATICSPOSE_H
