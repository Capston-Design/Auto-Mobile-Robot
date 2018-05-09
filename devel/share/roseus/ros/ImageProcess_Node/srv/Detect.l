;; Auto-generated. Do not edit!


(when (boundp 'ImageProcess_Node::Detect)
  (if (not (find-package "IMAGEPROCESS_NODE"))
    (make-package "IMAGEPROCESS_NODE"))
  (shadow 'Detect (find-package "IMAGEPROCESS_NODE")))
(unless (find-package "IMAGEPROCESS_NODE::DETECT")
  (make-package "IMAGEPROCESS_NODE::DETECT"))
(unless (find-package "IMAGEPROCESS_NODE::DETECTREQUEST")
  (make-package "IMAGEPROCESS_NODE::DETECTREQUEST"))
(unless (find-package "IMAGEPROCESS_NODE::DETECTRESPONSE")
  (make-package "IMAGEPROCESS_NODE::DETECTRESPONSE"))

(in-package "ROS")





(defclass ImageProcess_Node::DetectRequest
  :super ros::object
  :slots (_roi_image ))

(defmethod ImageProcess_Node::DetectRequest
  (:init
   (&key
    ((:roi_image __roi_image) 0.0)
    )
   (send-super :init)
   (setq _roi_image (float __roi_image))
   self)
  (:roi_image
   (&optional __roi_image)
   (if __roi_image (setq _roi_image __roi_image)) _roi_image)
  (:serialization-length
   ()
   (+
    ;; float32 _roi_image
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _roi_image
       (sys::poke _roi_image (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _roi_image
     (setq _roi_image (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass ImageProcess_Node::DetectResponse
  :super ros::object
  :slots (_result ))

(defmethod ImageProcess_Node::DetectResponse
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

(defclass ImageProcess_Node::Detect
  :super ros::object
  :slots ())

(setf (get ImageProcess_Node::Detect :md5sum-) "c5cdbbf937a2b7afdb40f16147414b23")
(setf (get ImageProcess_Node::Detect :datatype-) "ImageProcess_Node/Detect")
(setf (get ImageProcess_Node::Detect :request) ImageProcess_Node::DetectRequest)
(setf (get ImageProcess_Node::Detect :response) ImageProcess_Node::DetectResponse)

(defmethod ImageProcess_Node::DetectRequest
  (:response () (instance ImageProcess_Node::DetectResponse :init)))

(setf (get ImageProcess_Node::DetectRequest :md5sum-) "c5cdbbf937a2b7afdb40f16147414b23")
(setf (get ImageProcess_Node::DetectRequest :datatype-) "ImageProcess_Node/DetectRequest")
(setf (get ImageProcess_Node::DetectRequest :definition-)
      "float32 roi_image
---
string result
")

(setf (get ImageProcess_Node::DetectResponse :md5sum-) "c5cdbbf937a2b7afdb40f16147414b23")
(setf (get ImageProcess_Node::DetectResponse :datatype-) "ImageProcess_Node/DetectResponse")
(setf (get ImageProcess_Node::DetectResponse :definition-)
      "float32 roi_image
---
string result
")



(provide :ImageProcess_Node/Detect "c5cdbbf937a2b7afdb40f16147414b23")


