import time

def alarm_clock():
    alarm_time = input("Enter the time for the alarm (HH:MM): ")
    
    while True:
        current_time = time.strftime("%H:%M")
        print(f"Current time: {current_time}", end='\r')
        time.sleep(1)  # Check every second
        
        if current_time == alarm_time:
            print("\nAlarm! Time to wake up! ⏰")
            break

alarm_clock()
