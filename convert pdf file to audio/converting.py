# req-> python 3.7 ------ pip intall PyPDF2 ----- pip install gTTS -----
# Before running the file put the pdf in following directory "C:/Users/user/Desktop/" and the audio file will be created at the location "C:/Users/user/Desktop/story1"

import PyPDF2
from gtts import gTTS
t=input("Enter name of the pdf file to convert to audio\n")
pdfFileObj=open("C:/Users/user/Desktop/"+t+".pdf","rb")

pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
mytext=""

for pageNum in range(pdfReader.numPages):
    pageObj=pdfReader.getPage(pageNum)

    mytext+=pageObj.extractText()
#print(mytext)
pdfFileObj.close()

tts=gTTS(text=mytext,lang='en')
tts.save("C:/Users/user/Desktop/story1.mp4")
