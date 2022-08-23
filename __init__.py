import os
from cudatext import *
import cudatext_cmd as cmds
import requests
import html

GET_TIMEOUT = 5 # in seconds

FORMAT_URL = {
    'Markdown': '[{title}]({url})',
    'reStructuredText': '`{title} <{url}>`__',
    'MediaWiki': '[{url} {title}]',
}

FORMAT_PIC = {
    'Markdown': '![alt text]({filename} "Title")',
    'reStructuredText': '\n.. image:: {filename}',
    'MediaWiki': '\n[[File:{filename}]]',
}

def dbg(s):
    #print(s)
    pass

def get_title(s, tag):
    n = s.find('<'+tag+'>')
    if n<0:
        dbg('no <title>: '+s)
        return
    s = s[n+len(tag)+2:]
    n = s.find('</'+tag+'>')
    if n<0:
        dbg('no </title>: '+s)
        return
    s = s[:n]
    return html.unescape(s)


class Command:

    def on_paste(self, ed_self, keep_caret, select_then):

        # Shift pressed? don't work
        state = app_proc(PROC_GET_KEYSTATE, '')
        if 's' in state:
            return

        fmt = app_proc(PROC_CLIP_ENUM, '')
        if 'p' in fmt:
            self.paste_pic()
            return False # block usual Paste

        if 't' in fmt:
            return self.paste_text()

    def paste_pic(self):

        fn_ed = ed.get_filename()
        if not fn_ed:
            msg_status('Cannot paste picture in the untitled tab')
            return

        while True:
            s = dlg_input('Clipboard contains some picture.\nSave it to filename in the current folder (without ".png"):', 'temp_picture')
            if not s:
                return
            if not s.endswith('.png'):
                s += '.png'

            fn = os.path.dirname(fn_ed)+os.sep+s
            if os.path.exists(fn):
                msg_status('File already exists: '+fn)
            else:
                break

        if not app_proc(PROC_CLIP_SAVE_PIC, fn):
            msg_status('Cannot save clipboard to file: '+fn)
            return

        lex = ed.get_prop(PROP_LEXER_FILE)
        text = FORMAT_PIC.get(lex)
        if not text:
            return

        text = text.replace('{filename}', os.path.basename(fn))
        ed.cmd(cmds.cCommand_TextInsert, text)


    def paste_text(self):

        s = app_proc(PROC_GET_CLIP, '')
        if '\n' in s:
            return
        if not s.startswith('http://') and not s.startswith('https://'):
            return

        try:
            r = requests.get(s, verify=False, timeout=GET_TIMEOUT)
        except:
            return

        if not r:
            return
        text = r.content.decode('utf-8', errors='replace')
        if not text:
            return

        title = get_title(text, 'title') or get_title(text, 'TITLE') or 'Title'

        lex = ed.get_prop(PROP_LEXER_CARET)
        fmt = FORMAT_URL.get(lex)
        if not fmt:
            return
        fmt = fmt.replace('{url}', s)
        fmt = fmt.replace('{title}', title)

        ed.cmd(cmds.cCommand_TextInsert, fmt)
        return False #block usual Paste
