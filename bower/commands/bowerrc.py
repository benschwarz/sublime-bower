import sublime
import sublime_plugin
import json
import os


class BowerrcCommand(sublime_plugin.WindowCommand):
    def run(self):
        try:
            path = os.path.join(self.window.folders()[0], '.bowerrc')

            if not os.path.exists(path):
                rc = json.dumps({'directory': 'components'}, indent=2)

                f = open(path, 'w+')
                f.write(rc)

            self.window.open_file(path)
        except IndexError:
            sublime.error_message('Oh Dear! I need a directory for file .bowerrc.')