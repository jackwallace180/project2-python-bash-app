#!/bin/bash

for i in {0..100} ; do
	num_factor=`factor $i|wc -w`
	if [ $num_factor -eq 2 ]; then echo "dog"
	elif (! ((i % 3)) ) && (! ((i % 5)) ); then echo "cat and mouse"
	elif (! ((i % 3)) ); then echo "cat"
	elif (! ((i % 5)) ); then echo "mouse"
	else echo $i;
fi

done  	
