plugin for CudaText.
it handles on_paste event for lexers: Markdown, reStructuredText;
but only if clipboard contains 'http://' or 'https://' URL.
it changes pasted text according to these templates:

- for Markdown: [Text](url)
- for reStructuredText: `Text <url>`__

how to temporary skip plugin work? call the Paste command with any hotkey containing
'Shift+' (or call menu item Paste while holding Shift).
eg with Shift+Insert - standard second hotkey for Paste. or with Ctrl+Shift+V,
but first you need to assign Ctrl+Shift+V to "Paste" (in the Command Palette dialog).
 

author: Alexey Torgashin
license: MIT
