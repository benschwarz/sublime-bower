# Bower, for Sublime Text

This is a plugin for Sublime text, it will allow you to install packages via [Twitter's Bower tool](http://twitter.github.com/bower/).

Want to learn about the available packages? Check [Bower components](http://sindresorhus.com/bower-components/) 

## How to use

Run the command "Bower install" to get a list of packages from the canonical bower repository.

Packages will be installed the current working directory. 

![Demo of plugin in action](http://0.germanforblack.com/sublime-plugin.gif)

## Installation

Sublime Package Control allows you to easily install or remove sublime-bower (and many other packages) from within the editor. It offers automatically updating packages as well so you no longer need to keep track of changes in sublime-bower.

Install Sublime Package Control (if you haven't done so already) from http://wbond.net/sublime_packages/package_control

Bring up the command palette (default ctrl+shift+p or cmd+shift+p) and start typing Package Control: Install Package then press return or click on that option to activate it. You will be presented with a new Quick Panel with the list of available packages. (Search for "Bower")

Alternately, you can manually install it: (In your Terminal)

```bash
  cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
  git clone git://github.com/benschwarz/sublime-bower.git Bower
```

## Requirements

* Have bower installed: `npm install bower -g`
* Have the bower binary in your path

Its a good idea to do a test run to make sure that bower is working - if `bower install jquery` works, then you're ready to go.

## Testing / platforms

* Untested on Sublime Text v3 (Let me know)

#### PSA
This is my first attempt at writing a ST plugin… I don't write python either, so if you think you can help, lemme know. k? word.

## Contributing

* Check the [issue list](https://github.com/benschwarz/sublime-bower/issues) to find something to help with
* Add any implementation queries, ideas or psudeo code
* Fork the project, work in a topic branch
* Send a pull request
* You the boss now, dawg