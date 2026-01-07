from textnode import TextType, TextNode
from extract_functions import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        # print(f"Iterating on the {old_node}")
        if old_node.text_type != TextType.PLAIN_TEXT:
            # print("Inside the condition")
            new_nodes.append(TextNode(old_node.text, old_node.text_type))
            continue
        split = old_node.text.split(delimiter)
        # print(f"Split: {split}")
        if len(split) % 2 == 0 or len(split) == 1:
            raise ValueError("Text doesn't contain a pair of specified delimiters.")
        for i in range(len(split)):
            if split[i] == '':
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(split[i], TextType.PLAIN_TEXT))
            else:
                new_nodes.append(TextNode(split[i], text_type))
    return new_nodes

def index_finder(text, char1, char2, char3, char4):
    return text.find(char1), text.find(char2), text.find(char3), text.find(char4)

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN_TEXT))   
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN_TEXT))    

    return new_nodes

