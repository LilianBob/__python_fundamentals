# write a single function, randInt() that takes up to 2 arguments.
# If no arguments are provided, the function should return a random integer between 0 and 100.
# If only a max number is provided, the function should return a random integer between 0 and the max number.
# If only a min number is provided, the function should return a random integer between the min number and 100
# If both a min and max number are provided, the function should return a random integer between those 2 values.

import random
def randInt(min =0, max =100 ):
    num_range = max-min
    num = round(random.random()* num_range + min)
    return num
print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50))
print(randInt(min=50, max=500))

#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
#NB the output depends on the arguments we pass to the function when we call it and is not suggested by the arguments passed to parameters when defining the function; 
# this represent the default