import urllib2
import requests
import sys
import os
import random

# from song_download import download_song
from bs4 import BeautifulSoup

def download_song(url):
	save_path = 'C:/Users/Arvind/Desktop/Newfolder'
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




if len(sys.argv) > 1:
	quote_page = str(sys.argv[1])
else:
	print 'Give url as Argument'
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
		download_song(b['href']);
		print b['href']





