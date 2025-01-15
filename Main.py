from Node import Node

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)

node1.left = node2  
node1.right = node3 

node2.left = node4  
node2.right = node5  
node3.left = node6  
node3.right = node7  

node4.left = node8   
node4.right = node9 

node5.left = node10 

def preorder_dfs(node,DFS):
    if node:
        DFS.append(node.val)  # Kök düğümü yazdır
        preorder_dfs(node.left,DFS)   # Sol alt ağacı ziyaret et
        preorder_dfs(node.right,DFS)  # Sağ alt ağacı ziyaret et

# Preorder DFS'yi başlat
DFS = []
preorder_dfs(node1,DFS)
print(DFS)