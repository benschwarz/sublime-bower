import json
import os
from bower.utils.bowerrc import BowerRC


class PackageDefinition:
    def __init__(self, projectdir):
        self.projectdir = projectdir

    def get_installed_packages(self):
        defpath = self.definition_path()
        if not os.path.isdir(defpath):
            return []
        return [name for name in os.listdir(defpath) if os.path.isdir(os.path.join(defpath, name))]

    def definition_path(self):
        bowerrc = BowerRC()
        bowercpath = bowerrc.read(self.projectdir)
        
        if 'directory' in bowercpath:
            bower_directory = bowerrc.read(self.projectdir)['directory']
            return os.path.join(self.projectdir, bower_directory)
        else:
            return os.path.join(self.projectdir, "components")

    def read(self, package_name):
        path = os.path.join(self.definition_path(), package_name, "component.json")
        
        if os.path.exists(path):
            return json.loads(open(path).read())
        else:
            print "[Bower]: " + package_name + " doesn't have a component.json - Please submit an issue to the " + package_name + " project to tell the author." 
            return {}