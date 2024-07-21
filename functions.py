from classes import *
def change_audio_driver():
    os.putenv('SDL_AUDIODRIVER', 'alsa')
    os.putenv('SDL_AUDIODEV', '/dev/audio')
@app.route('/')
@app.route('/library')
def library():
    content = ""
    for song in os.listdir(source_paths[0]):
        content += f"<a href='/add/{song}'>{song}</a><br>"
    return flask.render_template("index.html",content=content)

@app.route('/add/<string:song>')
def add(song):
    with open(queuefile, "r") as f:
        queue = eval(f.read())
    queue.append(song)
    with open(queuefile, "w") as f:
        f.write(str(queue))
    return "Added " + song + " to queue <meta http-equiv='refresh' content='0;url=/library'>"

def Audio_Daemon():
    queue = []
    while not Shutdown_Flag.is_set():
        with open(queuefile, "r") as f:
            try:
                queue = eval(f.read())
            except:
                queue = ["None"]
        if pygame.mixer.music.get_busy() == 0 and (queue and queue[0] != "None"):
            if queue:
                song = ""
                for path in source_paths:
                    if os.path.exists(path + queue[0]):
                        print(info("Now Playing " + queue[0]))
                        song = path + queue.pop(0)
                        break
                if song:
                    pygame.mixer.music.load(song)
                    pygame.mixer.music.play()
            with open(queuefile, "w") as f:
                f.write(str(queue))