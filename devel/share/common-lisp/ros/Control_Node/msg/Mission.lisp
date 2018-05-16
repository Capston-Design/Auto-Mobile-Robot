; Auto-generated. Do not edit!


(cl:in-package Control_Node-msg)


;//! \htmlinclude Mission.msg.html

(cl:defclass <Mission> (roslisp-msg-protocol:ros-message)
  ((traffic
    :reader traffic
    :initarg :traffic
    :type cl:boolean
    :initform cl:nil)
   (parking
    :reader parking
    :initarg :parking
    :type cl:boolean
    :initform cl:nil)
   (crossbar
    :reader crossbar
    :initarg :crossbar
    :type cl:boolean
    :initform cl:nil)
   (tunnel
    :reader tunnel
    :initarg :tunnel
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Mission (<Mission>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Mission>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Mission)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name Control_Node-msg:<Mission> is deprecated: use Control_Node-msg:Mission instead.")))

(cl:ensure-generic-function 'traffic-val :lambda-list '(m))
(cl:defmethod traffic-val ((m <Mission>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader Control_Node-msg:traffic-val is deprecated.  Use Control_Node-msg:traffic instead.")
  (traffic m))

(cl:ensure-generic-function 'parking-val :lambda-list '(m))
(cl:defmethod parking-val ((m <Mission>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader Control_Node-msg:parking-val is deprecated.  Use Control_Node-msg:parking instead.")
  (parking m))

(cl:ensure-generic-function 'crossbar-val :lambda-list '(m))
(cl:defmethod crossbar-val ((m <Mission>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader Control_Node-msg:crossbar-val is deprecated.  Use Control_Node-msg:crossbar instead.")
  (crossbar m))

(cl:ensure-generic-function 'tunnel-val :lambda-list '(m))
(cl:defmethod tunnel-val ((m <Mission>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader Control_Node-msg:tunnel-val is deprecated.  Use Control_Node-msg:tunnel instead.")
  (tunnel m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Mission>) ostream)
  "Serializes a message object of type '<Mission>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'traffic) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'parking) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'crossbar) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'tunnel) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Mission>) istream)
  "Deserializes a message object of type '<Mission>"
    (cl:setf (cl:slot-value msg 'traffic) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'parking) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'crossbar) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'tunnel) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Mission>)))
  "Returns string type for a message object of type '<Mission>"
  "Control_Node/Mission")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Mission)))
  "Returns string type for a message object of type 'Mission"
  "Control_Node/Mission")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Mission>)))
  "Returns md5sum for a message object of type '<Mission>"
  "132b675c11a085c243deb3519223ef08")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Mission)))
  "Returns md5sum for a message object of type 'Mission"
  "132b675c11a085c243deb3519223ef08")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Mission>)))
  "Returns full string definition for message of type '<Mission>"
  (cl:format cl:nil "bool traffic~%bool parking~%bool crossbar~%bool tunnel~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Mission)))
  "Returns full string definition for message of type 'Mission"
  (cl:format cl:nil "bool traffic~%bool parking~%bool crossbar~%bool tunnel~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Mission>))
  (cl:+ 0
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Mission>))
  "Converts a ROS message object to a list"
  (cl:list 'Mission
    (cl:cons ':traffic (traffic msg))
    (cl:cons ':parking (parking msg))
    (cl:cons ':crossbar (crossbar msg))
    (cl:cons ':tunnel (tunnel msg))
))
