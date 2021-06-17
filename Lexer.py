import re
import sys

def lex(characters):
    pos = 0
    tokens = []
    while pos < len(characters):
        for token_expr in token_exprs:
            pattern, tag, priority = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match[0]
                if tag:
                    token = (text, tag, priority)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: %s\n' % characters[pos])
            sys.exit(1)
        else:
            pos = match.end()
    return tokens

token_exprs = [
    (r'[ \t\n]+', None, None),
    (r'#[^\n]*', None, None),
    (r'if', 'IF_KEYWORD', None),
    (r'else', 'ELSE_KEYWORD', None),
    (r'while', 'WHILE_KEYWORD', None),
    (r'do', 'DO_KEYWORD', None),
    (r'LinkedList', 'LINKED_LIST_KEYWORD',0),
    (r';', 'CLOSE', None),
    (r'(==)|(<=)|(>=)|(!=)|>|<|(&&)|(\|\|)', 'LOGICAL_OP', 0),
    (r'=', 'ASSIGN', 0),
    (r'\(', 'LP', None),
    (r'\)', 'RP', None),
    (r'\{', 'LB', None),
    (r'\}', 'RB', None),
    (r',', 'COMMA', None),
    (r'\.', 'POINT', None),
    (r'-?0|(-?[1-9][0-9]*)', 'INT', None),
    (r'[\+]', 'PLUS', 1),
    (r'[\-]', 'MINUS', 1),
    (r'[\*]', 'MULTI', 2),
    (r'[\/]', 'DIV', 2),
    (r'[A-Za-z_][A-Za-z0-9_]*', 'VAR', None),
]