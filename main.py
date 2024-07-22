from functions import *
from config import *
clear()
print_at(1, 1, "Starting...")
Audio_Daemon_Thread = threading.Thread(target=Audio_Daemon)
def on_shutdown():
    Shutdown_Flag.set()
    Audio_Daemon_Thread.join()
    pygame.quit()
atexit.register(on_shutdown)

queue = load_queue()
if Start_Audio_At_Boot:
    Audio_Daemon_Thread.start()
else:
    queue = ["Stop"]+queue
    save_queue(queue)
    Audio_Daemon_Thread.start()
print_at(1, 2, "Started!")
sleep(0.5)
clear()
print(f"""{Fore.BLUE}    - - - - - - - - - - - - - - - -
    | \                           | \ 
    |   - - - - - - - - - - - - - - - -
    |   |                         |   |
    |   |                         |   |
    |   |      {Fore.GREEN} .~~.   .~~.       {Fore.BLUE}|   |
    |   |      {Fore.GREEN}'. \ ' ' / .'      {Fore.BLUE}|   |
    |   |    {Fore.RED}   .~ .~~~..~.       {Fore.BLUE}|   |
    |   |    {Fore.RED}  : .~.'~'.~. :      {Fore.BLUE}|   |
    |   |    {Fore.RED} ~ (   ) (   ) ~     {Fore.BLUE}|   |
    |   |    {Fore.RED}( : '~'.~.'~' : )    {Fore.BLUE}|   |
    |   |    {Fore.RED} ~ .~ (   ) ~. ~     {Fore.BLUE}|   |
    |   |    {Fore.RED}  (  : '~' :  )      {Fore.BLUE}|   |
    |   |    {Fore.RED}   '~ .~~~. ~'       {Fore.BLUE}|   |
    |   |    {Fore.RED}       '~'           {Fore.BLUE}|   |
    - - | - - - - - - - - - - - - -   |
      \ |                           \ |
        - - - - - - - - - - - - - - - -{RESET}""")
app.run('0.0.0.0',80)