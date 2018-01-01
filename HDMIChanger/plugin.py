#
#  HDMI Changer - Enigma 2 plugin
#  
#  Plugin assigned to button on remote control allow to quickly change HDMI ports on TV
#
#  Tested on nbox (image by freebox)
#

# Plugin definition
from Plugins.Plugin import PluginDescriptor

def main(session, **kwargs): 
	try:
		file = open('/tmp/hdmi.txt', 'r')
		status = file.read()
		file.close()
	except:
		status = '0'
	
	status = int (status)
	
	port = {
	0: '3f821100',
	1: '3f822100',
	2: '3f823100',
	3: '3f824100'
	} [status]
	
	open('/proc/stb/hdmi/cec', 'w').write(port)
	
	status += 1
	if status == 3: #Number of HDMI ports in TV, max 4  
		status = 0
		
	file = open('/tmp/hdmi.txt', 'w')
	file.write(str(status))
	file.close()
		
	
	
def Plugins(**kwargs): 
	return PluginDescriptor( 
		name="HDMI Changer", 
		description="Allow change HDMI port in TV", 
		where = PluginDescriptor.WHERE_PLUGINMENU, 
		icon="./hdmi.png", 
		fnc=main)
