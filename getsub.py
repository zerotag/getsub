import sys
import time
import os
import hashlib
import requests

user_agent = {'User-Agent': "SubDB/1.0 (getsub/0.1; http://github.com/trecuu/getsub)"}
language = 'pt,en'#selected languages
videoFile = str(sys.argv[1]) #file location ex.: C:\Downloads\Video.mkv


def get_hash(name):
	readsize = 64 * 1024
	with open(name, 'rb') as f:
		size = os.path.getsize(name)
		data = f.read(readsize)
		f.seek(-readsize, os.SEEK_END)
		data += f.read(readsize)
	return hashlib.md5(data).hexdigest()


def get_sub(fileHash, language):
	url = 'http://api.thesubdb.com/?action=download&hash='+fileHash+'&language='+language 
	url = requests.get(url, headers=user_agent)
	if str(url.status_code) == '404':
		print ('Not Found')
	elif str(url.status_code) == '400':
		print ('Bad Request')
	elif str(url.status_code) == '200':
		open(videoFile[:-4]+'.srt', 'wb').write(url.content)
		print ('SUB DOWNLOADED!')



videoHash = get_hash(videoFile)
get_sub(videoHash,language)

time.sleep(1)