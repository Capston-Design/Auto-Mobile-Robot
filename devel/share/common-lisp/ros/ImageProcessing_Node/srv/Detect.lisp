; Auto-generated. Do not edit!


(cl:in-package ImageProcessing_Node-srv)


;//! \htmlinclude Detect-request.msg.html

(cl:defclass <Detect-request> (roslisp-msg-protocol:ros-message)
  ((roi_image
    :reader roi_image
    :initarg :roi_image
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image)))
)

(cl:defclass Detect-request (<Detect-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Detect-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Detect-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ImageProcessing_Node-srv:<Detect-request> is deprecated: use ImageProcessing_Node-srv:Detect-request instead.")))

(cl:ensure-generic-function 'roi_image-val :lambda-list '(m))
(cl:defmethod roi_image-val ((m <Detect-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ImageProcessing_Node-srv:roi_image-val is deprecated.  Use ImageProcessing_Node-srv:roi_image instead.")
  (roi_image m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Detect-request>) ostream)
  "Serializes a message object of type '<Detect-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'roi_image) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Detect-request>) istream)
  "Deserializes a message object of type '<Detect-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'roi_image) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Detect-request>)))
  "Returns string type for a service object of type '<Detect-request>"
  "ImageProcessing_Node/DetectRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Detect-request)))
  "Returns string type for a service object of type 'Detect-request"
  "ImageProcessing_Node/DetectRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Detect-request>)))
  "Returns md5sum for a message object of type '<Detect-request>"
  "a3926dcdd8f922bd0ad49b8c9d565283")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Detect-request)))
  "Returns md5sum for a message object of type 'Detect-request"
  "a3926dcdd8f922bd0ad49b8c9d565283")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Detect-request>)))
  "Returns full string definition for message of type '<Detect-request>"
  (cl:format cl:nil "sensor_msgs/Image roi_image~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Detect-request)))
  "Returns full string definition for message of type 'Detect-request"
  (cl:format cl:nil "sensor_msgs/Image roi_image~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Detect-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'roi_image))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Detect-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Detect-request
    (cl:cons ':roi_image (roi_image msg))
))
;//! \htmlinclude Detect-response.msg.html

(cl:defclass <Detect-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:string
    :initform ""))
)

(cl:defclass Detect-response (<Detect-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Detect-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Detect-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ImageProcessing_Node-srv:<Detect-response> is deprecated: use ImageProcessing_Node-srv:Detect-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <Detect-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ImageProcessing_Node-srv:result-val is deprecated.  Use ImageProcessing_Node-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Detect-response>) ostream)
  "Serializes a message object of type '<Detect-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'result))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'result))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Detect-response>) istream)
  "Deserializes a message object of type '<Detect-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'result) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'result) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Detect-response>)))
  "Returns string type for a service object of type '<Detect-response>"
  "ImageProcessing_Node/DetectResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Detect-response)))
  "Returns string type for a service object of type 'Detect-response"
  "ImageProcessing_Node/DetectResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Detect-response>)))
  "Returns md5sum for a message object of type '<Detect-response>"
  "a3926dcdd8f922bd0ad49b8c9d565283")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Detect-response)))
  "Returns md5sum for a message object of type 'Detect-response"
  "a3926dcdd8f922bd0ad49b8c9d565283")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Detect-response>)))
  "Returns full string definition for message of type '<Detect-response>"
  (cl:format cl:nil "string result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Detect-response)))
  "Returns full string definition for message of type 'Detect-response"
  (cl:format cl:nil "string result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Detect-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'result))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Detect-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Detect-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Detect)))
  'Detect-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Detect)))
  'Detect-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Detect)))
  "Returns string type for a service object of type '<Detect>"
  "ImageProcessing_Node/Detect")