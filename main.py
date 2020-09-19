import gtts
from playsound import playsound
myText=str(input())
print("Press 1 for playing the audio or else Press 0 for saving the audio!!!!")
tts=gtts.gTTS(text=myText,lang='en',slow=0)

def option(z):

    switcher={
        0:tts.save("final1.mp3"),
        1:playsound("final1.mp3")
    }
    return switcher.get(z,"option not available")

n=int(input("Enter choice: "))
c=option(n)
if(n==0):
    print("audio is saved")
elif(n==1):
    print("audio is played")
else:
    print("enter the valid option!!")



