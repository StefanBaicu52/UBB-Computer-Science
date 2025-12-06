cmake_minimum_required(VERSION 3.30)
project(dsa4)

set(CMAKE_CXX_STANDARD 20)

add_executable(dsa4 app.cpp ExtendedTest.cpp ShortTest.cpp SMIterator.cpp SortedMap.cpp ExtendedTest.h ShortTest.h SMIterator.h SortedMap.h)
