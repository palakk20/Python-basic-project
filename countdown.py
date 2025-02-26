import time

def countdown_timer():
    seconds = int(input("Enter countdown time in seconds: "))
    
    while seconds > 0:
        print(seconds, "seconds remaining...")
        time.sleep(1)  # Pause for 1 second
        seconds -= 1
    
    print("Time's up! ⏰")

countdown_timer()
