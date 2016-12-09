#!/usr/bin/python

import boto3
import base64
import pprint

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

amazon_image = 'ami-2051294a'
amazon_instance = 't2.micro'
amazon_pem_key = 'load-ballancer-static-content'
firewall_profile = 'launch-wizard-2'

print(amazon_image)
print(amazon_instance)
print(amazon_pem_key)


#UserData = """#!/user/bin/python
#import sys
#sys.stdout = open('/tmp/file', 'w')
#print 'test'
#"""

def launch_test_instance():

   instances = ec2.create_instances(
      ImageId = amazon_image,
      InstanceType = amazon_instance,
      MinCount=1,
      MaxCount=1,
      KeyName = amazon_pem_key,
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
   #response = client.describe_instances(instances)
   #pprint.pprint(response)

launch_test_instance()

