// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from turtle_control_action:action/Navigate.idl
// generated code does not contain a copyright notice

#ifndef TURTLE_CONTROL_ACTION__ACTION__DETAIL__NAVIGATE__STRUCT_H_
#define TURTLE_CONTROL_ACTION__ACTION__DETAIL__NAVIGATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in action/Navigate in the package turtle_control_action.
typedef struct turtle_control_action__action__Navigate_Goal
{
  float goal_x;
  float goal_y;
} turtle_control_action__action__Navigate_Goal;

// Struct for a sequence of turtle_control_action__action__Navigate_Goal.
typedef struct turtle_control_action__action__Navigate_Goal__Sequence
{
  turtle_control_action__action__Navigate_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtle_control_action__action__Navigate_Goal__Sequence;


// Constants defined in the message

/// Struct defined in action/Navigate in the package turtle_control_action.
typedef struct turtle_control_action__action__Navigate_Result
{
  bool success;
  float current_x;
  float current_y;
} turtle_control_action__action__Navigate_Result;

// Struct for a sequence of turtle_control_action__action__Navigate_Result.
typedef struct turtle_control_action__action__Navigate_Result__Sequence
{
  turtle_control_action__action__Navigate_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtle_control_action__action__Navigate_Result__Sequence;


// Constants defined in the message

/// Struct defined in action/Navigate in the package turtle_control_action.
typedef struct turtle_control_action__action__Navigate_Feedback
{
  float current_x;
  float current_y;
  float distance_to_goal;
} turtle_control_action__action__Navigate_Feedback;

// Struct for a sequence of turtle_control_action__action__Navigate_Feedback.
typedef struct turtle_control_action__action__Navigate_Feedback__Sequence
{
  turtle_control_action__action__Navigate_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtle_control_action__action__Navigate_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "turtle_control_action/action/detail/navigate__struct.h"

/// Struct defined in action/Navigate in the package turtle_control_action.
typedef struct turtle_control_action__action__Navigate_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  turtle_control_action__action__Navigate_Goal goal;
} turtle_control_action__action__Navigate_SendGoal_Request;

// Struct for a sequence of turtle_control_action__action__Navigate_SendGoal_Request.
typedef struct turtle_control_action__action__Navigate_SendGoal_Request__Sequence
{
  turtle_control_action__action__Navigate_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtle_control_action__action__Navigate_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/Navigate in the package turtle_control_action.
typedef struct turtle_control_action__action__Navigate_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} turtle_control_action__action__Navigate_SendGoal_Response;

// Struct for a sequence of turtle_control_action__action__Navigate_SendGoal_Response.
typedef struct turtle_control_action__action__Navigate_SendGoal_Response__Sequence
{
  turtle_control_action__action__Navigate_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtle_control_action__action__Navigate_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/Navigate in the package turtle_control_action.
typedef struct turtle_control_action__action__Navigate_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} turtle_control_action__action__Navigate_GetResult_Request;

// Struct for a sequence of turtle_control_action__action__Navigate_GetResult_Request.
typedef struct turtle_control_action__action__Navigate_GetResult_Request__Sequence
{
  turtle_control_action__action__Navigate_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtle_control_action__action__Navigate_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "turtle_control_action/action/detail/navigate__struct.h"

/// Struct defined in action/Navigate in the package turtle_control_action.
typedef struct turtle_control_action__action__Navigate_GetResult_Response
{
  int8_t status;
  turtle_control_action__action__Navigate_Result result;
} turtle_control_action__action__Navigate_GetResult_Response;

// Struct for a sequence of turtle_control_action__action__Navigate_GetResult_Response.
typedef struct turtle_control_action__action__Navigate_GetResult_Response__Sequence
{
  turtle_control_action__action__Navigate_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtle_control_action__action__Navigate_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "turtle_control_action/action/detail/navigate__struct.h"

/// Struct defined in action/Navigate in the package turtle_control_action.
typedef struct turtle_control_action__action__Navigate_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  turtle_control_action__action__Navigate_Feedback feedback;
} turtle_control_action__action__Navigate_FeedbackMessage;

// Struct for a sequence of turtle_control_action__action__Navigate_FeedbackMessage.
typedef struct turtle_control_action__action__Navigate_FeedbackMessage__Sequence
{
  turtle_control_action__action__Navigate_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtle_control_action__action__Navigate_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TURTLE_CONTROL_ACTION__ACTION__DETAIL__NAVIGATE__STRUCT_H_
