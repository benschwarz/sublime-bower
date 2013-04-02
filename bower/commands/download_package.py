import sublime
import sublime_plugin
import threading
import sys
from bower.utils.download import Download

class DownloadPackageCommand(sublime_plugin.TextCommand):
    result = None
    pkg_name = None

    def run(self, edit, pkg_name, cwd):
        self.edit = edit
        self.pkg_name = pkg_name
        self.cwd = cwd
        
        threads = []
        thread = Download(pkg_name, cwd)
        threads.append(thread)
        thread.start()
        self.handle_threads(edit, threads)

    def handle_threads(self, edit, threads, offset=0, i=0, dir=1):
        status = None
        next_threads = []
        for thread in threads:
            status = thread.result
            txt = thread.txt
            if thread.is_alive():
                next_threads.append(thread)
                continue
            if thread.result == False:
                continue

        threads = next_threads

        if len(threads):
            # This animates a little activity indicator in the status area
            before = i % 8
            after = (7) - before

            if not after:
                dir = -1
            if not before:
                dir = 1

            i += dir
            sublime.status_message(('Downloading %s [%s=%s]') % (self.pkg_name, ' ' * before, ' ' * after)) 

            sublime.set_timeout(lambda: self.handle_threads(edit, threads, offset, i, dir), 100)
            return

        if status:
            sublime.status_message(('Bower: installed %s') % self.pkg_name)