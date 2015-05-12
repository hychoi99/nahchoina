
(cl:in-package :asdf)

(defsystem "nahchoina-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "SteeringMessage" :depends-on ("_package_SteeringMessage"))
    (:file "_package_SteeringMessage" :depends-on ("_package"))
  ))