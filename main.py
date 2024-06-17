from lexer import tokenize
from parser_1 import Parser

def main():
    code = "a = 10;"
    tokens = tokenize(code)
    for token in tokens:
        print(token)

    parser = Parser(tokens)
    tree = parser.parse()
    print(tree)

if __name__ == "__main__":
    main()