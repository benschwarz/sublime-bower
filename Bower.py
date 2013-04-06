import sublime
import sublime_plugin

#Internal
try:
    # ST3
    from .bower.commands.discover import DiscoverPackageCommand
    from .bower.commands.install import InstallCommand
    from .bower.commands.download_package import DownloadPackageCommand
    from .bower.commands.bowerrc import BowerrcCommand
except (ImportError, ValueError):
    # ST2
    from bower.commands.discover import DiscoverPackageCommand
    from bower.commands.install import InstallCommand
    from bower.commands.download_package import DownloadPackageCommand
    from bower.commands.bowerrc import BowerrcCommand
