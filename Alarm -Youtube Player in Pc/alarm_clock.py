import datetime
import os
import time
import random
import webbrowser

# If video URL file does not exist, create one
if not os.path.isfile("youtube_alarm_videos.txt"):
    print("Creating 'youtube_alarm_videos.txt'...")
    with open("youtube_alarm_videos.txt", "w") as alarm_file:
        alarm_file.write("https://youtube.com/watch?v=anM6uIZvx74")

def check_alarm_input(alarm_time):
    """ Checks to see if the user has entered in a valid alarm time."""
    if len(alarm_time) == 1: # [Hour] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0:
            return True

    if len(alarm_time) == 2: # [Hour:Minute] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and alarm_time[1] < 60 and alarm_time[1] >= 0 :
            return True

    elif len(alarm_time) == 3: # [Hour:Minute:Second] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and alarm_time[1] < 60 and alarm_time[1] >= 0 and alarm_time[2] < 60 and alarm_time[2] >= 0:
            return True

    return False

# Get user input for the alarm time
print("Set a time for the alarm (Ex. 06:30 or 18:30:00)")
while True:
    alarm_input =input(">> ")
    try:
        alarm_time = [int(n) for n in alarm_input.split(":")]
        if check_alarm_input(alarm_time):
            break
        else:
            raise ValueError
    except ValueError:
        print("ERROR: Enter the time in HH:MM:SS format")

# convert the alarm time from [H:M] or [H:M:S] to seconds
seconds_hms = [3600, 60, 1] # Number of seconds in an Hour, Minute, and second
alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

# Get the current time of the day in seconds
now = datetime.datetime.now()
current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

# Calculate the number of seconds until the alarm goes off
time_diff_seconds = alarm_seconds - current_time_seconds

# If time difference is negative, set the alarm for next day
if time_diff_seconds < 0:
    time_diff_seconds += 86400 # no of seconds in a day

# Display the amount of time until the alarm goes off
print("Alarm set to go off in %s" %datetime.timedelta(seconds=time_diff_seconds))

time.sleep(time_diff_seconds)

# time for the alarm goes off
print("Wake Up!")

# Load list of possible video URLs
with open("youtube_alarm_videos.txt", "r") as alarm_file:
    videos = alarm_file.readlines()

# open a random video from the list of videos
webbrowser.open(random.choice(videos))
