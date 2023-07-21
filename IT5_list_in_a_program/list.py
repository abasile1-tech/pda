# Demonstrate the use of a list in a program. Include in your screenshot(s):
# *A list in a program
# *A function (that you’ve created) that uses the list
# *The result of the function running
# Submit a comment explaining your understanding of:
# *The use of lists in programs
# *The code you’ve submitted


# Lists allow me to store objects in an ordered manner.
# I wrote a little program to keep track of team members
# I have written two functions. They ultimately allow me to 
# find the job title of a particular team member.
teams = [
	{
		"Accounts Team": 1,
		"Art Team": 2,
		"Facilities Team": 3
	},
	{
		"Rob": "banker",
		"Steve": "salesman",
		"Angela": "accountant",
		"Gwen": "banker"
	},
	{
		"Ariel": "art director",
		"Miriam": "painter"
	},
	{
		"Javier": "maintenance member",
		"David": "grounds crew member"
	}
]

def find_team_index(teams_list, team_name):
	index = False
	for key in teams_list[0].keys():
		if key == team_name:
			index = teams_list[0][key]
			break
	return index

def find_job_title(teams_list, team_name, name):
	index = find_team_index(teams_list, team_name)
	job_title = False
	if index:
		job_title = teams[index][name]
	return job_title

print(find_job_title(teams, "Facilities Team", "David"))

# further explanation of the code to meet the submission requirements:
# The find_job_title function that I wrote finds the job title from the 
# list by first calling the other function that I wrote which is called 
# find_team_index. The find_team_index function returns the index of the 
# team that the faculty member we are looking for is assigned to. 
# The teams list is a list of dictionary objects. 
# The first dictionary object in the list is a directory telling us
#  where in the list we can find the particular team we are looking for. 
# The other items in the last are dictionary objects  representing the 
# individual teams. Each team contains the employees that work on that 
# particular team along with their job titles stored as values. 
# The find_team_index function searches the first element in the list 
# to obtain the index for the team_name that is passed in. 
# The find_job_title function then takes that index and uses it 
# find the dictionary object in the list that represents the team 
# we are looking for. Then, inside of that dictionary item, it 
# finds the name of the worker and returns their job title.

# Basically, lists allow us to store items in an ordered way. 
# We can then access items in the list if we know the index 
# (or order) in which they exist in the list. We can index 
# into a list by using square brackets and putting the index 
# inside of the square brackets.