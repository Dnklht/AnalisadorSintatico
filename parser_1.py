from node import Node
from token_1 import Token

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        return self.parse_statement()

    def parse_statement(self):
        id_node = self.match("ID")
        self.match("OP", "=")
        expr = self.parse_expression()
        self.match("SEMICOLON")
        return Node("AssignStmt", [id_node, expr])

    def parse_expression(self):
        term = self.parse_term()
        return term

    def parse_term(self):
        token = self.tokens[self.pos]
        if token.type == "INTEGER":
            return self.match("INTEGER")
        elif token.type == "ID":
            return self.match("ID")
        else:
            self.error()

    def match(self, expected_type, expected_value=None):
        token = self.tokens[self.pos]
        if token.type != expected_type or (expected_value and token.value != expected_value):
            self.error()
        self.pos += 1
        return Node(token.type, token=token)

    def error(self):
        raise Exception(f"Syntax error at token {self.tokens[self.pos]}")