import sublime
import sublime_plugin
import json
import os

try:
    # ST3
    from ..utils.cli import CLI
except ImportError:
    # ST2
    from bower.utils.cli import CLI

class InstallDependenciesCommand(sublime_plugin.WindowCommand):
    def get_config_path(self):
        project_file_path = self.window.project_file_name()
        if not project_file_path:
            return self.window.folders()[0]
        else:
            return os.path.dirname(project_file_path)

    def run(self):
        self.install_package()

    def install_package(self):
        command = ['install', '--save']
        CLI().execute(command, cwd=self.get_config_path())
