import sublime_plugin
from bower.utils.api import API

class InstallCommand(sublime_plugin.WindowCommand):
    fileList = []

    def run(self, *args, **kwargs):
        self.list_packages()

    def list_packages(self):
        packages = API().get('packages')
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