# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "C:/Users/mmoran/Projects/Git-Repos/MechTabby/myBlink/build/_deps/picotool-src"
  "C:/Users/mmoran/Projects/Git-Repos/MechTabby/myBlink/build/_deps/picotool-build"
  "C:/Users/mmoran/Projects/Git-Repos/MechTabby/myBlink/build/_deps/picotool-subbuild/picotool-populate-prefix"
  "C:/Users/mmoran/Projects/Git-Repos/MechTabby/myBlink/build/_deps/picotool-subbuild/picotool-populate-prefix/tmp"
  "C:/Users/mmoran/Projects/Git-Repos/MechTabby/myBlink/build/_deps/picotool-subbuild/picotool-populate-prefix/src/picotool-populate-stamp"
  "C:/Users/mmoran/Projects/Git-Repos/MechTabby/myBlink/build/_deps/picotool-subbuild/picotool-populate-prefix/src"
  "C:/Users/mmoran/Projects/Git-Repos/MechTabby/myBlink/build/_deps/picotool-subbuild/picotool-populate-prefix/src/picotool-populate-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "C:/Users/mmoran/Projects/Git-Repos/MechTabby/myBlink/build/_deps/picotool-subbuild/picotool-populate-prefix/src/picotool-populate-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "C:/Users/mmoran/Projects/Git-Repos/MechTabby/myBlink/build/_deps/picotool-subbuild/picotool-populate-prefix/src/picotool-populate-stamp${cfgdir}") # cfgdir has leading slash
endif()
