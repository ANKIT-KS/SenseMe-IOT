import subprocess
flag = 0
addrAnkit = 'your_device_bluetooth_address'
addrHC_05 = 'your_bluetooth_module address'
while flag < 1:
	p = subprocess.Popen(['hcitool', 'scan'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, err = p.communicate()
	if addrAnkit in output:
		p = subprocess.Popen(["sh", "request.sh"], stdout=subprocess.PIPE)
		flag = 2
	elif addrHC_05 in output:
		p = subprocess.Popen(["sh", "request.sh"], stdout=subprocess.PIPE)
		flag = 2
	else:
		continue
#print output
#output["command_string"]
#q= subprocess.Popen([output, "json", "command_string"]
#a="1.mp3"
#p = subprocess.Popen(["vlc", "a"], stdout=subprocess.PIPE)
