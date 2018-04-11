; Auto-generated. Do not edit!


(cl:in-package stack_image_node-srv)


;//! \htmlinclude Save-request.msg.html

(cl:defclass <Save-request> (roslisp-msg-protocol:ros-message)
  ((flag_message
    :reader flag_message
    :initarg :flag_message
    :type cl:string
    :initform ""))
)

(cl:defclass Save-request (<Save-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Save-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Save-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name stack_image_node-srv:<Save-request> is deprecated: use stack_image_node-srv:Save-request instead.")))

(cl:ensure-generic-function 'flag_message-val :lambda-list '(m))
(cl:defmethod flag_message-val ((m <Save-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader stack_image_node-srv:flag_message-val is deprecated.  Use stack_image_node-srv:flag_message instead.")
  (flag_message m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Save-request>) ostream)
  "Serializes a message object of type '<Save-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'flag_message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'flag_message))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Save-request>) istream)
  "Deserializes a message object of type '<Save-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'flag_message) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'flag_message) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Save-request>)))
  "Returns string type for a service object of type '<Save-request>"
  "stack_image_node/SaveRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Save-request)))
  "Returns string type for a service object of type 'Save-request"
  "stack_image_node/SaveRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Save-request>)))
  "Returns md5sum for a message object of type '<Save-request>"
  "2c75fafdcb7a71b1c42c8cdb584b2cf6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Save-request)))
  "Returns md5sum for a message object of type 'Save-request"
  "2c75fafdcb7a71b1c42c8cdb584b2cf6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Save-request>)))
  "Returns full string definition for message of type '<Save-request>"
  (cl:format cl:nil "string flag_message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Save-request)))
  "Returns full string definition for message of type 'Save-request"
  (cl:format cl:nil "string flag_message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Save-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'flag_message))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Save-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Save-request
    (cl:cons ':flag_message (flag_message msg))
))
;//! \htmlinclude Save-response.msg.html

(cl:defclass <Save-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Save-response (<Save-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Save-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Save-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name stack_image_node-srv:<Save-response> is deprecated: use stack_image_node-srv:Save-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <Save-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader stack_image_node-srv:result-val is deprecated.  Use stack_image_node-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Save-response>) ostream)
  "Serializes a message object of type '<Save-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Save-response>) istream)
  "Deserializes a message object of type '<Save-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Save-response>)))
  "Returns string type for a service object of type '<Save-response>"
  "stack_image_node/SaveResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Save-response)))
  "Returns string type for a service object of type 'Save-response"
  "stack_image_node/SaveResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Save-response>)))
  "Returns md5sum for a message object of type '<Save-response>"
  "2c75fafdcb7a71b1c42c8cdb584b2cf6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Save-response)))
  "Returns md5sum for a message object of type 'Save-response"
  "2c75fafdcb7a71b1c42c8cdb584b2cf6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Save-response>)))
  "Returns full string definition for message of type '<Save-response>"
  (cl:format cl:nil "bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Save-response)))
  "Returns full string definition for message of type 'Save-response"
  (cl:format cl:nil "bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Save-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Save-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Save-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Save)))
  'Save-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Save)))
  'Save-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Save)))
  "Returns string type for a service object of type '<Save>"
  "stack_image_node/Save")