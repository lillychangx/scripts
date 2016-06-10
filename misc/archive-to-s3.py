
# Copyright 2013. Amazon Web Services, Inc. All Rights Reserved.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Import the SDK
import boto
import uuid

import sys, socket, os, re, glob, time
from time import strftime



# Instantiate a new client for Amazon Simple Storage Service (S3). With no
# parameters or configuration, the AWS SDK for Python (Boto) will look for
# access keys in these environment variables:
#
#    AWS_ACCESS_KEY_ID='...'
#    AWS_SECRET_ACCESS_KEY='...'
#
# For more information about this interface to Amazon S3, see:
# http://boto.readthedocs.org/en/latest/s3_tut.html

AWS_ACCESS_KEY_ID='AKIAJOR2ZRBZZNKUSPJA'
AWS_SECRET_ACCESS_KEY='oKxXSHfY2Uvp2z3QnYiEcwPSH6+0k5TzqP7d6Wq7'

file_name = "./sample_rba_scripts"
bucket_name = "vistara-wiki-backups"


s3 = boto.connect_s3()
bucket = s3.get_bucket(bucket_name)


from boto.s3.key import Key

k = Key(bucket)

fp = open(file_name, "r")

print ("uploaded file" + file_name + " to " + bucket_name)


k.key = file_name
k.set_contents_from_file(fp)

print ("finished pushing to S3")

sys.exit()
