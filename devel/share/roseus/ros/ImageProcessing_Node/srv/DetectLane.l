;; Auto-generated. Do not edit!


(when (boundp 'ImageProcessing_Node::DetectLane)
  (if (not (find-package "IMAGEPROCESSING_NODE"))
    (make-package "IMAGEPROCESSING_NODE"))
  (shadow 'DetectLane (find-package "IMAGEPROCESSING_NODE")))
(unless (find-package "IMAGEPROCESSING_NODE::DETECTLANE")
  (make-package "IMAGEPROCESSING_NODE::DETECTLANE"))
(unless (find-package "IMAGEPROCESSING_NODE::DETECTLANEREQUEST")
  (make-package "IMAGEPROCESSING_NODE::DETECTLANEREQUEST"))
(unless (find-package "IMAGEPROCESSING_NODE::DETECTLANERESPONSE")
  (make-package "IMAGEPROCESSING_NODE::DETECTLANERESPONSE"))

(in-package "ROS")

(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))




(defclass ImageProcessing_Node::DetectLaneRequest
  :super ros::object
  :slots (_lane_img ))

(defmethod ImageProcessing_Node::DetectLaneRequest
  (:init
   (&key
    ((:lane_img __lane_img) (instance sensor_msgs::Image :init))
    )
   (send-super :init)
   (setq _lane_img __lane_img)
   self)
  (:lane_img
   (&rest __lane_img)
   (if (keywordp (car __lane_img))
       (send* _lane_img __lane_img)
     (progn
       (if __lane_img (setq _lane_img (car __lane_img)))
       _lane_img)))
  (:serialization-length
   ()
   (+
    ;; sensor_msgs/Image _lane_img
    (send _lane_img :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; sensor_msgs/Image _lane_img
       (send _lane_img :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; sensor_msgs/Image _lane_img
     (send _lane_img :deserialize buf ptr-) (incf ptr- (send _lane_img :serialization-length))
   ;;
   self)
  )

(defclass ImageProcessing_Node::DetectLaneResponse
  :super ros::object
  :slots (_error ))

(defmethod ImageProcessing_Node::DetectLaneResponse
  (:init
   (&key
    ((:error __error) 0.0)
    )
   (send-super :init)
   (setq _error (float __error))
   self)
  (:error
   (&optional __error)
   (if __error (setq _error __error)) _error)
  (:serialization-length
   ()
   (+
    ;; float32 _error
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _error
       (sys::poke _error (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _error
     (setq _error (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass ImageProcessing_Node::DetectLane
  :super ros::object
  :slots ())

(setf (get ImageProcessing_Node::DetectLane :md5sum-) "a6e07a703491622fa69b198031d85522")
(setf (get ImageProcessing_Node::DetectLane :datatype-) "ImageProcessing_Node/DetectLane")
(setf (get ImageProcessing_Node::DetectLane :request) ImageProcessing_Node::DetectLaneRequest)
(setf (get ImageProcessing_Node::DetectLane :response) ImageProcessing_Node::DetectLaneResponse)

(defmethod ImageProcessing_Node::DetectLaneRequest
  (:response () (instance ImageProcessing_Node::DetectLaneResponse :init)))

(setf (get ImageProcessing_Node::DetectLaneRequest :md5sum-) "a6e07a703491622fa69b198031d85522")
(setf (get ImageProcessing_Node::DetectLaneRequest :datatype-) "ImageProcessing_Node/DetectLaneRequest")
(setf (get ImageProcessing_Node::DetectLaneRequest :definition-)
      "sensor_msgs/Image lane_img

================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of cameara
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id
---
float32 error
")

(setf (get ImageProcessing_Node::DetectLaneResponse :md5sum-) "a6e07a703491622fa69b198031d85522")
(setf (get ImageProcessing_Node::DetectLaneResponse :datatype-) "ImageProcessing_Node/DetectLaneResponse")
(setf (get ImageProcessing_Node::DetectLaneResponse :definition-)
      "sensor_msgs/Image lane_img

================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of cameara
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id
---
float32 error
")



(provide :ImageProcessing_Node/DetectLane "a6e07a703491622fa69b198031d85522")


