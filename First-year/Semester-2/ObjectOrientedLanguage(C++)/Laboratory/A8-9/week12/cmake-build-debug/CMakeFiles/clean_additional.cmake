# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\week12_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\week12_autogen.dir\\ParseCache.txt"
  "week12_autogen"
  )
endif()
