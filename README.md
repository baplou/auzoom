# auzoom
This is a Python Library which allows you to automate zoom by the use of various classes and
functions. It does this by using Applescript and running it as a shell command.

## Example Usage (so far)

```python
from auzoom import ZoomClient
z = ZoomClient() # Creating ZoomClient() object, this opens zoom

# Functions
z.start_meeting() # starts a meeting
z.mic() # changes the microphones state (if unmuted the microphone will mute, if muted the microphone will unmute
z.camera() # changes the cameras state, like .mic()
z.quit_zoom() # quits zoom
```

## Things to keep in mind
* A feature activates zoom and simulates keystrokes that do what the feature says it's going to do
* ONLY works on MACOS

## Running the example
```bash
git clone https://github.com/baplou/auzoom.git
cd auzoom; ./example.py
```

## TODO
* pip installation
* more features
* Support for windows
