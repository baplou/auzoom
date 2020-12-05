import os
import platform

if os.name == "posix" and platform.system() == "Darwin":
  from auzoom.main import ZoomClient
else:
  print("auzoom only works on MACOS")
  print("Support for WINDOWS 10 will be added later")
  print("if you have any suggestions open an issue or a pull request at:")
  quit()
