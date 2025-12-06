cmake_minimum_required(VERSION 3.30)
project(untitled5)

set(CMAKE_CXX_STANDARD 20)


# Add the executable and all source files
add_executable(untitled5
        main.cpp
        domain/dog.cpp
        repository/AdminRepository.cpp
        repository/UserRepository.cpp
        service/service.cpp
        ui/ui.cpp
        validation/validation.cpp
        exceptions/exceptions.cpp
        repository/AdoptionList.cpp

)

