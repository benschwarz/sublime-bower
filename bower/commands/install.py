import sublime
import sublime_plugin
import json
import os
try:
    # ST3
    from ..utils.api import API
except ImportError:
    # ST2
    from bower.utils.api import API


class InstallCommand(sublime_plugin.WindowCommand):
    def run(self, *args, **kwargs):
        self.list_packages()

    def list_packages(self):
        self.fileList = []
        registryUrl = self.get_registry_url()
        packages = API().get('packages', registryUrl)
        packages.reverse()

        for package in packages:
            self.fileList.append([package['name'], package['url']])
        self.window.show_quick_panel(self.fileList, self.get_file)

    def get_file(self, index):
        if (index > -1):
            if not self.window.views():
                self.window.new_file()

            name = self.fileList[index][0]
            cwd = self.window.folders()[0]
            self.window.run_command("download_package", {"pkg_name": name, "cwd": cwd})

    def get_bower_config(self):
        path = os.path.join(self.window.folders()[0], '.bowerrc')

        if not os.path.exists(path):
            return {}

        try:
            jsonData = open(path)
            return json.load(jsonData)
        except:
            sublime.error_message('Unable to parse .bowerrc configuration')

    def get_project_settings(self):
        projectData = sublime.active_window().project_data()
        if projectData and 'settings' in projectData and 'bower' in projectData.get('settings'):
            return projectData.get('settings').get('bower')
        return {}

    def get_plugin_settings(self):
        pluginSettings = sublime.load_settings('Bower.sublime-settings')
        if pluginSettings:
            return pluginSettings
        return {}

    def get_registry_url(self):
        config = self.get_bower_config()
        if 'registry' in config:
            return config.get('registry')

        projectSettings = self.get_project_settings()
        if 'registry' in projectSettings:
            return projectSettings.get('registry')

        pluginSettings = self.get_plugin_settings()
        if pluginSettings.get('registry'):
            return pluginSettings.get('registry')

        return None
