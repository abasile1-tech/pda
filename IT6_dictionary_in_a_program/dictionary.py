# Demonstrate the use of a dictionary in a program. 
# Include in your screenshot(s):
# *A dictionary in a program
# *A function (that you’ve created) that uses the dictionary
# *The result of the function running

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