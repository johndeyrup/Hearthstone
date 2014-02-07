# Author: Mattis Haase 2014
#
# GNU GPL v3
#
# this script calculates the chance of drawing one
# of N cards of your deck of c cards

startAtCards = 26. # number of cards we start with

for cards in range(1,11): #for 1-10 cards in your deck
	results=[]
	probability = (startAtCards-cards)/startAtCards # so for 30 thats 29/30 - chance of drawing one card
	results.append(probability)
	for turn in range(1,10): # for turn 1-10
		probability = probability*(startAtCards-cards-turn)/(startAtCards-turn)
		results.append(probability)
	with open('results.txt', 'a') as f:
			f.write('\n    <tr>\n        <th>'+str(cards)+'\n\n')
			for item in results:
				f.write('        <th>'+str(round((1-item)*100, 1))+'\n')
		