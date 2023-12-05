#!/bin/sh

rm -rf build

mkdir build
cd build

cmake ${CMAKE_ARGS} .. \
      -DCMAKE_BUILD_TYPE=Release \
      -DPYTHON_EXECUTABLE=$PYTHON \
      -DBUILD_PYTHON_INTERFACE=ON \
      -DGENERATE_PYTHON_STUBS=ON \
      -DBUILD_WITH_OPENMP_SUPPORT=OFF \
      -DBUILD_EXAMPLES=OFF \
      -DBUILD_TESTING=ON

make -j${CPU_COUNT}
make install
