########################################################################
##
## CS 101
## Program 1
## Name Christian Barlow
## Email cbhnn@mail.umkc.edu
##
## PROBLEM : Write a program that calculates ingredients of Hogies
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##   Creation date: 09/03/17 Due date: 09/03/17
##
########################################################################
print('Hello, welcome to Hopper\'s Hoagies!\n')

#Take input of Hoagies sold
small_italian = int(input('How many small Italians were sold?\n'))
large_italian = int(input('How many large Italians were sold?\n'))

small_veg = int(input('How many small Vegetarians were sold?\n'))
large_veg = int(input('How many large Vegetarians were sold?\n'))

small_Tbird = int(input('How many small Tbirds were sold?\n'))
large_Tbird = int(input('How many large Tbirds were sold?\n'))

#Store ingredients for Hoagies

bread = ((small_italian * .5) + (large_italian * 1) + (small_veg * .5) + 
(large_veg * 1) + (small_Tbird * .5) + (large_Tbird * 1))

salami = (small_italian * .3) + (large_italian * .5)

vegetables  = ((small_italian * .2) + (large_italian * .5) + (small_veg * .5) + 
(large_veg * 1.2))

cheese = ((small_italian * 4) + (large_italian * 8) + (small_veg * 5) + 
(large_veg * 11) + (small_Tbird * 3) + (large_Tbird * 8))

turkey = ((small_Tbird * .4) + (large_Tbird * .9))

#output ingredients

print('You have used...\n ')
print('', bread, 'loaves of bread\n', salami, 'pounds of salami\n', vegetables,
      'pounds of vegetables\n', cheese, 'slices of cheese\n', turkey,
      'pounds of turkey\n')
print('Thanks for using the hoagie calculator! See you next time!')







