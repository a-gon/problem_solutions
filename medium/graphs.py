class Node:
    def __init__(self, value, children = []):
        self.value = value
        self.children = children

    def printG(self):
        queue = [self]
        graph = []
        visited = set()
        while queue:
            node = queue.pop(0)
            if node in visited:
                print(f'{node.value} cycle detected')
                continue
            if node:
                graph.append(node.value)
                visited.add(node)
                queue.extend(node.children)
        print(graph)
        
    def dfs(self, target):
        stack = [self]
        visited = set()

        while stack:
            node = stack.pop()    # pop from the very top

            print(f'node {node.value}')
            if node in visited:
                print(f'node {node.value} already visited')
                continue
            visited.add(node)
            if node.value == target:
                return True
            stack.extend(node.children)
        return False


        
    
    def rec_dfs(self, target):
        def recur(v, target):
            if not v:
                print('not v')
                return False
            visited.add(v)
            print(f'visited node {v.value}')
            if v.value == target:
                print(f'target {target} found')
                return True
            for next in v.children:
                if next not in visited:
                    recur(next, target)
            print(f'reached end, target {target} not found')
            # return False

        visited = set()
        return recur(self, target)
             
    
n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n0.children = [n1, n3]
n1.children = [n2]
n2.children = [n5, n6]
n3.children = [n4]
n5.children = [n0]
n4.children = [n2, n3]
n6.children = [n3, n5]

    
# graph.printG()

# n0.printG()
print(n0.dfs(5))
# print(n0.rec_dfs(3))

