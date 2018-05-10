; Auto-generated. Do not edit!


(cl:in-package ImageProcessing_Node-srv)


;//! \htmlinclude DetectLane-request.msg.html

(cl:defclass <DetectLane-request> (roslisp-msg-protocol:ros-message)
  ((lane_img
    :reader lane_img
    :initarg :lane_img
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image)))
)

(cl:defclass DetectLane-request (<DetectLane-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DetectLane-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DetectLane-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ImageProcessing_Node-srv:<DetectLane-request> is deprecated: use ImageProcessing_Node-srv:DetectLane-request instead.")))

(cl:ensure-generic-function 'lane_img-val :lambda-list '(m))
(cl:defmethod lane_img-val ((m <DetectLane-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ImageProcessing_Node-srv:lane_img-val is deprecated.  Use ImageProcessing_Node-srv:lane_img instead.")
  (lane_img m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DetectLane-request>) ostream)
  "Serializes a message object of type '<DetectLane-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'lane_img) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DetectLane-request>) istream)
  "Deserializes a message object of type '<DetectLane-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'lane_img) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DetectLane-request>)))
  "Returns string type for a service object of type '<DetectLane-request>"
  "ImageProcessing_Node/DetectLaneRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DetectLane-request)))
  "Returns string type for a service object of type 'DetectLane-request"
  "ImageProcessing_Node/DetectLaneRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DetectLane-request>)))
  "Returns md5sum for a message object of type '<DetectLane-request>"
  "a6e07a703491622fa69b198031d85522")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DetectLane-request)))
  "Returns md5sum for a message object of type 'DetectLane-request"
  "a6e07a703491622fa69b198031d85522")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DetectLane-request>)))
  "Returns full string definition for message of type '<DetectLane-request>"
  (cl:format cl:nil "sensor_msgs/Image lane_img~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DetectLane-request)))
  "Returns full string definition for message of type 'DetectLane-request"
  (cl:format cl:nil "sensor_msgs/Image lane_img~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DetectLane-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'lane_img))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DetectLane-request>))
  "Converts a ROS message object to a list"
  (cl:list 'DetectLane-request
    (cl:cons ':lane_img (lane_img msg))
))
;//! \htmlinclude DetectLane-response.msg.html

(cl:defclass <DetectLane-response> (roslisp-msg-protocol:ros-message)
  ((error
    :reader error
    :initarg :error
    :type cl:float
    :initform 0.0))
)

(cl:defclass DetectLane-response (<DetectLane-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DetectLane-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DetectLane-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ImageProcessing_Node-srv:<DetectLane-response> is deprecated: use ImageProcessing_Node-srv:DetectLane-response instead.")))

(cl:ensure-generic-function 'error-val :lambda-list '(m))
(cl:defmethod error-val ((m <DetectLane-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ImageProcessing_Node-srv:error-val is deprecated.  Use ImageProcessing_Node-srv:error instead.")
  (error m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DetectLane-response>) ostream)
  "Serializes a message object of type '<DetectLane-response>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'error))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DetectLane-response>) istream)
  "Deserializes a message object of type '<DetectLane-response>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'error) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DetectLane-response>)))
  "Returns string type for a service object of type '<DetectLane-response>"
  "ImageProcessing_Node/DetectLaneResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DetectLane-response)))
  "Returns string type for a service object of type 'DetectLane-response"
  "ImageProcessing_Node/DetectLaneResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DetectLane-response>)))
  "Returns md5sum for a message object of type '<DetectLane-response>"
  "a6e07a703491622fa69b198031d85522")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DetectLane-response)))
  "Returns md5sum for a message object of type 'DetectLane-response"
  "a6e07a703491622fa69b198031d85522")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DetectLane-response>)))
  "Returns full string definition for message of type '<DetectLane-response>"
  (cl:format cl:nil "float32 error~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DetectLane-response)))
  "Returns full string definition for message of type 'DetectLane-response"
  (cl:format cl:nil "float32 error~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DetectLane-response>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DetectLane-response>))
  "Converts a ROS message object to a list"
  (cl:list 'DetectLane-response
    (cl:cons ':error (error msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'DetectLane)))
  'DetectLane-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'DetectLane)))
  'DetectLane-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DetectLane)))
  "Returns string type for a service object of type '<DetectLane>"
  "ImageProcessing_Node/DetectLane")