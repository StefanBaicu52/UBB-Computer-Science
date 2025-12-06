cmake_minimum_required(VERSION 3.30)
project(dsa3)

set(CMAKE_CXX_STANDARD 20)

add_executable(dsa3 App.cpp Bag.cpp Bag.h BagIterator.cpp BagIterator.h ExtendedTest.h ExtendedTest.cpp ShortTest.h ShortTest.cpp)
