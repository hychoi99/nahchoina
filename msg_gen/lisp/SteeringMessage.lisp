; Auto-generated. Do not edit!


(cl:in-package nahchoina-msg)


;//! \htmlinclude SteeringMessage.msg.html

(cl:defclass <SteeringMessage> (roslisp-msg-protocol:ros-message)
  ((event
    :reader event
    :initarg :event
    :type cl:string
    :initform "")
   (linear
    :reader linear
    :initarg :linear
    :type cl:float
    :initform 0.0)
   (angular
    :reader angular
    :initarg :angular
    :type cl:float
    :initform 0.0))
)

(cl:defclass SteeringMessage (<SteeringMessage>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SteeringMessage>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SteeringMessage)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name nahchoina-msg:<SteeringMessage> is deprecated: use nahchoina-msg:SteeringMessage instead.")))

(cl:ensure-generic-function 'event-val :lambda-list '(m))
(cl:defmethod event-val ((m <SteeringMessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nahchoina-msg:event-val is deprecated.  Use nahchoina-msg:event instead.")
  (event m))

(cl:ensure-generic-function 'linear-val :lambda-list '(m))
(cl:defmethod linear-val ((m <SteeringMessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nahchoina-msg:linear-val is deprecated.  Use nahchoina-msg:linear instead.")
  (linear m))

(cl:ensure-generic-function 'angular-val :lambda-list '(m))
(cl:defmethod angular-val ((m <SteeringMessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nahchoina-msg:angular-val is deprecated.  Use nahchoina-msg:angular instead.")
  (angular m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SteeringMessage>) ostream)
  "Serializes a message object of type '<SteeringMessage>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'event))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'event))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'linear))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'angular))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SteeringMessage>) istream)
  "Deserializes a message object of type '<SteeringMessage>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'event) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'event) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'linear) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angular) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SteeringMessage>)))
  "Returns string type for a message object of type '<SteeringMessage>"
  "nahchoina/SteeringMessage")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SteeringMessage)))
  "Returns string type for a message object of type 'SteeringMessage"
  "nahchoina/SteeringMessage")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SteeringMessage>)))
  "Returns md5sum for a message object of type '<SteeringMessage>"
  "992808bfa7b78263265c8590a7a20a3c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SteeringMessage)))
  "Returns md5sum for a message object of type 'SteeringMessage"
  "992808bfa7b78263265c8590a7a20a3c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SteeringMessage>)))
  "Returns full string definition for message of type '<SteeringMessage>"
  (cl:format cl:nil "string event~%float32 linear~%float32 angular~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SteeringMessage)))
  "Returns full string definition for message of type 'SteeringMessage"
  (cl:format cl:nil "string event~%float32 linear~%float32 angular~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SteeringMessage>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'event))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SteeringMessage>))
  "Converts a ROS message object to a list"
  (cl:list 'SteeringMessage
    (cl:cons ':event (event msg))
    (cl:cons ':linear (linear msg))
    (cl:cons ':angular (angular msg))
))
