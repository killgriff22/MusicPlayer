from classes import *
def change_audio_driver():
    os.putenv('SDL_AUDIODRIVER', 'alsa')
    os.putenv('SDL_AUDIODEV', '/dev/audio')

def load_queue():
    with open(queuefile, "r") as f:
        try:
            queue = eval(f.read())
        except:
            queue = ["None"]
    return queue

def save_queue(queue):
    with open(queuefile, "w") as f:
        f.write(str(queue))
@app.route('/')
@app.route('/library')
def library():
    content = ""
    for song in os.listdir(source_paths[0]):
        content += f"""<a href="/add/{song}"><button type="button" class="btn btn-dark">{song}</button></a><br>"""
    return flask.render_template("index.html",content=content)

@app.route("/playback")
def playback():
    content = f"""
    <a href="/play"><button type="button" class="btn btn-dark">Play</button></a><br>
    <a href="/pause"><button type="button" class="btn btn-dark">Pause</button></a><br>
    <a href="/stop"><button type="button" class="btn btn-dark">Stop</button></a><br>
    <a href="/next"><button type="button" class="btn btn-dark">Next</button></a><br>"""
    return flask.render_template("index.html",content=content)

@app.route('/play')
def play():
    if pygame.mixer.music.get_busy() == 0:
        queue = load_queue()
        if queue:
            if queue[0] == "Stop":
                queue = queue[1:]
                save_queue(queue)
    pygame.mixer.music.unpause()
    return "Playing <meta http-equiv='refresh' content='0;url=/playback'>"
@app.route('/pause')
def pause():
    pygame.mixer.music.pause()
    return "Paused <meta http-equiv='refresh' content='0;url=/playback'>"
@app.route('/stop')
def stop():
    with open(queuefile, "w") as f:
        f.write(str(["None"]))
    pygame.mixer.music.stop()
    return "Stopped <meta http-equiv='refresh' content='0;url=/playback'>"
@app.route('/next')
def next():
    pygame.mixer.music.stop()
    return "Next <meta http-equiv='refresh' content='0;url=/playback'>"

@app.route('/add/<string:song>')
def add(song):
    queue = load_queue()
    if "None" in queue:
        queue.remove("None")
    queue.append(song)
    save_queue(queue)
    return "Added " + song + " to queue <meta http-equiv='refresh' content='0;url=/library'>"

def Audio_Daemon():
    print(info("Audio Daemon Started!"))
    queue = load_queue()
    while not Shutdown_Flag.is_set():
        queue = load_queue()
        if pygame.mixer.music.get_busy() == 0 and (queue and queue[0] != "None"):
            if queue:
                if queue[0] == "Stop":
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(os.path.join(wd,"silence.mp3"))
                    pygame.mixer.music.play()
                    pygame.mixer.music.pause()
                    continue
                song = ""
                for path in source_paths:
                    if os.path.exists(path + queue[0]):
                        print(info("Now Playing " + queue[0]))
                        song = path + queue[0]
                        break
                if song:
                    pygame.mixer.music.load(song)
                    pygame.mixer.music.play()
            save_queue(queue[1:])