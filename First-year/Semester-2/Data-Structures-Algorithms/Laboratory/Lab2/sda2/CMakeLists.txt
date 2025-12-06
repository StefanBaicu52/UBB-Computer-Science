cmake_minimum_required(VERSION 3.30)
project(sda2)

set(CMAKE_CXX_STANDARD 20)

add_executable(sda2 main.cpp ExtendedTest.cpp ExtendedTest.h ShortTest.cpp ShortTest.h SMIterator.cpp SMIterator.h SortedMap.cpp SortedMap.h)

