# annoying process killer for windows.
# Feb 2016 - Adrian St. Onge
import os,psutil

#BLACKLIST
programs = {"Adobe Acrobat Update Service":"armsvc.exe","Windows 10 Upgrader":"GWX.exe", "Nero Updater":"NASvc.exe","Punkbuster":"PnkBstrA.exe","SynergyD":"synergyd.exe"}

# check to see if the current process matches one in our list of badies..
def check_process(exename):
	for appName, appExe in programs.items():
		if(appExe == exename):
			return True

# loop through running process
for p in psutil.process_iter():
	#get each processes PID and NAME (exe filename)
	proc_info = p.as_dict(attrs=['pid','name'])

	# is it on the blacklist?
	if check_process(proc_info['name']):
		print "Found match:",proc_info['name'],".. killing."
		try:
			p.kill()
		except:
			print "Error killing process.."
