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