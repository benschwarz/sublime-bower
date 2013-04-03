import json
from bower.utils.bowerrc import BowerRC

class PackageDefinition():
  def definition_path():
    bowerrc = BowerRC()
    
    if bowerrc.exists() and bowerrc.read().has_key('directory'):
      return bowerrc.read()['directory']
    else
      return "components"

  def read(self, package_name):
    path = self.definition_path() + "/" + package_name

    definition = open(path)
    return json.loads(definition)