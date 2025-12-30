// generated from rosidl_generator_c/resource/rosidl_generator_c__visibility_control.h.in
// generated code does not contain a copyright notice

#ifndef TURTLE_CONTROL_ACTION__MSG__ROSIDL_GENERATOR_C__VISIBILITY_CONTROL_H_
#define TURTLE_CONTROL_ACTION__MSG__ROSIDL_GENERATOR_C__VISIBILITY_CONTROL_H_

#ifdef __cplusplus
extern "C"
{
#endif

// This logic was borrowed (then namespaced) from the examples on the gcc wiki:
//     https://gcc.gnu.org/wiki/Visibility

#if defined _WIN32 || defined __CYGWIN__
  #ifdef __GNUC__
    #define ROSIDL_GENERATOR_C_EXPORT_turtle_control_action __attribute__ ((dllexport))
    #define ROSIDL_GENERATOR_C_IMPORT_turtle_control_action __attribute__ ((dllimport))
  #else
    #define ROSIDL_GENERATOR_C_EXPORT_turtle_control_action __declspec(dllexport)
    #define ROSIDL_GENERATOR_C_IMPORT_turtle_control_action __declspec(dllimport)
  #endif
  #ifdef ROSIDL_GENERATOR_C_BUILDING_DLL_turtle_control_action
    #define ROSIDL_GENERATOR_C_PUBLIC_turtle_control_action ROSIDL_GENERATOR_C_EXPORT_turtle_control_action
  #else
    #define ROSIDL_GENERATOR_C_PUBLIC_turtle_control_action ROSIDL_GENERATOR_C_IMPORT_turtle_control_action
  #endif
#else
  #define ROSIDL_GENERATOR_C_EXPORT_turtle_control_action __attribute__ ((visibility("default")))
  #define ROSIDL_GENERATOR_C_IMPORT_turtle_control_action
  #if __GNUC__ >= 4
    #define ROSIDL_GENERATOR_C_PUBLIC_turtle_control_action __attribute__ ((visibility("default")))
  #else
    #define ROSIDL_GENERATOR_C_PUBLIC_turtle_control_action
  #endif
#endif

#ifdef __cplusplus
}
#endif

#endif  // TURTLE_CONTROL_ACTION__MSG__ROSIDL_GENERATOR_C__VISIBILITY_CONTROL_H_
