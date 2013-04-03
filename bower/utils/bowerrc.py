import os
import json
from os.path import expanduser

class BowerRC():
  def exists():
    if self.get_path() != None:
      return true
    else:
      return false

  def get_path(this):
    bowerrc = ".bowerrc"
    project_home_dir = "" # Figure this out

    projectrc = os.path.join(project_home_dir, bowerrc)
    homerc = os.path.join(expanduser("~"), bowerrc)

    for path in [projectrc, homerc]:
      if os.path.exists(path)
        return path

    return None

  def read(this):
    if self.exists():
      return json.loads(self.get_path())
    else:
      return {}