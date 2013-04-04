import os
import json
from os.path import expanduser


class BowerRC():
    def get_path(self, projectdir=""):
        bowerrc = ".bowerrc"
        projectrc = os.path.join(projectdir, bowerrc)
        homerc = os.path.join(expanduser("~"), bowerrc)

        for path in [projectrc, homerc]:
            if os.path.exists(path):
                return path

        return None

    def read(self, projectdir):
        path = self.get_path(projectdir)
        if path is not None:
            return json.loads(open(path).read())
        else:
            return {}
