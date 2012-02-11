# Pandoc Plugin for Sublime Text 2 #

A [Sublime Text 2](http://www.sublimetext.com/2) plugin for calling the Pandoc Markdown renderer to create HTML and DocX output.

## Installation ##

The easiest way is to run the following from your Sublime Text 2 Packages folder.

~~~~~~~~~~~~~ {#mycode .sh}
$ git clone git://github.com/jclement/SublimePandoc.git
~~~~~~~~~~~~~~~~~~~~~~

## Dependencies ##

You'll need to download and install [Pandoc] and have it in your PATH.

## Available Commands ##

**pandoc_render** will render the markdown to HTML or DOCx and takes the following optional arguments:

writeBeside
  ~ When set will output the rendered result in the same folder, and with the same name as the source file.  This requires that the buffer has already been saved and has a filename.  Defaults to FALSE.
openAfter
  ~ When set will open the resulting document after rendering it.  Defaults to FALSE.
target
  ~ Can be either 'html' or 'docx'.  Defaults to 'html'.


## Templates ##

## Sample Keybindings ##
~~~~~ {#mycode .python .numberLines startFrom="100"}
[
	{"keys": ["ctrl+alt+r"], 		"command":"pandoc_render", "args":{"openAfter":true, 	"target":"html", 	"writeBeside":false}},
	{"keys": ["ctrl+alt+shift+d"], 	"command":"pandoc_render", "args":{"openAfter":false, 	"target":"docx",	"writeBeside":true}},
	{"keys": ["ctrl+alt+shift+r"], 	"command":"pandoc_render", "args":{"openAfter":false, 	"target":"html", 	"writeBeside":true}}
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

[Pandoc]: http://johnmacfarlane.net/pandoc/	