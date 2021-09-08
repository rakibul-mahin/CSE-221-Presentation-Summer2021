class Tree:
    #This is how each node will look like.
    #Value, Left Child and Right Child
    def __init__(self, root_value = None):
        self.left_child = None
        self.right_child = None
        self.data = root_value

    #This will add children to a node    
    def add_children(self, value):
        if self.data:
            if value < self.data:
                if self.left_child is None:
                    self.left_child = Tree(value)
                else:
                    self.left_child.add_children(value)
            elif value > self.data:
                if self.right_child is None:
                    self.right_child = Tree(value)
                else:
                    self.right_child.add_children(value)
        else: self.data = value

    #This will find the route of the node given    
    def find_path(self, root, route, v1):
        
        if root is None:
            return False
        
        route.append(root.data)
        
        if root.data == v1:
            return True
        
        if (root.left_child != None and self.find_path(root.left_child, route, v1)) or (root.right_child != None and self.find_path(root.right_child, route, v1)):
            return True
        
        route.pop()
        return False
    
    #This is the code to find LCA
    def LCA(self, root, v1, v2):
        
        path1 = []
        path2 = []
        
        if (not self.find_path(root, path1, v1)) or (not self.find_path(root, path2, v2)):
            return -1
        
        i = 0
        while(i < len(path1) and i < len(path2)):
            if path1[i] != path2[i]:
                break
            
            i += 1
            
        return path1[i-1]

root = Tree(68)
root.add_children(34)
root.add_children(94)
root.add_children(41)
root.add_children(76)
root.add_children(101)
root.add_children(14)
root.add_children(81)
root.add_children(43)
root.add_children(79)
root.add_children(107)

print(root.LCA(root, 14, 41))