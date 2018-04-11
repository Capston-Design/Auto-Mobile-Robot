;; Auto-generated. Do not edit!


(when (boundp 'stack_image_node::Save)
  (if (not (find-package "STACK_IMAGE_NODE"))
    (make-package "STACK_IMAGE_NODE"))
  (shadow 'Save (find-package "STACK_IMAGE_NODE")))
(unless (find-package "STACK_IMAGE_NODE::SAVE")
  (make-package "STACK_IMAGE_NODE::SAVE"))
(unless (find-package "STACK_IMAGE_NODE::SAVEREQUEST")
  (make-package "STACK_IMAGE_NODE::SAVEREQUEST"))
(unless (find-package "STACK_IMAGE_NODE::SAVERESPONSE")
  (make-package "STACK_IMAGE_NODE::SAVERESPONSE"))

(in-package "ROS")





(defclass stack_image_node::SaveRequest
  :super ros::object
  :slots (_flag_message ))

(defmethod stack_image_node::SaveRequest
  (:init
   (&key
    ((:flag_message __flag_message) "")
    )
   (send-super :init)
   (setq _flag_message (string __flag_message))
   self)
  (:flag_message
   (&optional __flag_message)
   (if __flag_message (setq _flag_message __flag_message)) _flag_message)
  (:serialization-length
   ()
   (+
    ;; string _flag_message
    4 (length _flag_message)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _flag_message
       (write-long (length _flag_message) s) (princ _flag_message s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _flag_message
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _flag_message (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass stack_image_node::SaveResponse
  :super ros::object
  :slots (_result ))

(defmethod stack_image_node::SaveResponse
  (:init
   (&key
    ((:result __result) nil)
    )
   (send-super :init)
   (setq _result __result)
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; bool _result
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _result
       (if _result (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _result
     (setq _result (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass stack_image_node::Save
  :super ros::object
  :slots ())

(setf (get stack_image_node::Save :md5sum-) "2c75fafdcb7a71b1c42c8cdb584b2cf6")
(setf (get stack_image_node::Save :datatype-) "stack_image_node/Save")
(setf (get stack_image_node::Save :request) stack_image_node::SaveRequest)
(setf (get stack_image_node::Save :response) stack_image_node::SaveResponse)

(defmethod stack_image_node::SaveRequest
  (:response () (instance stack_image_node::SaveResponse :init)))

(setf (get stack_image_node::SaveRequest :md5sum-) "2c75fafdcb7a71b1c42c8cdb584b2cf6")
(setf (get stack_image_node::SaveRequest :datatype-) "stack_image_node/SaveRequest")
(setf (get stack_image_node::SaveRequest :definition-)
      "string flag_message
---
bool result
")

(setf (get stack_image_node::SaveResponse :md5sum-) "2c75fafdcb7a71b1c42c8cdb584b2cf6")
(setf (get stack_image_node::SaveResponse :datatype-) "stack_image_node/SaveResponse")
(setf (get stack_image_node::SaveResponse :definition-)
      "string flag_message
---
bool result
")



(provide :stack_image_node/Save "2c75fafdcb7a71b1c42c8cdb584b2cf6")


