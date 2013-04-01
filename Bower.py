import sublime
import sublime_plugin
import os
import sys
import threading
import re
import subprocess

# Internal
from bower.api import API

if os.name == 'nt':
    LOCAL_PATH = ''
    BINARY_NAME = 'bower.cmd'
else:
    LOCAL_PATH = ':/usr/local/bin:/usr/local/sbin:/usr/local/share/npm/bin'
    BINARY_NAME = 'bower'

os.environ['PATH'] += LOCAL_PATH

class DiscoverPackageCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command('open_url', {'url': 'http://sindresorhus.com/bower-components'})

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
            self.window.run_command("bower_get", {"pkg_name": name, "cwd": cwd})


class BowerGetCommand(sublime_plugin.TextCommand):
    result = None
    pkg_name = None

    def run(self, edit, pkg_name, cwd):
        self.edit = edit
        self.pkg_name = pkg_name
        self.cwd = cwd
        
        threads = []
        thread = BowerDownload(pkg_name, cwd)
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

class BowerDownload(threading.Thread):
    def __init__(self, pkg_name, cwd):
        self.pkg_name = pkg_name
        self.txt = None
        self.cwd = cwd

        # Defaults
        self.result = None
        threading.Thread.__init__(self)

    def run(self):
        self.install_package()

    def install_package(self):
        cli = BowerCLI()
        command = ['install', self.pkg_name, '--save']
        cli.execute(command, cwd=self.cwd)

class NonCleanExitError(Exception):
    def __init__(self, returncode):
        self.returncode = returncode

    def __str__(self):
        return repr(self.returncode)


class BowerCLI():
    def find_binary(self):
        for dir in os.environ['PATH'].split(os.pathsep):
            path = os.path.join(dir, BINARY_NAME)
            if os.path.exists(path):
                return path
        sublime.error_message(BINARY_NAME + ' could not be found in your $PATH. Install bower with `npm install bower -g`')

    def execute(self, command, cwd):
        binary = self.find_binary()
        command.insert(0, binary)

        proc = subprocess.Popen(command, cwd=cwd, stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        output = proc.stdout.read()
        returncode = proc.wait()
        if returncode != 0:
            error = NonCleanExitError(returncode)
            error.output = output
            raise error
        return output
