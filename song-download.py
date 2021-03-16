import urllib2
import requests
import sys
import os
import random
import ntpath
import glob
import eyed3

# from song_download import download_song
from bs4 import BeautifulSoup


def change_song_name(folder):
	# folder = 'C:/Users/Arvind/Desktop/Newfolder/'
	folder = folder + '/'
	print "name changing" + folder
	for x in glob.glob(folder + '*.mp3'):
		if ntpath.exists(x):
			# print os.remove(x)
			print x
			file_name = eyed3.load(x)
			if hasattr(file_name, 'tag'):
				if hasattr(file_name.tag, 'title'):
					os.rename(x, folder + file_name.tag.title + '.mp3')


def download_song(url, folder):
	# save_path = 'C:/Users/Arvind/Desktop/Newfolder'
	save_path = folder
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




if len(sys.argv) > 2:
	quote_page = str(sys.argv[1])
	folder = str(sys.argv[2])
else:
	print 'Give url of film from sunmusiq and directory to download as Argument'
	sys.exit();	
# quote_page = 'https://www.sunmusiq.com/movies/boys-2003-tamil-movie-songs-196-starmusiq-download.html'

req = urllib2.Request(quote_page, headers={'User-Agent' : "Magic Browser"}) 
page = urllib2.urlopen(req)
# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')
hrefs = soup.find_all('a', href=True, attrs={'class': 'label-info'})
for a in hrefs:
	sub_req = urllib2.Request(a['href'], headers={'User-Agent' : "Magic Browser"}) 
	sub_page = urllib2.urlopen(sub_req)
	# parse the html using beautiful soup and store in variable `soup`
	sub_soup = BeautifulSoup(sub_page, 'html.parser')
	sub_hrefs = sub_soup.find_all('a', href=True, attrs={'class': 'btn-success'})
	for b in sub_hrefs:
		download_song(b['href'], folder);
		print b['href']

print "changing name"
change_song_name(folder)


