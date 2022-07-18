import sys
import time
import random
import datetime
import winsound
from prettytable import ALL
from datetime import datetime  
from datetime import timedelta
from prettytable import PrettyTable

class Processing_class():    
    def processing_function():
    
        print("ENTER THE POWER OF THE HEATING DEVICE")
        P = float(input())

        print("")

        print("ENTER THE NUMBER OF LITRES OF WATER TO BE HEATED")
        L = float(input())

        print("")

        V = L/1000
        ϕ = 1000
        m = V*ϕ
        c = 4200
        ϴ2 = 100
        ϴ1 = 25
        Δϴ = ϴ2 - ϴ1
        t = ((m*c*Δϴ)/(P))

        sec = t
        sec = sec % (24 * 3600)
        hour = sec // 3600
        sec %= 3600
        min = sec // 60
        sec %= 60

        now = datetime.now()
        alarm = datetime.now() + timedelta(hours = hour, minutes = min, seconds = sec)
        alarm_ring = alarm.strftime("%H:%M:%S")

        print("THE HEATING TIME WILL BE: %02d Hrs %02d Min %02d Sec" %(hour, min, sec))
        print("")

        print("YOU SHOULD CHECK YOUR WATER AT:",alarm_ring,"\n")

        print("WOULD YOU LIKE TO SET AN ALARM AT THIS TIME ? \n")
        x = PrettyTable(hrules = ALL)
        x.add_column("MENU",["[Y]: SET ALARM","[N]: EXIT"])
        x.align = "l"
        print(x)
        print("\nRESPONSE ? ")
        answer = str(input())

        while answer != "Y" and answer != "y" and answer != "N" and answer != "n":
            print("SYNTAX ERROR!!! ENTER EITHER [Y] OR [N]")
            answer = str(input())

        if answer == "Y" or answer == "y":
            print("\nTIME HAS BEEN SET \n\nSIT BACK AND RELAX WE WILL REMIND YOU WHEN IT'S TIME\n")                     
            
            def check_alarm_input(alarm_time):
                """Checks to see if the system has entered in a valid alarm time"""
                if len(alarm_time) == 1: # [Hour] Format
                    if alarm_time[0] < 24 and alarm_time[0] >= 0:
                        return True
                if len(alarm_time) == 2: # [Hour:Minute] Format
                    if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
                       alarm_time[1] < 60 and alarm_time[1] >= 0:
                        return True
                elif len(alarm_time) == 3: # [Hour:Minute:Second] Format
                    if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
                       alarm_time[1] < 60 and alarm_time[1] >= 0 and \
                       alarm_time[2] < 60 and alarm_time[2] >= 0:
                        return True
                return False

            # Get user input for the alarm time
            while True:
                alarm_input = alarm_ring
                try:
                    alarm_time = [int(n) for n in alarm_input.split(":")]
                    if check_alarm_input(alarm_time):
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("SYNTAX ERROR!!! ENTER TIME IN HH:MM or HH:MM:SS FORMAT\n")

            # Convert the alarm time from [H:M] or [H:M:S] to seconds
            seconds_hms = [3600, 60, 1] # Number of seconds in an Hour, Minute, and Second
            alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

            # Get the current time of day in seconds
            current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

            # Calculate the number of seconds until alarm goes off
            time_diff_seconds = alarm_seconds - current_time_seconds

            # If time difference is negative, set alarm for next day
            if time_diff_seconds < 0:
                time_diff_seconds += 86400 # number of seconds in a day

            # Sleep until the alarm goes off
            time.sleep(time_diff_seconds)

            # Time for the alarm to go off
            print("YOUR WATER IS BOILING!!!")
            winsound.Beep(700,5000)
            
        elif answer == "N" or answer == "n":
            sys.exit()