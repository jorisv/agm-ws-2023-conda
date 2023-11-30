#!/bin/sh

upload_runtime_conda_packages() {
  # exclude packages having "-devel" or "-split" suffix
  FILES=`echo $OUT_PACKAGES | tr ' ' '\n' | grep -v "\-devel\|\-split"`
  for f in $FILES
  do
    echo "Uploading $f..."
    anaconda upload $f
  done
}