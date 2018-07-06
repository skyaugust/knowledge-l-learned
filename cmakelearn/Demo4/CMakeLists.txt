cmake_minimum_required(VERSION 2.8)

project(Demo4)
set (DEMO_VERSION_MAJOR 1)
set (DEMO_VERSION_MINOR 0)
set (CMAKE_INCLUDE_CURRENT_DIR ON)
configure_file(
    "${PROJECT_SOURCE_DIR}/config.h.in"
    "${PROJECT_BINARY_DIR}/config.h"
)

option (USE_MYMATH
        "Use provided math implematation" ON)
if (USE_MYMATH)
    aux_source_directory(math MATH_DIR)
    include_directories(math)
endif(USE_MYMATH)

aux_source_directory(. DIR_SRCS)
add_executable(Demo ${DIR_SRCS} ${MATH_DIR})

