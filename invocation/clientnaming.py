import sys
import Pyro4

if sys.version_info<(3,0):
    input = raw_input

servant = Pyro4.Proxy("PYRONAME:example.servant")
servant.test()
message = input("Enter the message ").strip()
servant.sprint(message)




