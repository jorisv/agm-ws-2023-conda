import os

print('=== OUT_PACKAGES:', os.getenv('OUT_PACKAGES'))
conda_packages = os.getenv('OUT_PACKAGES')
if conda_packages:
  for package in conda_packages.splitlines():
    if '-devel' not in package and '-split' not in package:
      os.system('anaconda -t ' + os.getenv('ANACONDA_API_TOKEN') + ' upload --user agm-ws-2023 ' + package)
    else:
      print('Skipping package ', package, '...')
else:
  print('No package to upload')