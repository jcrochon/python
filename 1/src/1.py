import time
import webbrowser
  
tot_breaks = 300
cnt_break  = 0

print("Started: " + time.ctime())

def do_it():
    webbrowser.open("https://www.youtube.com/")
    webbrowser.open("https://www.youtube.com/")
    webbrowser.open("https://www.youtube.com/")
    webbrowser.open("https://www.youtube.com/")

do_it()

while (cnt_break < tot_breaks):
    do_it()
    time.sleep(3*60)
    cnt_break = cnt_break + 1

print("Ended: " + time.ctime())