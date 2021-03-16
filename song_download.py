import requests
import os
import random

url='http://www.musiqfile.xyz/download-7s-sng-new/download-3.ashx?Token=U29uZyQkMTI0MCQkVHlwZTIkJE9wZW5Eb3dubG9hZCQkMjAxOC0wNS0yMCAxNToxNTo1';
def download_song(url):
	# save_path = 'C:/Users/Arvind/Desktop/Newfolder'
	save_path = '/home/bej/Desktop/'
	print "DOWNLOADING here "
	url = 'http://www.musiqfile.xyz/download-7s-sng-new/' + url
	print url
	mobj = requests.get(url);

	filename = os.path.join(save_path,'song1')
	if os.path.exists(filename + '.mp3'):
	    append_write = 'w' # append if already exists
	    filename = filename + str(random.randint(1,100))
	else:
	    append_write = 'w' # make a new file if not
	filename = filename + '.mp3'
	print "writing" + filename
	with open(filename,append_write) as a:
	    a.write(mobj.content)
	return 0;

download_song(url);

