from __future__ import print_function
import Pyro4

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
            ns = False)

if __name__=="__main__":
    main()
    
