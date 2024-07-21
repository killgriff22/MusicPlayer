from modules import *
pygame.mixer.music.load("testfile.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue