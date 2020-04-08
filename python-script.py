for i in range(1,100):
	prime = True
	for p in range(2,(i - 1)):
		if (i % p) == 0:
			prime = False
	if prime:
		print ('dog')
	elif (i % 3) == 0 and (i % 5) == 0:
		print ('cat and mouse')
	elif (i % 3) == 0 :
		print ('cat')
	elif (i % 5 ) == 0:
		print ('mouse')
	else:
		print(i)
