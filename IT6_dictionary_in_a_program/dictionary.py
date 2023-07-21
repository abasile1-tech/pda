# Demonstrate the use of a dictionary in a program. 
# Include in your screenshot(s):
# *A dictionary in a program
# *A function (that you’ve created) that uses the dictionary
# *The result of the function running

# Dictionaries can be used to store key, value pairs. 
# They are useful for saving information that comes in pairs. 
# I have implemented a function that accesses a dictionary that 
# I made to get information about a particular type of dragon called the tatzelwurm.

tatzelwurm = {
	"other-names":["stollenwurm","stollwurm"],
	"region":"alps",
	"creature-type":"lizard-like",
	"face-style":"cat-like",
	"body-type":"serpent-like",
}

def get_element(dict, key):
	return dict[key]

print(f"The region of the tatzelwurm is {get_element(tatzelwurm, 'region')}")

# More Explanation
# I wrote the get_element function (the simplest implementation of a dictionary access). 
# It allows me to get the value of an item in the dictionary 
# simply be passing in the dictionary and the key. 
# The get_element function works by using square brackets to access 
# the value of the key that is passed in. A dictionary works by storing key, value pairs.