; Auto-generated. Do not edit!


(cl:in-package nahchoina-srv)


;//! \htmlinclude CliffData-request.msg.html

(cl:defclass <CliffData-request> (roslisp-msg-protocol:ros-message)
  ((CliffState
    :reader CliffState
    :initarg :CliffState
    :type cl:fixnum
    :initform 0))
)

(cl:defclass CliffData-request (<CliffData-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CliffData-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CliffData-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name nahchoina-srv:<CliffData-request> is deprecated: use nahchoina-srv:CliffData-request instead.")))

(cl:ensure-generic-function 'CliffState-val :lambda-list '(m))
(cl:defmethod CliffState-val ((m <CliffData-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nahchoina-srv:CliffState-val is deprecated.  Use nahchoina-srv:CliffState instead.")
  (CliffState m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CliffData-request>) ostream)
  "Serializes a message object of type '<CliffData-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'CliffState)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CliffData-request>) istream)
  "Deserializes a message object of type '<CliffData-request>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'CliffState)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CliffData-request>)))
  "Returns string type for a service object of type '<CliffData-request>"
  "nahchoina/CliffDataRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CliffData-request)))
  "Returns string type for a service object of type 'CliffData-request"
  "nahchoina/CliffDataRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CliffData-request>)))
  "Returns md5sum for a message object of type '<CliffData-request>"
  "84b1231b3f295dc64c73346c9744e043")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CliffData-request)))
  "Returns md5sum for a message object of type 'CliffData-request"
  "84b1231b3f295dc64c73346c9744e043")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CliffData-request>)))
  "Returns full string definition for message of type '<CliffData-request>"
  (cl:format cl:nil "uint8 CliffState~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CliffData-request)))
  "Returns full string definition for message of type 'CliffData-request"
  (cl:format cl:nil "uint8 CliffState~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CliffData-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CliffData-request>))
  "Converts a ROS message object to a list"
  (cl:list 'CliffData-request
    (cl:cons ':CliffState (CliffState msg))
))
;//! \htmlinclude CliffData-response.msg.html

(cl:defclass <CliffData-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass CliffData-response (<CliffData-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CliffData-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CliffData-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name nahchoina-srv:<CliffData-response> is deprecated: use nahchoina-srv:CliffData-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <CliffData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nahchoina-srv:result-val is deprecated.  Use nahchoina-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CliffData-response>) ostream)
  "Serializes a message object of type '<CliffData-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CliffData-response>) istream)
  "Deserializes a message object of type '<CliffData-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CliffData-response>)))
  "Returns string type for a service object of type '<CliffData-response>"
  "nahchoina/CliffDataResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CliffData-response)))
  "Returns string type for a service object of type 'CliffData-response"
  "nahchoina/CliffDataResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CliffData-response>)))
  "Returns md5sum for a message object of type '<CliffData-response>"
  "84b1231b3f295dc64c73346c9744e043")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CliffData-response)))
  "Returns md5sum for a message object of type 'CliffData-response"
  "84b1231b3f295dc64c73346c9744e043")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CliffData-response>)))
  "Returns full string definition for message of type '<CliffData-response>"
  (cl:format cl:nil "bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CliffData-response)))
  "Returns full string definition for message of type 'CliffData-response"
  (cl:format cl:nil "bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CliffData-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CliffData-response>))
  "Converts a ROS message object to a list"
  (cl:list 'CliffData-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'CliffData)))
  'CliffData-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'CliffData)))
  'CliffData-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CliffData)))
  "Returns string type for a service object of type '<CliffData>"
  "nahchoina/CliffData")