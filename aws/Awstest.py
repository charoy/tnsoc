# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import boto
import time

__author__="charoy"
__date__ ="$17 juil. 2013 17:10:04$"

if __name__ == "__main__":
    print "Hello World"
    
s3=boto.connect_s3()
bucket = s3.create_bucket('boto-demo-%s' % int(time.time()))
key = bucket.new_key('mykey')
key.set_contents_from_string("Hello World!")
time.sleep(2)

print key.get_contents_as_string()
key.delete()
bucket.delete()
print "fini"

