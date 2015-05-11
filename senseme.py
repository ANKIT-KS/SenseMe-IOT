import subprocess
flag = 0
addrAnkit = '78:CB:AF:A7:62:36'
addrHC_05 = '98:D3:31:50:27:45'
while flag < 1:
	p = subprocess.Popen(['hcitool', 'scan'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, err = p.communicate()
	if addrAnkit in output:
		p = subprocess.Popen(["sh", "finalshell.sh"], stdout=subprocess.PIPE)
		flag = 2
	elif addrHC_05 in output:
		p = subprocess.Popen(["sh", "finalshell.sh"], stdout=subprocess.PIPE)
		flag = 2
	else:
		continue
#print output
#output["command_string"]
#q= subprocess.Popen([output, "json", "command_string"]
#a="1.mp3"
#p = subprocess.Popen(["vlc", "a"], stdout=subprocess.PIPE)
