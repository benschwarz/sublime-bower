# Bower, for Sublime Text

This is a plugin for Sublime text, it will allow you to install packages via [Twitter's Bower tool](http://twitter.github.com/bower/).

Want to learn about the available packages? Check [Bower components](http://sindresorhus.com/bower-components/) 

## How to use

Run the command "Bower install" to get a list of packages from the canonical bower repository.
Packages will be installed the current working directory. 

Want to know more about Bower, or this plugin in action? [Checkout my screencast.](http://germanforblack.com/post/46734908388/i-built-a-plugin-for-sublime-text-that-integrates) 

## Installation

* Install bower using NPM: `npm install bower -g`
* Ensure that the bower binary is available in your path (type `bower` into your Terminal / Command prompt)
* [Install msysgit](https://github.com/twitter/bower#a-note-for-windows-users) (Windows only)

Sublime Package Control allows you to easily install or remove sublime-bower (and many other packages) from within the editor. It offers automatically updating packages as well so you no longer need to keep track of changes in sublime-bower.

* Install Sublime Package Control (if you haven't done so already) from http://wbond.net/sublime_packages/package_control

* Bring up the command palette (default ctrl+shift+p or cmd+shift+p) and start typing Package Control: Install Package then press return or click on that option to activate it. You will be presented with a new Quick Panel with the list of available packages. (Search for "Bower")

Alternately, instead of using Package Control, you can manually install sublime-bower (be aware, you'll have to fetch updates yourself):

On Mac OS X, in your Terminal:

```bash
  cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
  git clone git://github.com/benschwarz/sublime-bower.git Bower
```

On Windows, inside a command prompt (cmd.exe):

```cmd
  cd "%APPDATA%\Sublime Text 2\Packages"
  git clone git://github.com/benschwarz/sublime-bower.git Bower
```

## Platforms

* Works on Sublime text 2 & 3
* Works on Mac, Linux & Windows

## Contributing

* Check the [issue list](https://github.com/benschwarz/sublime-bower/issues) to find something to help with
* Add any implementation queries, ideas or psudeo code
* Fork the project, work in a topic branch
* Send a pull request
* You the boss now, dawg

## Contributors
* [@eonlepapillon](http://github.com/eonlepapillon) - ST3 support
* [@moonpyk](http://github.com/moonpyk) - Windows support
* [@sindresorhus](http://github.com/sindresorhus) - Bower support
* [@jaredwy](http://github.com/jaredwy) - Incredible autocompletions… not in master (yet)

## Licence

[Licenced MIT.](LICENCE)
