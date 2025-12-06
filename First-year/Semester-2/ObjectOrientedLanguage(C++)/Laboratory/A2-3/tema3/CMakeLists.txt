cmake_minimum_required(VERSION 3.30)
project(tema3 C)

set(CMAKE_C_STANDARD 11)

add_executable(tema3 main.c dynamic_array.c repository.c service.c offer.c dynamic_array.h repository.h service.h offer.h)
