cmake_minimum_required(VERSION 2.8)

project(Demo3)

aux_source_directory(. DIR_SRCS)
aux_source_directory(math MATH_DIR)

include_directories(math)


add_executable(Demo ${DIR_SRCS} ${MATH_DIR})

