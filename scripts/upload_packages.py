from subprocess import run
import os

packages = ['hpp-fcl', 'pinocchio', 'example-robot-data', 'crocoddyl', 'proxnlp', 'proxddp']

# collect all generated conda packages
out_packages = []
for package in packages:
  out_packages.append(run("conda build --output conda/recipes/" + package, capture_output=True, shell=True, text=True).stdout.split())

out_packages_flat = [item for sublist in out_packages for item in sublist]

# filter runtime packages and upload them to Anaconda dedicated channel
for package in out_packages_flat:
  if '-devel' not in package and '-split' not in package:
    os.system('anaconda -t ' + os.getenv('ANACONDA_API_TOKEN') + ' upload --user agm-ws-2023 ' + package)
  else:
    print('Skipping package ', package, '...')