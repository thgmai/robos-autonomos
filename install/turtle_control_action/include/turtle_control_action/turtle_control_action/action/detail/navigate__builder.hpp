// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from turtle_control_action:action/Navigate.idl
// generated code does not contain a copyright notice

#ifndef TURTLE_CONTROL_ACTION__ACTION__DETAIL__NAVIGATE__BUILDER_HPP_
#define TURTLE_CONTROL_ACTION__ACTION__DETAIL__NAVIGATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "turtle_control_action/action/detail/navigate__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace turtle_control_action
{

namespace action
{

namespace builder
{

class Init_Navigate_Goal_goal_y
{
public:
  explicit Init_Navigate_Goal_goal_y(::turtle_control_action::action::Navigate_Goal & msg)
  : msg_(msg)
  {}
  ::turtle_control_action::action::Navigate_Goal goal_y(::turtle_control_action::action::Navigate_Goal::_goal_y_type arg)
  {
    msg_.goal_y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtle_control_action::action::Navigate_Goal msg_;
};

class Init_Navigate_Goal_goal_x
{
public:
  Init_Navigate_Goal_goal_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Navigate_Goal_goal_y goal_x(::turtle_control_action::action::Navigate_Goal::_goal_x_type arg)
  {
    msg_.goal_x = std::move(arg);
    return Init_Navigate_Goal_goal_y(msg_);
  }

private:
  ::turtle_control_action::action::Navigate_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtle_control_action::action::Navigate_Goal>()
{
  return turtle_control_action::action::builder::Init_Navigate_Goal_goal_x();
}

}  // namespace turtle_control_action


namespace turtle_control_action
{

namespace action
{

namespace builder
{

class Init_Navigate_Result_current_y
{
public:
  explicit Init_Navigate_Result_current_y(::turtle_control_action::action::Navigate_Result & msg)
  : msg_(msg)
  {}
  ::turtle_control_action::action::Navigate_Result current_y(::turtle_control_action::action::Navigate_Result::_current_y_type arg)
  {
    msg_.current_y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtle_control_action::action::Navigate_Result msg_;
};

class Init_Navigate_Result_current_x
{
public:
  explicit Init_Navigate_Result_current_x(::turtle_control_action::action::Navigate_Result & msg)
  : msg_(msg)
  {}
  Init_Navigate_Result_current_y current_x(::turtle_control_action::action::Navigate_Result::_current_x_type arg)
  {
    msg_.current_x = std::move(arg);
    return Init_Navigate_Result_current_y(msg_);
  }

private:
  ::turtle_control_action::action::Navigate_Result msg_;
};

class Init_Navigate_Result_success
{
public:
  Init_Navigate_Result_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Navigate_Result_current_x success(::turtle_control_action::action::Navigate_Result::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_Navigate_Result_current_x(msg_);
  }

private:
  ::turtle_control_action::action::Navigate_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtle_control_action::action::Navigate_Result>()
{
  return turtle_control_action::action::builder::Init_Navigate_Result_success();
}

}  // namespace turtle_control_action


namespace turtle_control_action
{

namespace action
{

namespace builder
{

class Init_Navigate_Feedback_distance_to_goal
{
public:
  explicit Init_Navigate_Feedback_distance_to_goal(::turtle_control_action::action::Navigate_Feedback & msg)
  : msg_(msg)
  {}
  ::turtle_control_action::action::Navigate_Feedback distance_to_goal(::turtle_control_action::action::Navigate_Feedback::_distance_to_goal_type arg)
  {
    msg_.distance_to_goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtle_control_action::action::Navigate_Feedback msg_;
};

class Init_Navigate_Feedback_current_y
{
public:
  explicit Init_Navigate_Feedback_current_y(::turtle_control_action::action::Navigate_Feedback & msg)
  : msg_(msg)
  {}
  Init_Navigate_Feedback_distance_to_goal current_y(::turtle_control_action::action::Navigate_Feedback::_current_y_type arg)
  {
    msg_.current_y = std::move(arg);
    return Init_Navigate_Feedback_distance_to_goal(msg_);
  }

private:
  ::turtle_control_action::action::Navigate_Feedback msg_;
};

class Init_Navigate_Feedback_current_x
{
public:
  Init_Navigate_Feedback_current_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Navigate_Feedback_current_y current_x(::turtle_control_action::action::Navigate_Feedback::_current_x_type arg)
  {
    msg_.current_x = std::move(arg);
    return Init_Navigate_Feedback_current_y(msg_);
  }

private:
  ::turtle_control_action::action::Navigate_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtle_control_action::action::Navigate_Feedback>()
{
  return turtle_control_action::action::builder::Init_Navigate_Feedback_current_x();
}

}  // namespace turtle_control_action


namespace turtle_control_action
{

namespace action
{

namespace builder
{

class Init_Navigate_SendGoal_Request_goal
{
public:
  explicit Init_Navigate_SendGoal_Request_goal(::turtle_control_action::action::Navigate_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::turtle_control_action::action::Navigate_SendGoal_Request goal(::turtle_control_action::action::Navigate_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtle_control_action::action::Navigate_SendGoal_Request msg_;
};

class Init_Navigate_SendGoal_Request_goal_id
{
public:
  Init_Navigate_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Navigate_SendGoal_Request_goal goal_id(::turtle_control_action::action::Navigate_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Navigate_SendGoal_Request_goal(msg_);
  }

private:
  ::turtle_control_action::action::Navigate_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtle_control_action::action::Navigate_SendGoal_Request>()
{
  return turtle_control_action::action::builder::Init_Navigate_SendGoal_Request_goal_id();
}

}  // namespace turtle_control_action


namespace turtle_control_action
{

namespace action
{

namespace builder
{

class Init_Navigate_SendGoal_Response_stamp
{
public:
  explicit Init_Navigate_SendGoal_Response_stamp(::turtle_control_action::action::Navigate_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::turtle_control_action::action::Navigate_SendGoal_Response stamp(::turtle_control_action::action::Navigate_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtle_control_action::action::Navigate_SendGoal_Response msg_;
};

class Init_Navigate_SendGoal_Response_accepted
{
public:
  Init_Navigate_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Navigate_SendGoal_Response_stamp accepted(::turtle_control_action::action::Navigate_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_Navigate_SendGoal_Response_stamp(msg_);
  }

private:
  ::turtle_control_action::action::Navigate_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtle_control_action::action::Navigate_SendGoal_Response>()
{
  return turtle_control_action::action::builder::Init_Navigate_SendGoal_Response_accepted();
}

}  // namespace turtle_control_action


namespace turtle_control_action
{

namespace action
{

namespace builder
{

class Init_Navigate_GetResult_Request_goal_id
{
public:
  Init_Navigate_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::turtle_control_action::action::Navigate_GetResult_Request goal_id(::turtle_control_action::action::Navigate_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtle_control_action::action::Navigate_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtle_control_action::action::Navigate_GetResult_Request>()
{
  return turtle_control_action::action::builder::Init_Navigate_GetResult_Request_goal_id();
}

}  // namespace turtle_control_action


namespace turtle_control_action
{

namespace action
{

namespace builder
{

class Init_Navigate_GetResult_Response_result
{
public:
  explicit Init_Navigate_GetResult_Response_result(::turtle_control_action::action::Navigate_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::turtle_control_action::action::Navigate_GetResult_Response result(::turtle_control_action::action::Navigate_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtle_control_action::action::Navigate_GetResult_Response msg_;
};

class Init_Navigate_GetResult_Response_status
{
public:
  Init_Navigate_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Navigate_GetResult_Response_result status(::turtle_control_action::action::Navigate_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_Navigate_GetResult_Response_result(msg_);
  }

private:
  ::turtle_control_action::action::Navigate_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtle_control_action::action::Navigate_GetResult_Response>()
{
  return turtle_control_action::action::builder::Init_Navigate_GetResult_Response_status();
}

}  // namespace turtle_control_action


namespace turtle_control_action
{

namespace action
{

namespace builder
{

class Init_Navigate_FeedbackMessage_feedback
{
public:
  explicit Init_Navigate_FeedbackMessage_feedback(::turtle_control_action::action::Navigate_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::turtle_control_action::action::Navigate_FeedbackMessage feedback(::turtle_control_action::action::Navigate_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtle_control_action::action::Navigate_FeedbackMessage msg_;
};

class Init_Navigate_FeedbackMessage_goal_id
{
public:
  Init_Navigate_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Navigate_FeedbackMessage_feedback goal_id(::turtle_control_action::action::Navigate_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Navigate_FeedbackMessage_feedback(msg_);
  }

private:
  ::turtle_control_action::action::Navigate_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtle_control_action::action::Navigate_FeedbackMessage>()
{
  return turtle_control_action::action::builder::Init_Navigate_FeedbackMessage_goal_id();
}

}  // namespace turtle_control_action

#endif  // TURTLE_CONTROL_ACTION__ACTION__DETAIL__NAVIGATE__BUILDER_HPP_
