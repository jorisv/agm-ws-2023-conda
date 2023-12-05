#!/bin/sh

rm -rf build

mkdir build
cd build

cmake ${CMAKE_ARGS} .. \
      -DCMAKE_BUILD_TYPE=Release \
      -DPYTHON_EXECUTABLE=$PYTHON \
      -DBUILD_PYTHON_INTERFACE=ON \
      -DBUILD_CROCODDYL_COMPAT=ON \
      -DGENERATE_PYTHON_STUBS=ON \
      -DBUILD_WITH_OPENMP_SUPPORT=OFF \
      -DBUILD_BENCHMARKS=OFF \
      -DBUILD_EXAMPLES=ON \
      -DBUILD_TESTING=OFF 

make -j${CPU_COUNT}
make install
