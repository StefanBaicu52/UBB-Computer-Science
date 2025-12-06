cmake_minimum_required(VERSION 3.30)
project(untitled5)

set(CMAKE_CXX_STANDARD 20)

add_executable(untitled5
        main.cpp
        domain/dog.cpp
        dynamic_vector/dynamic_array.cpp
        repository/AdminRepository.cpp
        repository/UserRepository.cpp
        service/service.cpp
        ui/ui.cpp
        tests/tests.cpp
        validation/validation.cpp
)
