
import speech_recognition as sr
from textblob import TextBlob

# Record Audio
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source,timeout=1,phrase_time_limit=5)

# Speech recognition using Google Speech Recognition
try:
    print("You said: " + r.recognize_google(audio))

    words_you_spoke=r.recognize_google(audio)
    words_you_spoke = words_you_spoke.replace(",000,000", " m").replace(",000", " k").replace("′", "'").replace("’", "'")\
                           .replace("won't", " will not").replace("cannot", " can not").replace("can't", " can not").replace("haven't", " have not")\
                           .replace("n't", " not").replace("what's", " what is").replace("it's", " it is")\
                           .replace("'ve", " have").replace("'m", " am").replace("'re", " are")\
                           .replace("he's", " he is").replace("she's", " she is").replace("'s", " own")\
                           .replace("%", " percent ").replace("₹", " rupee ").replace("$", " dollar ")\
                           .replace("€", " euro ").replace("'ll", " will").replace("how's"," how has").replace("y'all"," you all")\
                           .replace("o'clock"," of the clock").replace("ne'er"," never").replace("let's"," let us")\
                           .replace("finna"," fixing to").replace("gonna"," going to").replace("gimme"," give me").replace("gotta"," got to").replace("'d"," would")\
                           .replace("daresn't"," dare not").replace("dasn't"," dare not").replace("e'er"," ever").replace("everyone's"," everyone is")\
                           .replace("'cause'"," because")
    
    # the following code is used to say what language u spoke
    word10 = TextBlob(words_you_spoke)
    z1 =word10.detect_language()
    if(z1=='en'):
        print("The language you spoke is english")
    if(z1=='hi'):
        print("The language you spoke is hindi")
    if(z1=='bn'):
        print("The language you spoke is bengali")
    if(z1=='zh-CN'):
        print("The language you spoke is chinese")
    if(z1=='ta'):
        print("The language you spoke is tamil")

    # next portion it says about the state of the sentence you spoke
    blob = TextBlob(words_you_spoke+'.')
    for sentence in blob.sentences:
         if(sentence.sentiment.polarity<0):
            print("YOU SPOKE A NEGATIVE SENTENCE")
         if(sentence.sentiment.polarity>0):
            print("YOU SPOKE A POSITIVE SENTENCE")
         if(sentence.sentiment.polarity==0):
            print("YOU SPOKE A NEUTRAL SENTENCE")
    
except sr.UnknownValueError:
    print("Your audio is not clear")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
