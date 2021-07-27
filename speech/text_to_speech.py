
from gtts import gTTS
tts = gTTS(text="python audio is created at the folder", lang='en')
tts.save("sample.mp3")
