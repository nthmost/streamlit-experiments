import pyttsx3

def say_it_all(stuff):
    engine.say('whatever', stuff)
    engine.startLoop(False)
    engine.iterate()
    engine.endLoop()


def main_loop(engine):
    say_it_all('Starting Server')
    while True:
        stuff = input("What should I say? ")
        say_it_all(stuff)

def onStart(name):
   print('starting', name)
def onWord(name, location, length):
   print('word', name, location, length)
def onEnd(name, completed):
   print('finishing', name, completed)
#   if name == 'fox':
#      engine.say('What a lazy dog!', 'dog')
#   elif name == 'dog':
#      engine.endLoop()


if __name__ == '__main__':
    engine = pyttsx3.init()
    engine.connect('started-utterance', onStart)
    engine.connect('started-word', onWord)
    engine.connect('finished-utterance', onEnd)
    engine.say('Starting text to speech.', 'fox')
    engine.startLoop(False)

    main_loop(engine)

    engine.endLoop()


