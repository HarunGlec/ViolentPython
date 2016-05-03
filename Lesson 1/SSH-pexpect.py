import pexpect
PROMPT = ['# ', '>>> ', '> ', '\$ ']

def send_command(child, cmd):
	child.sendline(cmd)
	child.expect('[sudo]')
	child.sendline('310595')
	child.expect('password:')
	child.sendline('qqq')
	child.expect('password:')
	child.sendline('qqq')
	child.expect(PROMPT)
	print child.before
	print 'Password Changed'

def connect(user, host, password):
	ssh_newkey = 'Are you sure you want to continue connecting'
	connStr = 'ssh ' + user + '@' + host
	child = pexpect.spawn(connStr)
	ret = child.expect([pexpect.TIMEOUT, ssh_newkey,'[P|p]assword:'])
	if ret == 0:
		print '[-] Error Connecting'
		return
	if ret == 1:
		child.sendline('yes')
		ret = child.expect([pexpect.TIMEOUT,'[P|p]assword:'])
		if ret == 0:
			print '[-] Error Connecting'
			return
	child.sendline(password)
	child.expect(PROMPT)
	return child
def main():
	host = 'localhost'
	user = 'user'
	password = 'pass'
	child = connect(user, host, password)
	send_command(child, 'sudo passwd root')
if __name__ == '__main__':
	main()