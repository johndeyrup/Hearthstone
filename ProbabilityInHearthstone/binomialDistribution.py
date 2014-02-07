# Author: Mattis Haase 2014
#
# GNU GPL v3
#
# This script calculates the chance of hitting a minion
# n times using a binomial random number generator
#

import numpy

for projectiles in [3,4,5,6,8,9]:
	for hits in range(1,projectiles+1):
		results=[]
		for minions in range(2, 6):
			binomial = numpy.random.binomial(projectiles, 1.0/minions, 100000)
			results.append(round(sum(binomial>hits-1)/1000., 1))
		with open('results.txt', 'a') as f:
			f.write('\n\nprojectiles '+str(projectiles)+'hits:'+str(hits)+'\n\n')
			for item in results:
				f.write(str(item)+'\n')
