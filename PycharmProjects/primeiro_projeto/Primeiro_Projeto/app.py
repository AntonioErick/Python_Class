import eel

eel.init('web')

#try:
eel.start(  'index.html', size=(850, 400), port=0)
#except(SystemExit, MemoryError, KeyboardInterrupt):
#    print("Program Exit, Save Logs if Needed")