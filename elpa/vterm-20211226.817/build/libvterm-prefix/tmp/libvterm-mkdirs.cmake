# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/Users/redstar/.personal.emacs.d/elpa/vterm-20211226.817/build/libvterm-prefix/src/libvterm"
  "/Users/redstar/.personal.emacs.d/elpa/vterm-20211226.817/build/libvterm-prefix/src/libvterm-build"
  "/Users/redstar/.personal.emacs.d/elpa/vterm-20211226.817/build/libvterm-prefix"
  "/Users/redstar/.personal.emacs.d/elpa/vterm-20211226.817/build/libvterm-prefix/tmp"
  "/Users/redstar/.personal.emacs.d/elpa/vterm-20211226.817/build/libvterm-prefix/src/libvterm-stamp"
  "/Users/redstar/.personal.emacs.d/elpa/vterm-20211226.817/build/libvterm-prefix/src"
  "/Users/redstar/.personal.emacs.d/elpa/vterm-20211226.817/build/libvterm-prefix/src/libvterm-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/Users/redstar/.personal.emacs.d/elpa/vterm-20211226.817/build/libvterm-prefix/src/libvterm-stamp/${subDir}")
endforeach()
