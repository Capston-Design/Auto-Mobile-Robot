; Auto-generated. Do not edit!


(cl:in-package ImageProcessing_Node-msg)


;//! \htmlinclude DetectLaneFeedback.msg.html

(cl:defclass <DetectLaneFeedback> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:string
    :initform ""))
)

(cl:defclass DetectLaneFeedback (<DetectLaneFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DetectLaneFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DetectLaneFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ImageProcessing_Node-msg:<DetectLaneFeedback> is deprecated: use ImageProcessing_Node-msg:DetectLaneFeedback instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <DetectLaneFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ImageProcessing_Node-msg:result-val is deprecated.  Use ImageProcessing_Node-msg:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DetectLaneFeedback>) ostream)
  "Serializes a message object of type '<DetectLaneFeedback>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'result))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'result))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DetectLaneFeedback>) istream)
  "Deserializes a message object of type '<DetectLaneFeedback>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DetectLaneFeedback>)))
  "Returns string type for a message object of type '<DetectLaneFeedback>"
  "ImageProcessing_Node/DetectLaneFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DetectLaneFeedback)))
  "Returns string type for a message object of type 'DetectLaneFeedback"
  "ImageProcessing_Node/DetectLaneFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DetectLaneFeedback>)))
  "Returns md5sum for a message object of type '<DetectLaneFeedback>"
  "c22f2a1ed8654a0b365f1bb3f7ff2c0f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DetectLaneFeedback)))
  "Returns md5sum for a message object of type 'DetectLaneFeedback"
  "c22f2a1ed8654a0b365f1bb3f7ff2c0f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DetectLaneFeedback>)))
  "Returns full string definition for message of type '<DetectLaneFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%string result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DetectLaneFeedback)))
  "Returns full string definition for message of type 'DetectLaneFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%string result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DetectLaneFeedback>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'result))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DetectLaneFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'DetectLaneFeedback
    (cl:cons ':result (result msg))
))
