from functions import *

def on_shutdown():
    Shutdown_Flag.set()
    Audio_Daemon_Thread.join()
    pygame.quit()
atexit.register(on_shutdown)

Audio_Daemon_Thread = threading.Thread(target=Audio_Daemon)
Audio_Daemon_Thread.start()
app.run('0.0.0.0',80,debug=True)