#!/bin/sh
FLAGS="-march=armv7-a -mfpu=vfpv3 -mfloat-abi=hard -mthumb"
export QMAKE_CXXFLAGS=$FLAGS
export QMAKE_LFLAGS=$FLAGS
export LDFLAGS=$FLAGS
export CXXFLAGS=$FLAGS
export CCFLAGS=$FLAGS
export CFLAGS=$FLAGS
export CPPFLAGS=$FLAGS
kiwix-build --target-platform armhf_static kiwix-tools --make-release -v
