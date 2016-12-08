#!/usr/bin/python
import sys, os


def set_up_git():
   print('install git')
   os.system('yum -y install git')
   
   print('instally my reposoitory')
   os.system('git clone https://github.com/nic-instruction/python_deploy.git /tmp/python_deploy')

set_up_git()

#os.chdir('python_deploy')
sys.path.append('/tmp/python_deploy')

import app_install

app_install.install_apache()
