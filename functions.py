from classes import *
def change_audio_driver():
    os.putenv('SDL_AUDIODRIVER', 'alsa')
    os.putenv('SDL_AUDIODEV', '/dev/audio')
@app.route('/')
@app.route('/library')
def library():
    content = ""
    for song in os.listdir(source_paths[0]):
        content += f"""<button type="button" class="btn" href="/add/{song}">{song}</button><br>"""
    return flask.render_template("index.html",content=content)

@app.route("/playback")
def playback():
    content = f"""<button type="button" class="btn" href="/play">Play</button><br>
    <button type="button" class="btn" href="/pause">Pause</button><br>
    <button type="button" class="btn" href="/stop">Stop</button><br>
    <button type="button" class="btn" href="'/next">Next</button><br>"""
    return flask.render_template("index.html",content=content)

@app.route('/play')
def play():
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