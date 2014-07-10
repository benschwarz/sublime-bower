import sublime
import sublime_plugin
import json
import os


class BowerrcCommand(sublime_plugin.WindowCommand):
    def run(self):
        try:
            bowerrc = path()

            if not os.path.exists(bowerrc):
                rc = json.dumps({'directory': 'components'}, indent=2)

                f = open(bowerrc, 'w+')
                f.write(rc)

            self.window.open_file(bowerrc)
        except IndexError:
            sublime.error_message('Oh Dear! I need a directory for file .bowerrc.')
    def path
        try:
            project_file_path = self.window.project_file_name()
            return os.path.join(os.path.dirname(project_file_path), '.bowerrc')
        except:
            return os.path.join(self.window.folders()[0], '.bowerrc')