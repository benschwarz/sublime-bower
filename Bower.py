import sublime
import sublime_plugin
import os
import sys
import threading
import re
import subprocess
import urllib2
import json
import gzip
from StringIO import StringIO

LOCAL_PATH = ':/usr/local/bin:/usr/local/sbin:'
os.environ['PATH'] += LOCAL_PATH 

class DiscoverPackageCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command('open_url', {'url': 'http://sindresorhus.com/bower-components'})

class InstallCommand(sublime_plugin.WindowCommand):
    fileList = []

    def run(self, *args, **kwargs):
        self.list_packages()

    def list_packages(self):
        uri = "http://bower.herokuapp.com/packages"
        request = urllib2.Request(uri)
        request.add_header('Accept-encoding', 'gzip')

        try:
            response = urllib2.urlopen(request)

            if response.info().get('Content-Encoding') == 'gzip':
                buf = StringIO( response.read() )
                f = gzip.GzipFile(fileobj=buf)
                responseText = f.read()           
            else:
                responseText = response.read()
            
            packages = json.loads(responseText)
            packages.reverse()

            for package in packages:
                self.fileList.append([package['name'], package['url']])
            self.window.show_quick_panel(self.fileList, self.get_file)
        except:
            sublime.error_message('Unable to connect to ' + uri + ". Check your internet connection.")

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
        clidownload = CliDownloader()
        
        if clidownload.find_binary('bower'):
            command = [clidownload.find_binary('bower'), 'install', self.pkg_name, '--save']
            clidownload.execute(command, cwd=self.cwd)

class NonCleanExitError(Exception):
    def __init__(self, returncode):
        self.returncode = returncode

    def __str__(self):
        return repr(self.returncode)


class CliDownloader():
    def find_binary(self, name):
        for dir in os.environ['PATH'].split(os.pathsep):
            path = os.path.join(dir, name)
            if os.path.exists(path):
                return path
        sublime.error_message('Bower could not be found in your $PATH. Install bower with `npm install bower -g`')

    def execute(self, command, cwd):
        proc = subprocess.Popen(command, cwd=cwd, stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        output = proc.stdout.read()
        returncode = proc.wait()
        if returncode != 0:
            error = NonCleanExitError(returncode)
            error.output = output
            raise error
        return output
