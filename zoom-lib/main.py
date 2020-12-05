# Zoom Library In Python
import subprocess

def join_meeting(mt_id):
  # Simulating Applescript
  # like this:
  # subprocess.run("osascript -e 'applescript code goes here'", shell=True)
  # checking if meeting id is a string of numbers
  try:
    assert isinstance(mt_id, str) == True
    a = int(mt_id)
  except:
    print("Meeting Id must be a string of numbers")
    quit()

  command = "osascript -e 'activate application " + '"zoom.us"\n' + "tell application " + '"System Events"\n' + '  keystroke "j" using command down\n'
  for char in mt_id:
    command += f'  keystroke "{char}"\n'
  command += "  key code 36\n" + "end tell'"
  subprocess.run(command, shell=True)
