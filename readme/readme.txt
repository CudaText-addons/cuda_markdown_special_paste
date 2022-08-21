plugin for CudaText.
it handles on_paste event for lexers: Markdown, reStructuredText;
but only if clipboard contains 'http://' or 'https://' URL.
it changes pasted text according to these templates:

for Markdown: [Text](url)
for reStructuredText: `Text <url>`__

author: Alexey Torgashin
license: MIT
