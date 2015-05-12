; Auto-generated. Do not edit!


(cl:in-package nahchoina-srv)


;//! \htmlinclude BumpData-request.msg.html

(cl:defclass <BumpData-request> (roslisp-msg-protocol:ros-message)
  ((bumpers
    :reader bumpers
    :initarg :bumpers
    :type cl:fixnum
    :initform 0)
   (cliff
    :reader cliff
    :initarg :cliff
    :type cl:fixnum
    :initform 0)
   (state
    :reader state
    :initarg :state
    :type cl:fixnum
    :initform 0))
)

(cl:defclass BumpData-request (<BumpData-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BumpData-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BumpData-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name nahchoina-srv:<BumpData-request> is deprecated: use nahchoina-srv:BumpData-request instead.")))

(cl:ensure-generic-function 'bumpers-val :lambda-list '(m))
(cl:defmethod bumpers-val ((m <BumpData-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nahchoina-srv:bumpers-val is deprecated.  Use nahchoina-srv:bumpers instead.")
  (bumpers m))

(cl:ensure-generic-function 'cliff-val :lambda-list '(m))
(cl:defmethod cliff-val ((m <BumpData-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nahchoina-srv:cliff-val is deprecated.  Use nahchoina-srv:cliff instead.")
  (cliff m))

(cl:ensure-generic-function 'state-val :lambda-list '(m))
(cl:defmethod state-val ((m <BumpData-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nahchoina-srv:state-val is deprecated.  Use nahchoina-srv:state instead.")
  (state m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BumpData-request>) ostream)
  "Serializes a message object of type '<BumpData-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'bumpers)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'cliff)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'state)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BumpData-request>) istream)
  "Deserializes a message object of type '<BumpData-request>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'bumpers)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'cliff)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'state)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BumpData-request>)))
  "Returns string type for a service object of type '<BumpData-request>"
  "nahchoina/BumpDataRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BumpData-request)))
  "Returns string type for a service object of type 'BumpData-request"
  "nahchoina/BumpDataRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BumpData-request>)))
  "Returns md5sum for a message object of type '<BumpData-request>"
  "7e42fd26a3c414dea20231fe4e1c87e2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BumpData-request)))
  "Returns md5sum for a message object of type 'BumpData-request"
  "7e42fd26a3c414dea20231fe4e1c87e2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BumpData-request>)))
  "Returns full string definition for message of type '<BumpData-request>"
  (cl:format cl:nil "uint8 bumpers~%uint8 cliff~%uint8 state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BumpData-request)))
  "Returns full string definition for message of type 'BumpData-request"
  (cl:format cl:nil "uint8 bumpers~%uint8 cliff~%uint8 state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BumpData-request>))
  (cl:+ 0
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BumpData-request>))
  "Converts a ROS message object to a list"
  (cl:list 'BumpData-request
    (cl:cons ':bumpers (bumpers msg))
    (cl:cons ':cliff (cliff msg))
    (cl:cons ':state (state msg))
))
;//! \htmlinclude BumpData-response.msg.html

(cl:defclass <BumpData-response> (roslisp-msg-protocol:ros-message)
  ((bumper_left
    :reader bumper_left
    :initarg :bumper_left
    :type cl:boolean
    :initform cl:nil)
   (bumper_mid
    :reader bumper_mid
    :initarg :bumper_mid
    :type cl:boolean
    :initform cl:nil)
   (bumper_right
    :reader bumper_right
    :initarg :bumper_right
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass BumpData-response (<BumpData-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BumpData-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BumpData-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name nahchoina-srv:<BumpData-response> is deprecated: use nahchoina-srv:BumpData-response instead.")))

(cl:ensure-generic-function 'bumper_left-val :lambda-list '(m))
(cl:defmethod bumper_left-val ((m <BumpData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nahchoina-srv:bumper_left-val is deprecated.  Use nahchoina-srv:bumper_left instead.")
  (bumper_left m))

(cl:ensure-generic-function 'bumper_mid-val :lambda-list '(m))
(cl:defmethod bumper_mid-val ((m <BumpData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nahchoina-srv:bumper_mid-val is deprecated.  Use nahchoina-srv:bumper_mid instead.")
  (bumper_mid m))

(cl:ensure-generic-function 'bumper_right-val :lambda-list '(m))
(cl:defmethod bumper_right-val ((m <BumpData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nahchoina-srv:bumper_right-val is deprecated.  Use nahchoina-srv:bumper_right instead.")
  (bumper_right m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BumpData-response>) ostream)
  "Serializes a message object of type '<BumpData-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'bumper_left) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'bumper_mid) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'bumper_right) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BumpData-response>) istream)
  "Deserializes a message object of type '<BumpData-response>"
    (cl:setf (cl:slot-value msg 'bumper_left) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'bumper_mid) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'bumper_right) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BumpData-response>)))
  "Returns string type for a service object of type '<BumpData-response>"
  "nahchoina/BumpDataResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BumpData-response)))
  "Returns string type for a service object of type 'BumpData-response"
  "nahchoina/BumpDataResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BumpData-response>)))
  "Returns md5sum for a message object of type '<BumpData-response>"
  "7e42fd26a3c414dea20231fe4e1c87e2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BumpData-response)))
  "Returns md5sum for a message object of type 'BumpData-response"
  "7e42fd26a3c414dea20231fe4e1c87e2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BumpData-response>)))
  "Returns full string definition for message of type '<BumpData-response>"
  (cl:format cl:nil "bool bumper_left~%bool bumper_mid~%bool bumper_right~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BumpData-response)))
  "Returns full string definition for message of type 'BumpData-response"
  (cl:format cl:nil "bool bumper_left~%bool bumper_mid~%bool bumper_right~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BumpData-response>))
  (cl:+ 0
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BumpData-response>))
  "Converts a ROS message object to a list"
  (cl:list 'BumpData-response
    (cl:cons ':bumper_left (bumper_left msg))
    (cl:cons ':bumper_mid (bumper_mid msg))
    (cl:cons ':bumper_right (bumper_right msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'BumpData)))
  'BumpData-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'BumpData)))
  'BumpData-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BumpData)))
  "Returns string type for a service object of type '<BumpData>"
  "nahchoina/BumpData")