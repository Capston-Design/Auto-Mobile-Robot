
(cl:in-package :asdf)

(defsystem "ImageProcessing_Node-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "Detect" :depends-on ("_package_Detect"))
    (:file "_package_Detect" :depends-on ("_package"))
  ))