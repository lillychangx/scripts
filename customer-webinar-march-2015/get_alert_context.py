import os, sys, time, commands, subprocess

# If the script is executed as an RBA on a alert on a monitor that monitors for a running linux process - mydaemon
# python /opt/ncare/lib/libexec/get_alert_context.py "httpd"  "/ServiceName::CPU" "/Instance::" "/NewState::Critical" "/OldState::Ok" "/UuId::CPU" "/UserParams::mydaemon"
#		python /opt/ncare/lib/libexec/get_alert_context.py mydaemon

######################################################################################################
# Use the below block of code in all the RBA scripts. Control sending alerts with variable "useApi"  #
######################################################################################################

useApi = False
api = None
try:
	sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
	from RBAPythonApi import RBAPythonApi
	api = RBAPythonApi(sys.argv)
	# To check if it is a event triggered execution.
	if api.monitorName:
		useApi = True
except Exception, emsg:
	useApi = False

####################################################################################################
_sub = "-------- additional alert context --------"
p = subprocess.Popen(["ping", "-c", "2", "www.google.com"], stdout=subprocess.PIPE)
_desc, err = p.communicate()

#print _sub
#print _desc



if useApi:
	api.sendAlertMsg(monitor=None, subject=_sub, description=_desc, newState=None, oldState=None, alertGroup=None, alertType=None, alertTime=None)

sys.exit(0)
