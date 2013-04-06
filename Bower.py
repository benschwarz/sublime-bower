import sublime
import sublime_plugin

#Internal
try:
	# ST3
	from Bower.bower.commands.discover import DiscoverPackageCommand
	from Bower.bower.commands.install import InstallCommand
	from Bower.bower.commands.download_package import DownloadPackageCommand
	from Bower.bower.commands.bowerrc import BowerrcCommand

except ImportError:
	# ST2
	from bower.commands.discover import DiscoverPackageCommand
	from bower.commands.install import InstallCommand
	from bower.commands.download_package import DownloadPackageCommand
	from bower.commands.bowerrc import BowerrcCommand
