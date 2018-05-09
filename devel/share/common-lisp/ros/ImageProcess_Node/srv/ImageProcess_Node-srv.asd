
(cl:in-package :asdf)

(defsystem "ImageProcess_Node-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Detect" :depends-on ("_package_Detect"))
    (:file "_package_Detect" :depends-on ("_package"))
  ))