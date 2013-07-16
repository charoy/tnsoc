import sys
import Pyro4

if sys.version_info<(3,0):
    input = raw_input

uri = input("Enter the uri of the servant: ").strip()
servant = Pyro4.Proxy(uri)
servant.test()
message = input("Enter the message ").strip()
servant.sprint(message)



