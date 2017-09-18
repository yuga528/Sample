#!/usr/bin/python3
import boto
import boto.s3.connection
from boto.s3.key import Key
import math, os
from filechunkio import FileChunkIO
'''
connection = boto.s3.connection.S3Connection(
    aws_access_key_id='vedams',
    aws_secret_access_key='vedams123',
    port=8080,
    host='10.1.25.195',
    is_secure=False,
    validate_certs=False,
    calling_format=boto.s3.connection.OrdinaryCallingFormat()
    )
'''

connection = boto.s3.connection.S3Connection(
    aws_access_key_id='c78c3562e33f4c6bab61f7a7f6285544',
    aws_secret_access_key='465f1ff0ebf542d78d9d83253e582df4',
    port=8080,
    host='192.168.7.182',
    is_secure=False,
    validate_certs=False,
    calling_format=boto.s3.connection.OrdinaryCallingFormat()
    )

################
# For objects
################
#bucket = connection.create_bucket('panasonic123')
#b1 = connection.get_bucket('panasonic123')



################
# For buckets
################

#bucket = connection.create_bucket('pandam1')
b = connection.get_bucket('pratap')
b.set_acl('private')

k = Key(b)
k.key = 'testKey3'
k.set_contents_from_string("This is a string of S3 2222")

print (k.get_contents_as_string())


k1 = Key(b)
k1.key = 'testKey1'
k1.set_contents_from_string("This is a string of S3 2222")

print (k1.get_contents_as_string())


k2 = Key(b)
k2.key = 'testKey2'
k2.set_contents_from_string("This is a string of S3 2222")
print (k2.get_contents_as_string())

for key in b.list():
    print(key.name)
    print(key.size)    
    
