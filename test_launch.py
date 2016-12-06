#!/usr/bin/python

import boto3
import base64
import pprint

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

def launch_test_instance():

   instances = ec2.create_instances(
      #use the image and spin up a box
      ImageId='ami-2051294a',
      InstanceType='t2.micro',
      MinCount=1,
      MaxCount=1,
      KeyName="load-ballancer-static-content",
      SecurityGroupIds=['launch-wizard-2'],
      UserData="""#!/usr/bin/python
import sys
sys.stdout = open('/tmp/file','w')
print 'test'
"""
    )

   pprint.pprint(instances)

launch_test_instance()
