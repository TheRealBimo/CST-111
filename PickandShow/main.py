import winsound
def playAntelope():
  winsound.PlaySound('sound.wav', winsound.SND_ASYNC)
  print("This is a test of the sound system.")

def showAntelope():
  image = 'antelope.jpg'
  showimage = makePicture('antelope.jpg')
  show(showimage)

question = input("Hello, what would you like to access? Picture or Sound?")
print("phase 1")
if question == "picture":
    print("Phase 2 - pic")
    showAntelope()
    print("Phase 3 - pic")
    exit()
if question == "sound":
    playAntelope()
    print("Sound Played")
else: 
    print("What you've entered is invalid. Please try again.")
