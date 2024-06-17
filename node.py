class Node:
    def __init__(self, type, children=None, token=None):
        self.type = type
        self.children = children if children is not None else []
        self.token = token

    def __repr__(self):
        return f"Node({self.type}, {self.children}, {self.token})"