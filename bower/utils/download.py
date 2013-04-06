from threading import Thread

try:
    # ST3
    from ..utils.cli import CLI
except ImportError:
    # ST2
    from bower.utils.cli import CLI


class Download(Thread):
    def __init__(self, pkg_name, cwd):
        self.pkg_name = pkg_name
        self.txt = None
        self.cwd = cwd

        # Defaults
        self.result = None
        Thread.__init__(self)

    def run(self):
        self.install_package()

    def install_package(self):
        command = ['install', self.pkg_name, '--save']
        CLI().execute(command, cwd=self.cwd)
