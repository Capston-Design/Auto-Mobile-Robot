;; Auto-generated. Do not edit!


(when (boundp 'ImageProcessing_Node::Detect)
  (if (not (find-package "IMAGEPROCESSING_NODE"))
    (make-package "IMAGEPROCESSING_NODE"))
  (shadow 'Detect (find-package "IMAGEPROCESSING_NODE")))
(unless (find-package "IMAGEPROCESSING_NODE::DETECT")
  (make-package "IMAGEPROCESSING_NODE::DETECT"))
(unless (find-package "IMAGEPROCESSING_NODE::DETECTREQUEST")
  (make-package "IMAGEPROCESSING_NODE::DETECTREQUEST"))
(unless (find-package "IMAGEPROCESSING_NODE::DETECTRESPONSE")
  (make-package "IMAGEPROCESSING_NODE::DETECTRESPONSE"))

(in-package "ROS")

(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))




(defclass ImageProcessing_Node::DetectRequest
  :super ros::object
  :slots (_roi_image ))

(defmethod ImageProcessing_Node::DetectRequest
  (:init
   (&key
    ((:roi_image __roi_image) (instance sensor_msgs::Image :init))
    )
   (send-super :init)
   (setq _roi_image __roi_image)
   self)
  (:roi_image
   (&rest __roi_image)
   (if (keywordp (car __roi_image))
       (send* _roi_image __roi_image)
     (progn
       (if __roi_image (setq _roi_image (car __roi_image)))
       _roi_image)))
  (:serialization-length
   ()
   (+
    ;; sensor_msgs/Image _roi_image
    (send _roi_image :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; sensor_msgs/Image _roi_image
       (send _roi_image :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; sensor_msgs/Image _roi_image
     (send _roi_image :deserialize buf ptr-) (incf ptr- (send _roi_image :serialization-length))
   ;;
   self)
  )

(defclass ImageProcessing_Node::DetectResponse
  :super ros::object
  :slots (_result ))

(defmethod ImageProcessing_Node::DetectResponse
  (:init
   (&key
    ((:result __result) "")
    )
   (send-super :init)
   (setq _result (string __result))
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; string _result
    4 (length _result)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _result
       (write-long (length _result) s) (princ _result s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _result
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _result (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass ImageProcessing_Node::Detect
  :super ros::object
  :slots ())

(setf (get ImageProcessing_Node::Detect :md5sum-) "a3926dcdd8f922bd0ad49b8c9d565283")
(setf (get ImageProcessing_Node::Detect :datatype-) "ImageProcessing_Node/Detect")
(setf (get ImageProcessing_Node::Detect :request) ImageProcessing_Node::DetectRequest)
(setf (get ImageProcessing_Node::Detect :response) ImageProcessing_Node::DetectResponse)

(defmethod ImageProcessing_Node::DetectRequest
  (:response () (instance ImageProcessing_Node::DetectResponse :init)))

(setf (get ImageProcessing_Node::DetectRequest :md5sum-) "a3926dcdd8f922bd0ad49b8c9d565283")
(setf (get ImageProcessing_Node::DetectRequest :datatype-) "ImageProcessing_Node/DetectRequest")
(setf (get ImageProcessing_Node::DetectRequest :definition-)
      "sensor_msgs/Image roi_image

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
string result
")

(setf (get ImageProcessing_Node::DetectResponse :md5sum-) "a3926dcdd8f922bd0ad49b8c9d565283")
(setf (get ImageProcessing_Node::DetectResponse :datatype-) "ImageProcessing_Node/DetectResponse")
(setf (get ImageProcessing_Node::DetectResponse :definition-)
      "sensor_msgs/Image roi_image

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
string result
")



(provide :ImageProcessing_Node/Detect "a3926dcdd8f922bd0ad49b8c9d565283")


