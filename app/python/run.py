import sys

def runapp(player_number=100):
        results = []
        for i in range(int(sys.argv[1]) + 1):
                prime = True
                for p in range(2, i):
                        if i % p == 0:
                                prime = False
                if (i == 1) or (i == 0):
                        prime = False
                        print(i)
                        results.append("{}".format(i))
                elif prime:
                        print("Dog")  
                        results.append("Dog")
                elif (i % 5 == 0) and (i % 3 == 0):
                        print("Cat and Mouse")
                        results.append("Cat and Mouse")
                elif i % 3 == 0:
                        print("Cat")
                        results.append("Cat")
                elif i % 5 == 0:
                        print("Mouse")
                        results.append("Mouse")
                else:
                        print(i)
                        results.append("{}".format(i))
                i = i+1
runapp()
