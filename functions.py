from classes import *
def change_audio_driver():
    os.putenv('SDL_AUDIODRIVER', 'alsa')
    os.putenv('SDL_AUDIODEV', '/dev/audio')
@app.route('/')
@app.route('/library')
def library():
    return flask.render_template('index.html', songs=[source_paths[0]+os.listdir(source_paths[0])[0]])