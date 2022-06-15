

class Node():
    """Node in a tree."""

    def __init__(self, data, children):
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Node {self.data}>"

    def find(self, data):
        """Return node object with this data.

        Start here. Return None if not found.
        """

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                return current

            to_visit.extend(current.children)


class Tree():
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Tree root={self.root}>"

    def find_in_tree(self, data):
        """Return node object with this data.

        Start at root.
        Return None if not found.
        """

        return self.root.find(data)

# Part 3:
# A Method that returns the total number of nodes that are present in a given tree:
    def total_nodes(self):

        def num_child_nodes(node, current_total):
            inner_nodes = current_total

            for child in node.children:
                inner_nodes += 1
                inner_nodes = num_child_nodes(child, inner_nodes)

            return inner_nodes

        return num_child_nodes(self.root, 0)            


# Part 2:
# A function that takes in two arguments– (1) the name of a CEO, as a string and (2) a list of the CEO’s direct reports, as a list of strings. 
def make_tree(ceo: str, directly_below: list):
    root = Node(ceo, directly_below)

    tree = Tree(root)
    return tree


if __name__ == "__main__":
    resume = Node("resume.txt", [])
    recipes = Node("recipes.txt", [])
    jane = Node("jane/", [resume, recipes])
    server = Node("server.py", [])
    jessica = Node("jessica/", [server])
    users = Node("Users/", [jane, jessica])
    root = Node("/", [users])

    tree = Tree(root)

    print(f"Total Nodes: {tree.total_nodes()}")