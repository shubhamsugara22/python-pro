from gtts import gTTS
mt = input("enter the required text: \t")

language = 'en'
voice = gTTS(text=mt, lang=language, slow=False)
voice.save(“conv.mp3”)
