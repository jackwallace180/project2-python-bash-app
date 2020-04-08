import sys

def runapp(player_number=100):  #definine the runapp function which operates on the numbers
	results = [] #store results in a list
	for i in range(int(sys.argv[1]) + 1): #create a range from the input number
		prime = True
		for p in range(2, i): #calculate whether or not it is a prime
			if i % p == 0:
				prime = False
		if (i == 1) or (i == 0): #1 and 0 arent primes 
			prime = False
			print(i)
			print(", ")
			results.append("{}".format(i))
			results.append(", ")
		elif (i == 3):  #3 is the only case of dog and cat
			print("Dog and Cat, ")
			results.append("Dog and Cat ,")
		elif (i == 5): #5 the only case of dog and mouse
			print("Dog and Mouse, ")
			results.append("Dog and Mouse, ")
		elif prime:  # print dog when prime
			print("Dog, ")  
			results.append("Dog, ")
		elif (i % 5 == 0) and (i % 3 == 0): #prime cat and mouse when divisible by 3 and 5
			print("Cat and Mouse, ")
			results.append("Cat and Mouse, ")
		elif i % 3 == 0: #print cat when divisinle by 3
			print("Cat, ")
			results.append("Cat, ")
		elif i % 5 == 0: #print mosue when divisible by 5
			print("Mouse, ")
			results.append("Mouse, ")
		else:  #if not print the number
			print(i) 
			print(", ")
			results.append("{}".format(i))
			results.append(", ")
		i = i+1
runapp() #run the function
