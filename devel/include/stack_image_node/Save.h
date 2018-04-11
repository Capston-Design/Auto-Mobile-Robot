// Generated by gencpp from file stack_image_node/Save.msg
// DO NOT EDIT!


#ifndef STACK_IMAGE_NODE_MESSAGE_SAVE_H
#define STACK_IMAGE_NODE_MESSAGE_SAVE_H

#include <ros/service_traits.h>


#include <stack_image_node/SaveRequest.h>
#include <stack_image_node/SaveResponse.h>


namespace stack_image_node
{

struct Save
{

typedef SaveRequest Request;
typedef SaveResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct Save
} // namespace stack_image_node


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::stack_image_node::Save > {
  static const char* value()
  {
    return "2c75fafdcb7a71b1c42c8cdb584b2cf6";
  }

  static const char* value(const ::stack_image_node::Save&) { return value(); }
};

template<>
struct DataType< ::stack_image_node::Save > {
  static const char* value()
  {
    return "stack_image_node/Save";
  }

  static const char* value(const ::stack_image_node::Save&) { return value(); }
};


// service_traits::MD5Sum< ::stack_image_node::SaveRequest> should match 
// service_traits::MD5Sum< ::stack_image_node::Save > 
template<>
struct MD5Sum< ::stack_image_node::SaveRequest>
{
  static const char* value()
  {
    return MD5Sum< ::stack_image_node::Save >::value();
  }
  static const char* value(const ::stack_image_node::SaveRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::stack_image_node::SaveRequest> should match 
// service_traits::DataType< ::stack_image_node::Save > 
template<>
struct DataType< ::stack_image_node::SaveRequest>
{
  static const char* value()
  {
    return DataType< ::stack_image_node::Save >::value();
  }
  static const char* value(const ::stack_image_node::SaveRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::stack_image_node::SaveResponse> should match 
// service_traits::MD5Sum< ::stack_image_node::Save > 
template<>
struct MD5Sum< ::stack_image_node::SaveResponse>
{
  static const char* value()
  {
    return MD5Sum< ::stack_image_node::Save >::value();
  }
  static const char* value(const ::stack_image_node::SaveResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::stack_image_node::SaveResponse> should match 
// service_traits::DataType< ::stack_image_node::Save > 
template<>
struct DataType< ::stack_image_node::SaveResponse>
{
  static const char* value()
  {
    return DataType< ::stack_image_node::Save >::value();
  }
  static const char* value(const ::stack_image_node::SaveResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // STACK_IMAGE_NODE_MESSAGE_SAVE_H
