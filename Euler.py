import math

#This is the Node Class
class Node:
    def __init__(self, value):
        self.data = value
        self.right_child = None
        self.left_child = None

#This is the tree class
#This class contains the root
#This also contains the function to add Children
class Tree:
    content = []
    
    def __init__(self):
        self.root = None
        
    def add_child(self, arr, root, i, n):
        if i < n:
            temp = Node(arr[i])
            root = temp
            
            root.left_child = self.add_child(arr, root.left_child, 2 * i + 1, n)
            root.right_child = self.add_child(arr, root.right_child, 2 * i + 2, n)
            
        return root
    
    def pre_order(self, root):
        
        if root != None:
            Tree.content.append(root.data)
            self.pre_order(root.left_child)
            self.pre_order(root.right_child)
            
        return Tree.content
#This is the LCA class
#This contains our main code       
class LCA:
    
    def __init__(self, root, length):
        self.pre_process_array = [[0] * (math.floor(math.log2(length) + 2)) for _ in range((length * 2) - 1)]
        self.euler = [0] * (length * 2 - 1)
        self.height = [0] * (length * 2 - 1)
        self.index = [-1  for _ in range(length + 1)]
        self.tour = 0
        self.euler_tour(root, 0)
        self.build_sparse_table(self.height)
    
    def build_sparse_table(self, height_array):
        for i in range(0, len(height_array)):
            self.pre_process_array[i][0] = height_array[i]
        
        j = 1
        
        while (2 ** j) <= len(height_array):
            i = 0
            while (i+(2**j)-1) < len(height_array):
                if self.pre_process_array[i][j-1] < self.pre_process_array[i + (2**(j-1))][j-1]:
                    self.pre_process_array[i][j] = self.pre_process_array[i][j - 1]
                else:
                    self.pre_process_array[i][j] = self.pre_process_array[i + (2**(j-1))][j-1]
                    
                i += 1
                
            j +=1
            
        return self.pre_process_array
            
    def rmq(self, L, R):
        
        l = R - L + 1
        k = int(math.log2(l))
        
        val =  min(self.pre_process_array[L][k], self.pre_process_array[L+l-(2**k)][k])
        
        lca_index = self.height[L:R+1].index(val) + L
        
        return lca_index
        
    def euler_tour(self, root, level):
        if root is not None:

            self.euler[self.tour] = root.data
            self.height[self.tour] = level
            self.tour += 1
            
            if self.index[root.data] == -1:
                self.index[root.data] = self.tour - 1
                
            if root.left_child is not None:
                self.euler_tour(root.left_child, level + 1)
                self.euler[self.tour] = root.data
                self.height[self.tour] = level
                self.tour += 1
                
            if root.right_child is not None:
                self.euler_tour(root.right_child, level + 1)
                self.euler[self.tour] = root.data
                self.height[self.tour] = level
                self.tour += 1
            
    def find_LCA(self, val1, val2):
        if val1 >= len(self.index) or val2 >= len(self.index):
            return -1
        
        if self.index[val1] > self.index[val2]:
            return self.euler[self.rmq(self.index[val2], self.index[val1])]
        elif self.index[val2] > self.index[val1]:
            return self.euler[self.rmq(self.index[val1], self.index[val2])]
                      

tree_data = [1,2,3,4,5,6,7,8,9,10]
length = len(tree_data)
         
tree = Tree()
root = tree.root


tree.root = tree.add_child(tree_data, root, 0, length)

'''
This is how the tree is
                                1
                               / \
                              /   \
                             2     3
                            /\     /\
                           /  \   /  \
                          4    5  6   7
                         /\    /
                        /  \  /
                       8    9 10 
'''


l = LCA(tree.root, length)
print(l.find_LCA(5, 4))