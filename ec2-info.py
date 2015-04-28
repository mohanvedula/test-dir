#!/usr/bin/env python

import boto
import boto.ec2

# connect to region and print the region name

ec2conn = boto.ec2.connect_to_region("us-west-2")

print '+-=-=-=-=-=-=-=-=-=-=-=-=-+'
print 'Region:', ec2conn

s3conn = boto.connect_s3()
print 's3 conn:', s3conn

# print a list of ec2 instances that are running
 
reservations = ec2conn.get_all_instances()
print '+-=-=-=-=-=-=-=-=-=-=-=-=-+'
print 'reservations:', reservations
 
