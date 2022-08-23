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


how to temporary skip plugin work?
----------------------------------

call the Paste command with any hotkey containing 'Shift'
(or call menu item Paste while holding Shift).
e.g. use Shift+Insert (standard second hotkey for Paste).
or use Ctrl+Shift+V, but first you need to assign Ctrl+Shift+V to "Paste"
(in the Command Palette dialog).


options
-------

config file "plugins.ini" can be opened via menu item:
  "Options / Settings-plugins / Markdown Special Paste / Config".

options in section [markdown_special_paste] are:
- url_timeout - Timeout in seconds, which it used on downloading webpage by its URL.
- pic_name - Initial suggested name for picture file. Can have macros:
    {now} - Current date/time formatted as yyyy-mm-dd-hh-mm-ss.
- pic_path - Initial folder for picture file, when pasting picture. Can have macros:
    {filedir} - Folder of current editor file.
    {projdir} - Folder of currently opened CudaText project.
                If no project is opened, it's folder of current editor file.
 

author: Alexey Torgashin
license: MIT
