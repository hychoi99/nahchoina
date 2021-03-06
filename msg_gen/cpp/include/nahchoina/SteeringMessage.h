/* Auto-generated by genmsg_cpp for file /home/turtlebot/jackhachoi-workspace/sandbox/nahchoina/msg/SteeringMessage.msg */
#ifndef NAHCHOINA_MESSAGE_STEERINGMESSAGE_H
#define NAHCHOINA_MESSAGE_STEERINGMESSAGE_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"


namespace nahchoina
{
template <class ContainerAllocator>
struct SteeringMessage_ {
  typedef SteeringMessage_<ContainerAllocator> Type;

  SteeringMessage_()
  : event()
  , linear(0.0)
  , angular(0.0)
  {
  }

  SteeringMessage_(const ContainerAllocator& _alloc)
  : event(_alloc)
  , linear(0.0)
  , angular(0.0)
  {
  }

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _event_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  event;

  typedef float _linear_type;
  float linear;

  typedef float _angular_type;
  float angular;


  typedef boost::shared_ptr< ::nahchoina::SteeringMessage_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::nahchoina::SteeringMessage_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct SteeringMessage
typedef  ::nahchoina::SteeringMessage_<std::allocator<void> > SteeringMessage;

typedef boost::shared_ptr< ::nahchoina::SteeringMessage> SteeringMessagePtr;
typedef boost::shared_ptr< ::nahchoina::SteeringMessage const> SteeringMessageConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::nahchoina::SteeringMessage_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::nahchoina::SteeringMessage_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace nahchoina

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::nahchoina::SteeringMessage_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::nahchoina::SteeringMessage_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::nahchoina::SteeringMessage_<ContainerAllocator> > {
  static const char* value() 
  {
    return "992808bfa7b78263265c8590a7a20a3c";
  }

  static const char* value(const  ::nahchoina::SteeringMessage_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x992808bfa7b78263ULL;
  static const uint64_t static_value2 = 0x265c8590a7a20a3cULL;
};

template<class ContainerAllocator>
struct DataType< ::nahchoina::SteeringMessage_<ContainerAllocator> > {
  static const char* value() 
  {
    return "nahchoina/SteeringMessage";
  }

  static const char* value(const  ::nahchoina::SteeringMessage_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::nahchoina::SteeringMessage_<ContainerAllocator> > {
  static const char* value() 
  {
    return "string event\n\
float32 linear\n\
float32 angular\n\
\n\
";
  }

  static const char* value(const  ::nahchoina::SteeringMessage_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::nahchoina::SteeringMessage_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.event);
    stream.next(m.linear);
    stream.next(m.angular);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct SteeringMessage_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::nahchoina::SteeringMessage_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::nahchoina::SteeringMessage_<ContainerAllocator> & v) 
  {
    s << indent << "event: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.event);
    s << indent << "linear: ";
    Printer<float>::stream(s, indent + "  ", v.linear);
    s << indent << "angular: ";
    Printer<float>::stream(s, indent + "  ", v.angular);
  }
};


} // namespace message_operations
} // namespace ros

#endif // NAHCHOINA_MESSAGE_STEERINGMESSAGE_H

