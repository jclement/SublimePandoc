# Pandoc Plugin for Sublime Text 2 #

A Sublime Text 2 plugin for calling the Pandoc Markdown renderer to create HTML and DocX output.

## Dependencies ##

You'll need to download and install [Pandoc] and have it in your PATH.

## Sample Keybindings ##
~~~~~ {#mycode .python .numberLines startFrom="100"}
[
	{"keys": ["ctrl+alt+r"], "command":"pandoc_render", "args":{"openInBrowser":true}},
	{"keys": ["ctrl+alt+shift+d"], "command":"pandoc_render_docx"},
	{"keys": ["ctrl+alt+shift+r"], "command":"pandoc_render", "args":{"openInBrowser":false, "writeBeside":true}}
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

[Pandoc]: http://johnmacfarlane.net/pandoc/