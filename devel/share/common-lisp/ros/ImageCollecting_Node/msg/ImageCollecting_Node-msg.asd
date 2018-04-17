
(cl:in-package :asdf)

(defsystem "ImageCollecting_Node-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "ROI" :depends-on ("_package_ROI"))
    (:file "_package_ROI" :depends-on ("_package"))
  ))