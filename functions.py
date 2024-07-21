from classes import *
def change_audio_driver():
    os.putenv('SDL_AUDIODRIVER', 'alsa')
    os.putenv('SDL_AUDIODEV', '/dev/audio')
@app.route('/')
@app.route('/library')
def library():
    return "<br>".join(str(os.listdir(source_paths[0]).split(",")))

def Audio_Daemon():
    queue = []
    while not Shutdown_Flag.is_set():
        with open("queue.py", "r") as f:
            try:
                queue = eval(f.read())
            except:
                queue = ["None"]
        if pygame.mixer.music.get_busy() == 0 and (queue and queue[0] != "None"):
            if queue:
                print(info("Now Playing " + queue[0]))
                for path in source_paths:
                    if os.path.exists(path + queue[0]):
                        pygame.mixer.music.load(path + queue.pop(0))
                        pygame.mixer.music.play()
                        break
            with open("queue.py", "w") as f:
                f.write(str(queue))