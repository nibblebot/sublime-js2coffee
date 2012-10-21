# Sublime JS2Coffee
A quick way to convert an existing JS file (or an unsaved buffer with Javascript in it) to Coffeescript from Sublime Text.


## Installation

* Install [Package Control](http://wbond.net/sublime_packages/package_control)
OR
* clone this repo to your Packages directory

* Install node, npm
* `npm install -g js2coffee coffee-script`
* `cmd-shift-p` Package Control: Install Package -> JS2Coffee


## Usage





 ![image](http://f.cl.ly/items/2f3Y3X070D1v0Q123Y35/test.js%20%E2%80%94%20sublime-js2coffee.jpg)
 
* `cmd-shift-p` JS2Coffee 

* OR

* Bind a key to `js_coffee` (e.g. in <Packages>/User/Default (OSX).sublime-keymap) (**Note: there is no keyboard shortcut set by default out of courtesy**):
`{ "keys": ["ctrl+shift+j"], "command": "js_coffee"}`

![image](http://f.cl.ly/items/2E192C1r3C443o2k3S3Q/untitled%20%E2%80%94%20sublime-js2coffee-1.jpg)

* A new buffer will open with the Command Palette preset to Set Syntax to CoffeeScript (You will have to hit Enter here to set the syntax).

 ![image](http://f.cl.ly/items/3S011V12233C2D1D2N20/untitled%20%E2%80%94%20sublime-js2coffee.jpg)


## Troubleshooting

If `js2coffee` outputs an error message it will show up in Sublime Text's console. There is not always useful context information in these messages, so YMMV.
