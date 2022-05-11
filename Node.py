class Node(object):
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def search(self, data):
        if data == self.data:
            print("{} in tree".format(data))
            return True
        if data < self.data:
            if self.left is None:
                print("{} not in tree".format(data))
                return False
            return self.left.search(data)
        if self.right is None:
            print("{} not in tree".format(data))
            return False
        return self.right.search(data)


    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


a = [4, 5, 1, 3, 2, 8, 0]
for i in range(len(a)):
    if i == 0:
        root = Node(a[i])
    else:
        root.insert(a[i])
root.print_tree()