from queue import Queue

class Node(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    @staticmethod
    def create_tree(values):
        node = None
        root = None
        values_stack = values[::-1]
        node_queue = Queue()

        while len(values_stack) > 0:
            val = values_stack.pop()
            new_node = Node(val)
            if node is None:
                node, root = new_node, new_node
            elif node.left is None:
                node.left = new_node
                node_queue.put(new_node)
            elif node.right is None:
                node.right = new_node
                node_queue.put(new_node)
            else:
                values_stack.append(val)
                node = node_queue.get()
    
        return root
    
    @staticmethod
    def print_tree_df(tree):
        node_stack = [tree]
        while len(node_stack) > 0:
            node = node_stack.pop()
            print(node.val)
            if node.right is not None:
                node_stack.append(node.right)
            if node.left is not None:
                node_stack.append(node.left)


def load_data(filename):
    file, data = open(filename, 'r'), []
    for line in file:
        data = line.split(',')
    return data

if __name__ == '__main__':
    data = load_data('./values.txt')
    tree = Node.create_tree(data)
    Node.print_tree_df(tree)