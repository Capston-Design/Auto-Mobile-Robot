; Auto-generated. Do not edit!


(cl:in-package ImageProcess_Node-srv)


;//! \htmlinclude Detect-request.msg.html

(cl:defclass <Detect-request> (roslisp-msg-protocol:ros-message)
  ((roi_image
    :reader roi_image
    :initarg :roi_image
    :type cl:float
    :initform 0.0))
)

(cl:defclass Detect-request (<Detect-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Detect-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Detect-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ImageProcess_Node-srv:<Detect-request> is deprecated: use ImageProcess_Node-srv:Detect-request instead.")))

(cl:ensure-generic-function 'roi_image-val :lambda-list '(m))
(cl:defmethod roi_image-val ((m <Detect-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ImageProcess_Node-srv:roi_image-val is deprecated.  Use ImageProcess_Node-srv:roi_image instead.")
  (roi_image m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Detect-request>) ostream)
  "Serializes a message object of type '<Detect-request>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'roi_image))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Detect-request>) istream)
  "Deserializes a message object of type '<Detect-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'roi_image) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Detect-request>)))
  "Returns string type for a service object of type '<Detect-request>"
  "ImageProcess_Node/DetectRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Detect-request)))
  "Returns string type for a service object of type 'Detect-request"
  "ImageProcess_Node/DetectRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Detect-request>)))
  "Returns md5sum for a message object of type '<Detect-request>"
  "c5cdbbf937a2b7afdb40f16147414b23")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Detect-request)))
  "Returns md5sum for a message object of type 'Detect-request"
  "c5cdbbf937a2b7afdb40f16147414b23")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Detect-request>)))
  "Returns full string definition for message of type '<Detect-request>"
  (cl:format cl:nil "float32 roi_image~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Detect-request)))
  "Returns full string definition for message of type 'Detect-request"
  (cl:format cl:nil "float32 roi_image~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Detect-request>))
  (cl:+ 0
     4
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
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ImageProcess_Node-srv:<Detect-response> is deprecated: use ImageProcess_Node-srv:Detect-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <Detect-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ImageProcess_Node-srv:result-val is deprecated.  Use ImageProcess_Node-srv:result instead.")
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
  "ImageProcess_Node/DetectResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Detect-response)))
  "Returns string type for a service object of type 'Detect-response"
  "ImageProcess_Node/DetectResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Detect-response>)))
  "Returns md5sum for a message object of type '<Detect-response>"
  "c5cdbbf937a2b7afdb40f16147414b23")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Detect-response)))
  "Returns md5sum for a message object of type 'Detect-response"
  "c5cdbbf937a2b7afdb40f16147414b23")
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
  "ImageProcess_Node/Detect")