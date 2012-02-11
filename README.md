% Pandoc Plugin for Sublime Text 2
% Jeff Clement

A Sublime Text 2 plugin for calling the Pandoc Markdown renderer to create HTML and DocX output.

## Dependencies ##

You'll need to download and install [Pandoc] and have it in your PATH.

## Available Commands ##

**pandoc_render** will render the markdown to HTML.  If argument "openInBrowser" is set to true it will open the rendered document as soon as it's done.   If "writeBeside" is true the HTML is output in the same folder as the markdown source file but with a .html extension.

**pandoc_render_docx** will render the markdown to a DOCX file in the same folder as the markdown source file.

## Templates ##

## Sample Keybindings ##
~~~~~ {#mycode .python .numberLines startFrom="100"}
[
	{"keys": ["ctrl+alt+r"], "command":"pandoc_render", "args":{"openInBrowser":true}},
	{"keys": ["ctrl+alt+shift+d"], "command":"pandoc_render_docx"},
	{"keys": ["ctrl+alt+shift+r"], "command":"pandoc_render", "args":{"openInBrowser":false, "writeBeside":true}}
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

[Pandoc]: http://johnmacfarlane.net/pandoc/