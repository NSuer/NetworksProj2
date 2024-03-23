cmake_minimum_required(VERSION 3.0)
project(ChatServer)

set(CMAKE_CXX_STANDARD 11) # Set C++ standard to C++11

# Add executable target
add_executable(ChatServer main.cpp)

# Find required libraries
find_package(Threads REQUIRED)

# Link the Threads library
target_link_libraries(ChatServer PRIVATE Threads::Threads)