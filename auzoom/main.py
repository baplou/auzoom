# Zoom Library In Python
# Simulating Applescript
# like this:
# subprocess.run("osascript -e 'applescript code goes here'", shell=True)

import subprocess
import time

# Todo:
#
# - Support for Windows
#   - Powershell code

class ZoomClient:
  def __init__(self):
    self.activate_zoom()
    time.sleep(2)

  # used alot
  @staticmethod
  def activate_zoom():
    subprocess.run("osascript -e 'activate application " + '"zoom.us"' + "'", shell=True)

  def join_meeting(self, mt_id, press_enter=True):
    self.activate_zoom()
    mt_id = mt_id.replace(" ", "")
    try:
      assert isinstance(mt_id, str) == True
      a = int(mt_id)
    except:
      print("Meeting ID must be a string of numbers.")
      quit()

    command = "osascript -e 'tell application " + '"System Events"\n' + '  keystroke "j" using command down\n'
    for char in mt_id:
      command += f'  keystroke "{char}"\n'
    if press_enter == True:
      command += "  key code 36\n" + "end tell'"
    else:
      command += "end tell'"
    subprocess.run(command, shell=True)

  def quit_zoom(self):
    self.activate_zoom()
    command = "osascript -e 'tell application " + '"zoom.us"' + " to quit'"
    subprocess.run(command, shell=True)
    print("ignore the error sign above, applescript is weird")

  def start_meeting(self):
    self.activate_zoom()
    command = "osascript -e 'tell application " + '"System Events"\n  keystroke "v" using {command down, control down}\nend tell' + "'"
    subprocess.run(command, shell=True)

  def mic(self):
    self.activate_zoom()
    command = "osascript -e 'tell application " + '"System Events"\n  keystroke "a" using {command down, shift down}\nend tell' + "'"
    subprocess.run(command, shell=True)

  def camera(self):
    self.activate_zoom()
    command = "osascript -e 'tell application " + '"System Events"\n keystroke "v" using {command down, shift down}\nend tell' + "'"
    subprocess.run(command, shell=True)
