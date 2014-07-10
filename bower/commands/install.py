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
    def get_config_path(self):
        try:
            project_file_path = self.window.project_file_name()
            return os.path.dirname(project_file_path)
        except AttributeError:
            return self.window.folders()[0]

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
            cwd = self.get_config_path()
            self.window.run_command("download_package", {"pkg_name": name, "cwd": cwd})

    def get_bower_config(self):
        path = os.path.join(self.get_config_path(), '.bowerrc')

        if not os.path.exists(path):
            return {}

        try:
            jsonData = open(path)
            return json.load(jsonData)
        except:
            sublime.error_message('Unable to parse .bowerrc configuration')

    def get_registry_url(self):
        config = self.get_bower_config()

        registry = config.get('registry')
        if not registry:
            return None
        if isinstance(registry, str):
            return registry
        if isinstance(registry, dict):
            searchRegistry = registry.get('search')
            if isinstance(searchRegistry, str):
                return searchRegistry
            if isinstance(searchRegistry, list):
                return searchRegistry[0]

        return None
