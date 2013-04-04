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

        if bowercpath is not None and 'directory' in bowercpath:
            return bowerrc.read(self.projectdir)['directory']
        else:
            return os.path.join(self.projectdir, "components")

    def read(self, package_name):
        print self.definition_path()
        print package_name
        path = os.path.join(self.definition_path(), package_name, "component.json")
        print path
        return json.loads(open(path).read())
