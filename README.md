# Pandoc Plugin for Sublime Text 2 #

A [Sublime Text 2](http://www.sublimetext.com/2) plugin for calling the Pandoc Markdown renderer to create HTML and DocX output.  Pandoc does a LOT more than this but this is the specific functionality I use.

## Installation ##

The easiest way is to install "SublimePandoc" using [Package Control](http://wbond.net/sublime_packages/package_control).

You can also grab the latest from Github and install it into your Sublime Text 2 Packages folder.

~~~~~~~~~~~~~ {#mycode .sh}
$ git clone git://github.com/jclement/SublimePandoc.git
~~~~~~~~~~~~~~~~~~~~~~

## Dependencies ##

You'll need to download and install [Pandoc] and have it in your PATH.

## Available Commands ##

**pandoc_render** will render the markdown to HTML or DOCx and takes the following optional arguments:

*	**writeBeside** - When set will output the rendered result in the same folder, and with the same name as the source file.  This requires that the buffer has already been saved and has a filename.  Defaults to FALSE.
*	**openAfter** - When set will open the resulting document after rendering it.  Defaults to FALSE.
*	**target** - Can be either 'html' or 'docx'.  Defaults to 'html'.
* **additionalArguments** - A list of additional arguments to pass to Pandoc.

Menu items for common tasks should show up under Tools > Pandoc.

## Output Hints ##

The following hints can be added in your document to flip on additional features in Pandoc.  (Note: these hints are processed by the plugin and NOT part of Pandoc itself)

**\<!-- \[\[TOC]] -->**: Add a Table of Contents to the top of your output document.

**\<!-- \[\[NUM]] -->**: Turn on numbering of sections.

## Templates ##

"template.html" controls the output of the HTML documents and "reference.docx" is used for style definitions for DOCX output. 

**Note**:  If you are using a pre-built binary of Pandoc you will be unable to customize the reference.docx using Microsoft Word in versions <= 1.9.1

## Sample Keybindings ##

The default keymapping on Windows...

~~~~~ {#mycode .python .numberLines startFrom="100"}
[
  { "keys": ["ctrl+alt+r"],     
    "command":"pandoc_render", 
    "args":{"openAfter":true,   "target":"html",  "writeBeside":false},
    "context":[{"key": "selector", "operator": "equal", "operand": "text.html.markdown" }]},

  { "keys": ["ctrl+alt+shift+d"],   
    "command":"pandoc_render", 
    "args":{"openAfter":true,   "target":"docx",  "writeBeside":true},
    "context":[{"key": "selector", "operator": "equal", "operand": "text.html.markdown" }]},

  { "keys": ["ctrl+alt+shift+r"],   
    "command":"pandoc_render", 
    "args":{"openAfter":false,  "target":"html",  "writeBeside":true},
    "context":[{"key": "selector", "operator": "equal", "operand": "text.html.markdown" }]}
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

[Pandoc]: http://johnmacfarlane.net/pandoc/