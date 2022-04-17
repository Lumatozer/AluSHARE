def connect():
	print("Welcome to the decentralized browser :)")
	domain=input("Input domain name : ")
	try:
		import socket,json,time,requests
		api_nodes=requests.get("http://127.0.0.1:8080/node")
		mynode=str(api_nodes.text)
		host = mynode
		port = 7777
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.settimeout(1)
		s.connect(('127.0.0.1', port))
		s.settimeout(None)
		s.send("client".encode())
		time.sleep(0.1)
		s.send("hi".encode())
		naach=json.dumps({"type":"get","domain":domain})
		msg = s.recv(1024)
		time.sleep(0.1)
		s.send(naach.encode())
		income=s.recv(1024000).decode()
		if income!="File does not exist/corrupted!":
			html= dict(json.loads(income))[domain]
			f = open('out.html', 'w')
			f.write(html)
			f.close()
			import webbrowser
			webbrowser.open('out.html') 
		else:
			print("File does not exist/corrupted on this node! Try a different node if you think this is a false alert.")
	except Exception as e:
		if str(e)=="dictionary update sequence element #0 has length 1; 2 is required":
			print("File in-existant on the node! Try a different node if you think this is a false alert.")