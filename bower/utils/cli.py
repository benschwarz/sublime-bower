import sublime
import os
import subprocess
from bower.exceptions.non_clean_exit_error import NonCleanExitError

if os.name == 'nt':
    LOCAL_PATH = ''
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
