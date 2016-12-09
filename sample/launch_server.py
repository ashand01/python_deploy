#!/usr/bin/python

import boto3
import base64
import pprint

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')


def launch_test_instance():

   instances = ec2.create_instances(
      ImageId='ami-2051294a',
      InstanceType='t2.micro',
      MinCount=1,
      MaxCount=1,
      KeyName="load-ballancer-static-content",
      SecurityGroupIds=['launch-wizard-2'],
      UserData="""#!/usr/bin/python
import sys, os

def set_up_git():
   print('install git')
   os.system('yum -y install git')
   
   print('instally my reposoitory')
   os.system('git clone https://github.com/nic-instruction/python_deploy.git /tmp/python_deploy')

set_up_git()

sys.path.append('/tmp/python_deploy')

import app_install

app_install.install_apache()

"""

    )

   pprint.pprint(instances)

launch_test_instance()
