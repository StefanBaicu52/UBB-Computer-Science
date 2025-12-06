# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\week11_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\week11_autogen.dir\\ParseCache.txt"
  "week11_autogen"
  )
endif()
