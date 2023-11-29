#!/bin/sh

rm -rf build

mkdir build
cd build

cmake ${CMAKE_ARGS} .. \
      -DCMAKE_BUILD_TYPE=Release \
      -DPYTHON_EXECUTABLE=$PYTHON \
      -DBUILD_PYTHON_INTERFACE=ON \
      -DBUILD_EXAMPLES=OFF \
      -DBUILD_TESTING=OFF 

make -j${CPU_COUNT}
make install
