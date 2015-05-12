
(cl:in-package :asdf)

(defsystem "nahchoina-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "BumpData" :depends-on ("_package_BumpData"))
    (:file "_package_BumpData" :depends-on ("_package"))
    (:file "CliffData" :depends-on ("_package_CliffData"))
    (:file "_package_CliffData" :depends-on ("_package"))
  ))