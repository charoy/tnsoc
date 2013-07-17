
__author__="charoy"
__date__ ="$17 juil. 2013 21:37:19$"

import boto.sqs
from boto.sqs.message import Message

conn = boto.sqs.connect_to_region("us-west-2")
q = conn.create_queue('myqueue')

m = Message()
m.set_body('This is my first message.')
status = q.write(m)

rs = q.get_messages()
print len(rs)
m = rs[0]
print m.get_body();

if __name__ == "__main__":
    print "Hello World";
