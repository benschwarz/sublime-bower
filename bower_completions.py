import sublime
import sublime_plugin
import os
from bower.utils.package_definition import PackageDefinition


class BowerCompletions(sublime_plugin.EventListener):

    def get_completion(self, file, name):
        path = os.path.join(self.packageDefinition.definition_path(), file.replace("./", ""))
        return (name +"\tbower", "<script src=\"" + path + "\"></script>")

    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], "text.html - source"):
            return []

        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))

        if ch != '`':
            return []

        packages = self.build_package_list(os.path.join(view.window().folders()[0]))
            
        return (packages, sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)

    def build_package_list(self, path):
        self.packageDefinition = PackageDefinition(path)

        packages = []
        for pkg in self.packageDefinition.get_installed_packages():
            if self.packageDefinition.read(pkg).has_key('main'):
                packages.append(self.get_completion(self.packageDefinition.read(pkg)["main"], pkg))
            else:
                print "[Bower]: " + pkg + " doesn't have a correctly formatted component.json file (missing 'main')"
        return packages


