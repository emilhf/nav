"""
$Id: RpcHandler.py,v 1.7 2002/12/09 15:33:15 magnun Exp $
$Source: /usr/local/cvs/navbak/navme/services/lib/handler/RpcHandler.py,v $
"""
import os
from job import JobHandler, Event
class RpcHandler(JobHandler):
	"""
	args:
	requried
	ex: nfs,nlockmgr
	"""
	def __init__(self, serviceid, boksid, ip, args, version,sysname):
		port = args.get("port", 111)
		JobHandler.__init__(self, "rpc", serviceid, boksid, (ip, port), args, version,sysname)

	def execute(self):
		args = self.getArgs()
		required = args.get('required','').split(',')

		ip, port = self.getAddress()

		input, output, err = os.popen3('/usr/sbin/rpcinfo -p %s' % ip)
		output = output.read()
		if not output:
			return Event.DOWN,'timeout'

		missing = []
		for i in required:
			i = i.strip()
			if output.find(i) == -1:
				missing += [i]
		if missing:
			return Event.DOWN,'missing: ' + ', '.join(missing)
		else:
			return Event.UP, "Ok"

def getRequiredArgs():
	"""
	Returns a list of required arguments
	"""
	requiredArgs = ['required']
	return requiredArgs
			
