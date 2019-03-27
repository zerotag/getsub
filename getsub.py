import sys
import time
import os
import hashlib
import requests

user_agent = {'User-Agent': "SubDB/1.0 (getsub/0.1; http://github.com/trecuu/getsub)"}

def get_hash(name):
        readsize = 64 * 1024
        with open(name, 'rb') as f:
            size = os.path.getsize(name)
            data = f.read(readsize)
            f.seek(-readsize, os.SEEK_END)
            data += f.read(readsize)
        return hashlib.md5(data).hexdigest()

def get_sub(fileHash):
	url = 'http://api.thesubdb.com/?action=download&hash='+fileHash+'&language=pt,en'
	r = requests.get(url, headers=user_agent)
	if str(r.status_code) == '404':
		print ('Not Found')
	elif str(r.status_code) == '400':
		print ('Bad Request')
	elif str(r.status_code) == '200':
		open(str(sys.argv[1])+'.srt', 'wb').write(r.content)
		print ('SUB DOWNLOADED!')



videoHash = get_hash(str(sys.argv[1]))
get_sub(videoHash)

time.sleep(1)