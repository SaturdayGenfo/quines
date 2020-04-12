def escape(s):
    x = ''
    for c in s:
        if c == '\n':
            x += '\\n'
        elif c == '\\':
            x += '\\\\'
        else:
            x+= c
    return x
s = "def escape(s):\n    x = ''\n    for c in s:\n        if c == '\\n':\n            x += '\\\\n'\n        elif c == '\\\\':\n            x+='\\\\\\\\'\n        else:\n            x+= c\n    return x\ns = \"\"\nprint(s[:-38] + escape(s) + s[-38:])"
print(s[:-38] + escape(s) + s[-38:])