# Sublime JS2Coffee
A quick way to convert an existing JS file (or an unsaved buffer with Javascript in it) to Coffeescript from Sublime Text.


## Installation

* Install [node](http://nodejs.org/) and [npm](https://npmjs.org/)
* Install js2coffee and coffee-script: `npm install -g js2coffee coffee-script`

then, either

* Install [Package Control](http://wbond.net/sublime_packages/package_control) if you don't already have it.
* `cmd-shift-p` Package Control: Install Package -> JS2Coffee

or

* Clone this repo into your `Packages` directory (**Not Recommended:** cloning will not allow you to update automatically).


## Usage
 
`cmd-shift-p` JS2Coffee: 

![image](http://f.cl.ly/items/3B1l2H2K0U3r2U1E0f0U/test.js%20%E2%80%94%20sublime-js2coffee-1.jpg)

The syntax will be automatically set to CoffeeScript, and either the current file will be replaced with the CoffeeScript convertion, or a new file will be opened containing the conversion (depending on the command you used).

![image](http://f.cl.ly/items/3P3z0Z0r2K1C3c2V1r3a/untitled%20%E2%80%94%20sublime-js2coffee-2.jpg)


## Bind a Key to `js_coffee`
**Note:** Out of courtesy, there is no keyboard shortcut set by default.

In `Packages/User/Default (`your OS`).sublime-keymap` add one of the following lines:

* `{ "keys": ["ctrl+shift+j"], "command": "js_coffee", "args":{"new_file": true}}`

or

* `{ "keys": ["ctrl+shift+j"], "command": "js_coffee", "args":{"new_file": false}}`


## Troubleshooting

If `js2coffee` outputs an error message it will show up in Sublime Text's console. There is not always useful context information in these messages, so YMMV.
