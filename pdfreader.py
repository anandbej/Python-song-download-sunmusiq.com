# importing required modules
# import PyPDF2 
import pyttsx3;
import subprocess
import pdftotext


def textToWav(text,file_name):
   subprocess.call(["espeak", "-w"+file_name+".wav", "-g 8", "-v+f3", text])


# creating a pdf file object 
pdfFileObj = open('itoohadluvstory.pdf', 'rb') 
# pdfFileObj = open('sample.pdf', 'rb') 

# Load your PDF
with pdfFileObj as f:
    pdf = pdftotext.PDF(f)

# If it's password-protected
# with open("secure.pdf", "rb") as f:
#     pdf = pdftotext.PDF(f, "secret")

# How many pages?
# print(len(pdf))
pdflength = len(pdf);

pages=0
for x in xrange(1,pdflength):
	# part = "\n\n".join(pdf[x])
	# if pages == 10:

	# pages = pages + 1;
	# # pdf = pdf[100]
	print pdf[x]
	textToWav(pdf[x],'itoohadluvstory' + str(x))
	pass

exit();
# Iterate over all the pages
# final = "\n\n".join(pdf);
# final = final.encode('ascii','ignore');
# print final
# print type(final.encode('ascii','ignore'));

pdfFileObj.close() 
# textToWav(final,'itoohadluvstory')
