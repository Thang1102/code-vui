
from hashlib import sha256
username = "semaphore"
password = "signalperson"
line = username + password
print(sha256(line.encode('utf-8')).hexdigest())
