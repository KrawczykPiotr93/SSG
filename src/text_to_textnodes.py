import delimiter_split
from textnode import TextType, TextNode

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.PLAIN_TEXT)]
    delimiters = {'**': TextType.BOLD_TEXT, '_': TextType.ITALIC_TEXT, '`': TextType.CODE}
    for delimiter in delimiters:
        new_nodes = []
        for node in nodes:
            if node.text_type != TextType.PLAIN_TEXT:
                new_nodes.append(node)
                continue
            try:
                new_nodes.extend(delimiter_split.split_nodes_delimiter([node], delimiter, delimiters[delimiter]))
            except ValueError:
                new_nodes.append(node)
        nodes = new_nodes

    functions = [delimiter_split.split_nodes_image, delimiter_split.split_nodes_link]
    for function in functions:
        new_nodes = []
        new_nodes = function(nodes)
        nodes = new_nodes 
    return nodes


# Version for debugging

# def text_to_textnodes(text):
#     nodes = [TextNode(text, TextType.PLAIN_TEXT)]
#     delimiters = {'**': TextType.BOLD_TEXT, '_': TextType.ITALIC_TEXT, '`': TextType.CODE}
#     for delimiter in delimiters:
#         new_nodes = []
#         # print(f"\nCurrent delimiter = {delimiter}\n")
#         # print(f"The list of the nodes {nodes}")
#         # # print(f"The list of the new_nodes {new_nodes}\n")
#         for node in nodes:
#             # # print(f"Iterating over {node}")
#             if node.text_type != TextType.PLAIN_TEXT:
#                 new_nodes.append(node)
#                 continue
#             try:
#                 new_nodes.extend(delimiter_split.split_nodes_delimiter([node], delimiter, delimiters[delimiter]))
#             except ValueError:
#                 new_nodes.append(node)
#             # print(f"New nodes after the itearion - {new_nodes}\n")
#         # print(f"Nodes after inner loop - {new_nodes}")
#         nodes = new_nodes
#         # print(f"Nodes to teraz {nodes}")

#     functions = [delimiter_split.split_nodes_image, delimiter_split.split_nodes_link]
#     for function in functions:
#         # print(f"\nWe do {function.__name__}")
#         new_nodes = []
#         new_nodes = function(nodes)
#         # print(f"New nodes after the split = {new_nodes}")
#         nodes = new_nodes 
#     return nodes