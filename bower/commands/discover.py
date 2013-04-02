import sublime_plugin

class DiscoverPackageCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command('open_url', {'url': 'http://sindresorhus.com/bower-components'})