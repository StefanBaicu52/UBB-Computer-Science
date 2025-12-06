cmake_minimum_required(VERSION 3.25)
project(week12)

set(CMAKE_CXX_STANDARD 20)

# Enable Qt-specific auto processing
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)

# Manually specify Qt installation path (adjust as needed)
set(CMAKE_PREFIX_PATH "C:/Qt/6.9.0/mingw_64")

# Find Qt6 modules
find_package(Qt6 REQUIRED COMPONENTS Core Gui Widgets)

# Add your sources
add_executable(week12
        main.cpp
        domain/dog.cpp
        exceptions/exceptions.cpp
        repository/AdminRepository.cpp
        repository/UserRepository.cpp
        repository/AdoptionList.cpp
        service/service.cpp
        validation/validation.cpp
        GUI/mainwindow.cpp
        GUI/mainwindow.ui
        undo-redo/undo.cpp
        undo-redo/AdoptionModel.cpp
)

# Link Qt libraries
target_link_libraries(week12 PRIVATE Qt6::Core Qt6::Gui Qt6::Widgets)
