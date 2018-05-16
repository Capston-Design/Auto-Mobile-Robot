
(cl:in-package :asdf)

(defsystem "Control_Node-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Mission" :depends-on ("_package_Mission"))
    (:file "_package_Mission" :depends-on ("_package"))
  ))