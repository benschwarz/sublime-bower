import sublime
import os
import subprocess

try:
    # ST3
    from ..exceptions.non_clean_exit_error import NonCleanExitError
except ImportError:
    # ST2
    from bower.exceptions.non_clean_exit_error import NonCleanExitError

if os.name == 'nt':
    LOCAL_PATH = ';' + os.getenv('APPDATA') + '\\npm'
    BINARY_NAME = 'bower.cmd'
else:
    LOCAL_PATH = ':/usr/local/bin:/usr/local/sbin:/usr/local/share/npm/bin'
    BINARY_NAME = 'bower'

os.environ['PATH'] += LOCAL_PATH


class CLI():
    def find_binary(self):
        for dir in os.environ['PATH'].split(os.pathsep):
            path = os.path.join(dir, BINARY_NAME)
            if os.path.exists(path):
                return path
        sublime.error_message(BINARY_NAME + ' could not be found in your $PATH. Check the installation guidelines - https://github.com/benschwarz/sublime-bower#installation')

    def execute(self, command, cwd):
        binary = self.find_binary()
        command.insert(0, binary)

        cflags = 0

        if os.name == 'nt':
            cflags = 0x08000000  # Avoid opening of a cmd on Windows

        proc = subprocess.Popen(command, cwd=cwd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, creationflags=cflags)

        output = proc.stdout.read()
        returncode = proc.wait()
        if returncode != 0:
            error = NonCleanExitError(returncode)
            error.output = output
            raise error
        return output
