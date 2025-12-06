cmake_minimum_required(VERSION 3.30)
project(week11)

set(CMAKE_CXX_STANDARD 20)

# Enable Qt features
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)

# Set Qt installation path (Windows - MinGW)
set(CMAKE_PREFIX_PATH "C:/Qt/6.9.0/mingw_64/lib/cmake")

# Find Qt modules
find_package(Qt6 REQUIRED COMPONENTS Core Gui Widgets)

# Add the executable and all source files
add_executable(week11
        main.cpp
        domain/dog.cpp
        repository/AdminRepository.cpp
        repository/UserRepository.cpp
        service/service.cpp
        ui/ui.cpp
        validation/validation.cpp
        exceptions/exceptions.cpp
        repository/AdoptionList.cpp
        GUI/GUI.cpp
)

# Link Qt libraries
target_link_libraries(week11 PRIVATE Qt6::Core Qt6::Gui Qt6::Widgets)
