import sys
import Pyro4
import Pyro4.util

__author__="charoy"
__date__ ="$17 juil. 2013 15:35:00$"

class Servant(object):

    def sprint(self,message):
        print("Voici le message : {0}".format(message))

    def test(self):
        print("yopla")

def main():
    servant = Servant()
    Pyro4.Daemon.serveSimple(
            {
                servant: "example.servant"
            },
            ns = True) # will be registered in the naming service

if __name__ == "__main__":
    print "start server"
    main()
    
