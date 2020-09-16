from gtts import gTTS
from playsound import playsound
from pydub import AudioSegment
s = str(input())
language = 'en'
output = gTTS(text=s,lang = language,slow = False)
output.save("output.mp3")
opt = int(input("Enter 0 for saving the audio file and Enter 1 for playing back live"))
if opt == 0:
    output.export('output.mp3', format='mp3')
elif opt == 1:
    playsound("output.mp3")



