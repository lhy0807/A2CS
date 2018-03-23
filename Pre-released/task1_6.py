def deterRole(salary):
	role = ''
	if (salary < 50): role = 'Manager'
	elif (50 < salary <= 70): role = 'Lead Developer'
	elif (70 < salary < 90): role = 'Consultant'
	else: role = 'Project Manager'
	return role