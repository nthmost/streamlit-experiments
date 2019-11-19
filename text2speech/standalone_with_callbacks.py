import pyttsx3



def main(engine):
    engine.say('How about that dog, huh?')
    engine.iterate()

def onStart(name):
   print('starting', name)
def onWord(name, location, length):
   print('word', name, location, length)
def onEnd(name, completed):
   print('finishing', name, completed)
   if name == 'fox':
      engine.say('What a lazy dog!', 'dog')
   elif name == 'dog':
      engine.endLoop()
engine = pyttsx3.init()
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
engine.say('Starting text to speech.', 'fox')
engine.startLoop(False)

main(engine)

engine.endLoop()


