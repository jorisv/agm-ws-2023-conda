from subprocess import run
import os

packages = ['hpp-fcl', 'pinocchio', 'example-robot-data', 'crocoddyl', 'proxnlp', 'proxddp', 'mim-solvers']
py_ver = os.getenv('PYTHON_VERSION')
numpy_ver = os.getenv('NUMPY_VERSION')

# collect all generated conda packages
out_packages = []
for package in packages:
  data = run(["conda", "build", "--py", py_ver, "--numpy", numpy_ver, "--output", "conda/recipes/" + package, "-c", "conda-forge"], capture_output=True, shell=False, text=True)
  print('Output:' + data.stdout)
  if(data.stderr):
    print('Error:' + data.stderr)
  out_packages.append(data.stdout.split())

out_packages_flat = [item for sublist in out_packages for item in sublist]

# filter runtime packages and upload them to Anaconda dedicated channel
for package in out_packages_flat:
  if '-devel' not in package and '-split' not in package:
    os.system('anaconda -t ' + os.getenv('ANACONDA_API_TOKEN') + ' upload --force --user agm-ws-2023 ' + package)
  else:
    print('Skipping package ', package, '...')