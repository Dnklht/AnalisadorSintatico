import re
from token_1 import Token

def tokenize(code):
    TOKEN_PATTERNS = re.compile(
        "(?P<INTEGER>\\d+)|"
        "(?P<REAL>\\d+\\.\\d+)|"
        "(?P<ID>[A-Za-z_][A-Za-z0-9_]*)|"
        "(?P<STRING>\"(\\\\\"|[^\"])*\")|"
        "(?P<CHAR>'(\\\\[nrt'\"\\\\]|[^'\\\\])')|"
        "(?P<OP>[-+*/=<>!&|%^~?:]+)|"
        "(?P<LPAREN>\\()|"
        "(?P<RPAREN>\\))|"
        "(?P<LBRACE>\\{)|"
        "(?P<RBRACE>\\})|"
        "(?P<LSQUARE>\\[)|"
        "(?P<RSQUARE>\\])|"
        "(?P<SEMICOLON>;)|"
        "(?P<COLON>:)|"
        "(?P<COMMA>,)|"
        "(?P<DOT>\\.)|"
        "(?P<WHITESPACE>[ \t]+)|"
        "(?P<NEWLINE>\\n)|"
        "(?P<COMMENT>/\\*.*?\\*/|//.*?\\n)|"
        "(?P<MISMATCH>.)"
    )

    line_no = 1
    current_pos = 0
    tokens = []
    matcher = TOKEN_PATTERNS.finditer(code)

    for match in matcher:
        if match.group("NEWLINE"):
            line_no += 1
            current_pos = match.end()
        elif match.group("WHITESPACE") or match.group("COMMENT"):
            current_pos = match.end()
        elif match.group("INTEGER"):
            tokens.append(Token("INTEGER", match.group("INTEGER"), line_no))
        elif match.group("REAL"):
            tokens.append(Token("REAL", match.group("REAL"), line_no))
        elif match.group("ID"):
            tokens.append(Token("ID", match.group("ID"), line_no))
        elif match.group("STRING"):
            tokens.append(Token("STRING", match.group("STRING"), line_no))
        elif match.group("CHAR"):
            tokens.append(Token("CHAR", match.group("CHAR"), line_no))
        elif match.group("OP"):
            tokens.append(Token("OP", match.group("OP"), line_no))
        elif match.group("LPAREN"):
            tokens.append(Token("LPAREN", match.group("LPAREN"), line_no))
        elif match.group("RPAREN"):
            tokens.append(Token("RPAREN", match.group("RPAREN"), line_no))
        elif match.group("LBRACE"):
            tokens.append(Token("LBRACE", match.group("LBRACE"), line_no))
        elif match.group("RBRACE"):
            tokens.append(Token("RBRACE", match.group("RBRACE"), line_no))
        elif match.group("LSQUARE"):
            tokens.append(Token("LSQUARE", match.group("LSQUARE"), line_no))
        elif match.group("RSQUARE"):
            tokens.append(Token("RSQUARE", match.group("RSQUARE"), line_no))
        elif match.group("SEMICOLON"):
            tokens.append(Token("SEMICOLON", match.group("SEMICOLON"), line_no))
        elif match.group("COLON"):
            tokens.append(Token("COLON", match.group("COLON"), line_no))
        elif match.group("COMMA"):
            tokens.append(Token("COMMA", match.group("COMMA"), line_no))
        elif match.group("DOT"):
            tokens.append(Token("DOT", match.group("DOT"), line_no))
        elif match.group("MISMATCH"):
            raise RuntimeError(f"Unexpected character: {match.group('MISMATCH')} at line {line_no}")

    return tokens