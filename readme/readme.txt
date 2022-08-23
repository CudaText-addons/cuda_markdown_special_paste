plugin for CudaText.
it handles "on_paste" event for lexers:
- Markdown
- reStructuredText
- MediaWiki

1) if clipboard contains text URL: 'http://' or 'https://'.
it changes pasted text according to these templates:

- for Markdown: [Text](url)
- for reStructuredText: `Text <url>`__
- for MediaWiki: [url Text]

2) if clipboard contains a picture. plugin then suggests to save the picture
in the folder of the current file, and after that it inserts the link to this
new file.

- for Markdown: '![alt text](filename.png "Title")
- for reStructuredText: .. image:: filename.png
- for MediaWiki: [[File:filename.png]]


how to temporary skip plugin work? call the Paste command with any hotkey containing
'Shift+' (or call menu item Paste while holding Shift).
eg with Shift+Insert - standard second hotkey for Paste. or with Ctrl+Shift+V,
but first you need to assign Ctrl+Shift+V to "Paste" (in the Command Palette dialog).
 

author: Alexey Torgashin
license: MIT
