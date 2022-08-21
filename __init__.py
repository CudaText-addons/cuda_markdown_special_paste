import os
from cudatext import *
import cudatext_cmd as cmds

FORMATS = {
    'Markdown': '[Text]({url})',
    'reStructuredText': '`Text <{url}>`__',
}

class Command:
    
    def on_paste(self, ed_self, keep_caret, select_then):
        s = app_proc(PROC_GET_CLIP, '')
        if '\n' in s:
            return
        if not s.startswith('http://') and not s.startswith('https://'):
            return
        lex = ed.get_prop(PROP_LEXER_FILE)
        fmt = FORMATS.get(lex)
        if not fmt:
            return
        fmt = fmt.replace('{url}', s)
        ed.cmd(cmds.cCommand_TextInsert, fmt)
        return False
