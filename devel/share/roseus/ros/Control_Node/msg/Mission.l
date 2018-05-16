;; Auto-generated. Do not edit!


(when (boundp 'Control_Node::Mission)
  (if (not (find-package "CONTROL_NODE"))
    (make-package "CONTROL_NODE"))
  (shadow 'Mission (find-package "CONTROL_NODE")))
(unless (find-package "CONTROL_NODE::MISSION")
  (make-package "CONTROL_NODE::MISSION"))

(in-package "ROS")
;;//! \htmlinclude Mission.msg.html


(defclass Control_Node::Mission
  :super ros::object
  :slots (_traffic _parking _crossbar _tunnel ))

(defmethod Control_Node::Mission
  (:init
   (&key
    ((:traffic __traffic) nil)
    ((:parking __parking) nil)
    ((:crossbar __crossbar) nil)
    ((:tunnel __tunnel) nil)
    )
   (send-super :init)
   (setq _traffic __traffic)
   (setq _parking __parking)
   (setq _crossbar __crossbar)
   (setq _tunnel __tunnel)
   self)
  (:traffic
   (&optional __traffic)
   (if __traffic (setq _traffic __traffic)) _traffic)
  (:parking
   (&optional __parking)
   (if __parking (setq _parking __parking)) _parking)
  (:crossbar
   (&optional __crossbar)
   (if __crossbar (setq _crossbar __crossbar)) _crossbar)
  (:tunnel
   (&optional __tunnel)
   (if __tunnel (setq _tunnel __tunnel)) _tunnel)
  (:serialization-length
   ()
   (+
    ;; bool _traffic
    1
    ;; bool _parking
    1
    ;; bool _crossbar
    1
    ;; bool _tunnel
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _traffic
       (if _traffic (write-byte -1 s) (write-byte 0 s))
     ;; bool _parking
       (if _parking (write-byte -1 s) (write-byte 0 s))
     ;; bool _crossbar
       (if _crossbar (write-byte -1 s) (write-byte 0 s))
     ;; bool _tunnel
       (if _tunnel (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _traffic
     (setq _traffic (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _parking
     (setq _parking (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _crossbar
     (setq _crossbar (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _tunnel
     (setq _tunnel (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get Control_Node::Mission :md5sum-) "132b675c11a085c243deb3519223ef08")
(setf (get Control_Node::Mission :datatype-) "Control_Node/Mission")
(setf (get Control_Node::Mission :definition-)
      "bool traffic
bool parking
bool crossbar
bool tunnel
")



(provide :Control_Node/Mission "132b675c11a085c243deb3519223ef08")


