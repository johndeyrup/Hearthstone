# Author: Mattis Haase 2014
#
# GNU GPL v3
#
# This script calculates the chance of Nat Pagle Carddraw
# What is the chance of at least n draws if Pagle stays alive t turns
#

import numpy

results=[]

for turns in range(1,11):
	results.append([])
	binomial = numpy.random.binomial(turns, 0.5, 100000)
	for cards in range(0,turns):
		results[turns-1].append(round(100*sum(binomial>cards)/100000., 1))	
with open('results.txt', 'a') as f:
	for i in range(0,10):
		f.write('<tr>\n    <th>'+str(i+1)+' cards\n\n')
		for j in range(0,10):
			if i < len(results[j]):
				print '['+str(j)+']['+str(i)+']'
				f.write('\n    <th>'+str(results[j][i]))
			else:
				f.write('\n    <th>--')