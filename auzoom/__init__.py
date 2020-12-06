import os
import platform

if os.name == "posix" and platform.system() == "Darwin":
  # only works on macos
  from auzoom.main import ZoomClient
else:
  class NotMacosError(Exception):
    pass

  #print("auzoom only works on MACOS")
  #print("Support for WINDOWS 10 will be added later")
  #print("If you have any suggestions open an issue or a pull request at:")
  #print("https://www.github.com/baplou/auzoom")

  raise NotMacosError("auzoom only works on MACOS\nIf you have any suggestions open an issue or a pull request at:\nhttps://www.github.com/baplou/auzoom")
