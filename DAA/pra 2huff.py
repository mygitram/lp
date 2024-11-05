class Node:
    def __init__(self,char,frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

def count_freq(temp):
    freq_c={}
    for i in temp:
        if i not in freq_c:
            freq_c[i] = 1
        else:
            freq_c[i] +=1 
    return freq_c


def generate_codes(node, prefix="", code_map={}):
    if node:
        if node.char:
            code_map[node.char] = prefix
        generate_codes(node.left, prefix + "0", code_map)
        generate_codes(node.right, prefix + "1", code_map)
    return code_map

def generateTree(text):
    freq_c = count_freq(text)
    nodes = [Node(ch,fr) for (ch,fr) in freq_c.items()]
    while len(nodes)>1:
        sorted(nodes,key=lambda x:x.frequency)
        left = nodes.pop(0)
        right = nodes.pop(0)

        mergedNode = Node(None,left.frequency+right.frequency)
        mergedNode.left = left
        mergedNode.right= right

        nodes.append(mergedNode)
    return nodes[0] if nodes else None


text = "hellohuffman"
root = generateTree(text)
code_map = generate_codes(root)

print("Text:", text)
print("Huffman Code:", code_map)
