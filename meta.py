#meta.py
from subprocess import Popen, PIPE

# describe the version of the current repository
describe = Popen(['git', 'describe', '--dirty','--always'],stdout=PIPE)
version = describe.communicate()[0].decode('utf-8').strip()

# most recent release
describe = Popen(['git','describe','--abbrev=0'],stdout=PIPE)
release = describe.communicate()[0].decode('utf-8').strip()

name = 'ESIP-envlib'
author = 'Aarif Shaikh'
copyright = 'NOAA - ESIP GSoC 2018'

