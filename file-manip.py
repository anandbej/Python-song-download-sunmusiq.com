import ntpath
import glob
import os
import eyed3

folder = 'C:/Users/Arvind/Desktop/Newfolder'
for x in glob.glob(folder + '/*.mp3'):
	if ntpath.exists(x):
		# print os.remove(x)
		print x
		file_name = eyed3.load(x)
		# print file_name.tag.title
		if str(file_name.tag.album) is not None:
			print str(file_name.tag.album)
			print 'here'
		os.rename(x, folder + '/' + file_name.tag.title + '.mp3')
		# os.rename(folder, folder + file_name.tag.album)

