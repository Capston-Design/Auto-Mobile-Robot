
(cl:in-package :asdf)

(defsystem "ImageProcessing_Node-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "DetectLane" :depends-on ("_package_DetectLane"))
    (:file "_package_DetectLane" :depends-on ("_package"))
  ))