import sublime_plugin
import json
import os

class BowerrcCommand(sublime_plugin.WindowCommand):
    def run(self):
        path = os.path.join(self.window.folders()[0], '.bowerrc')

        if not os.path.exists(path):
            rc = json.dumps({ 'directory': 'components' })

            f = open(path, 'w+')
            f.write(rc)

        self.window.open_file(path)