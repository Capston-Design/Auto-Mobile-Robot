;; Auto-generated. Do not edit!


(when (boundp 'ImageCollecting_Node::ROI)
  (if (not (find-package "IMAGECOLLECTING_NODE"))
    (make-package "IMAGECOLLECTING_NODE"))
  (shadow 'ROI (find-package "IMAGECOLLECTING_NODE")))
(unless (find-package "IMAGECOLLECTING_NODE::ROI")
  (make-package "IMAGECOLLECTING_NODE::ROI"))

(in-package "ROS")
;;//! \htmlinclude ROI.msg.html
(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))


(defclass ImageCollecting_Node::ROI
  :super ros::object
  :slots (_road_image _sign_image ))

(defmethod ImageCollecting_Node::ROI
  (:init
   (&key
    ((:road_image __road_image) (instance sensor_msgs::Image :init))
    ((:sign_image __sign_image) (instance sensor_msgs::Image :init))
    )
   (send-super :init)
   (setq _road_image __road_image)
   (setq _sign_image __sign_image)
   self)
  (:road_image
   (&rest __road_image)
   (if (keywordp (car __road_image))
       (send* _road_image __road_image)
     (progn
       (if __road_image (setq _road_image (car __road_image)))
       _road_image)))
  (:sign_image
   (&rest __sign_image)
   (if (keywordp (car __sign_image))
       (send* _sign_image __sign_image)
     (progn
       (if __sign_image (setq _sign_image (car __sign_image)))
       _sign_image)))
  (:serialization-length
   ()
   (+
    ;; sensor_msgs/Image _road_image
    (send _road_image :serialization-length)
    ;; sensor_msgs/Image _sign_image
    (send _sign_image :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; sensor_msgs/Image _road_image
       (send _road_image :serialize s)
     ;; sensor_msgs/Image _sign_image
       (send _sign_image :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; sensor_msgs/Image _road_image
     (send _road_image :deserialize buf ptr-) (incf ptr- (send _road_image :serialization-length))
   ;; sensor_msgs/Image _sign_image
     (send _sign_image :deserialize buf ptr-) (incf ptr- (send _sign_image :serialization-length))
   ;;
   self)
  )

(setf (get ImageCollecting_Node::ROI :md5sum-) "376bf59068ed68c4cf9a55425ed061fe")
(setf (get ImageCollecting_Node::ROI :datatype-) "ImageCollecting_Node/ROI")
(setf (get ImageCollecting_Node::ROI :definition-)
      "sensor_msgs/Image road_image
sensor_msgs/Image sign_image

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

")



(provide :ImageCollecting_Node/ROI "376bf59068ed68c4cf9a55425ed061fe")


