from markdown_to_blocks import markdown_to_blocks 
from block_to_blocktype import BlockType, block_to_block_type 
from htmlnode import HTMLnode, ParentNode, LeafNode 
from text_to_textnodes import text_to_textnodes 
from textnode import TextType, TextNode, text_to_html_node 

def extract_children_from_html(text):
    text_nodes = text_to_textnodes(text) # Split text of a block block into text children nodes
    # print(f"\necfm text_nodes = {text_nodes}")
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_to_html_node(text_node))
    # print(f"\necfh html_nodes = {html_nodes}")
    return html_nodes

def list_to_html(tag, item_tag, text):
    items = text.split("\n")
    # print(f"\nItems = {items}")

    HTML_list_items = []
    for item in items:
        if tag == "ul":
            item = item[2:]
        else:
            item = item[3:]
        # print(f"\nIterating over {item}")
        children = extract_children_from_html(item)
        # print(f"\nChildren: {children}")
        html_node = ParentNode(item_tag, children) 
        # print(f"\nParent node = {html_node.to_html()}")
        HTML_list_items.append(html_node)
        # print(f"\nHTML_list_nodes inside the loop = {HTML_list_items}")
    HTML_list = ParentNode(tag, HTML_list_items)
    # print(f"\nFinal HTML list = {HTML_list.to_html()}")

    return HTML_list    

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown) # Split markdown into text blocks
    
    HTMLnodes = []
    for block in blocks: # Iterating over each block to check its BlockType. Creating HTML parent node and children nodes if necessary
        # print(f"\n=====================")
        # print(f"\nBlock = {block}")
        blockType = block_to_block_type(block) # Get block's type
        # print(f"\nBlocktype: {blockType}")

        if blockType == BlockType.PARAGRAPH:
            text_nodes_from_block = text_to_textnodes(block)
            # print(f"\TFNB {text_nodes_from_block} ")
            htmlnodes = []
            for node in text_nodes_from_block:
                htmlnodes.append(text_to_html_node(node))
            # print(f"Html nodes = {htmlnodes}")
            HTMLnodes.append(ParentNode("p", htmlnodes))


        if blockType == BlockType.HEADING:
            count = block[:6].count("#") # Checking how many # chars are at the beggining of the text
            block = block[count +  1:] # Removing first hashtags from the heading
            text_nodes_from_block = text_to_textnodes(block)
            htmlnodes = []
            for node in text_nodes_from_block:
                htmlnodes.append(text_to_html_node(node))
            HTMLnodes.append(ParentNode(f"h{count}", htmlnodes))
        
        if blockType == BlockType.QUOTE:
            lines = block.split("\n")
            new_lines = []
            for line in lines:
                if not line.startswith(">"):
                    raise ValueError("invalid quote block")
                new_lines.append(line.lstrip(">").strip())
            block = " ".join(new_lines)
            text_nodes_from_block = text_to_textnodes(block)
            htmlnodes = []
            for node in text_nodes_from_block:
                htmlnodes.append(text_to_html_node(node))
            HTMLnodes.append(ParentNode(f"blockquote", htmlnodes))                        

        if blockType == BlockType.UNORDERED_LIST:
            HTMLnodes.append(list_to_html("ul", "li", block))

        if blockType == BlockType.ORDERED_LIST:
            HTMLnodes.append(list_to_html("ol", "li", block))

        if blockType == BlockType.CODE:
            text = block[4:-3]
            # print(f"\nLines inside the code block = {text}")
            raw_text_node = TextNode(text, TextType.PLAIN_TEXT)
            # print(f"\nRaw text node inside the code block = {raw_text_node}")
            child = text_to_html_node(raw_text_node)
            # print(f"\nChild = {child}")
            code = ParentNode("code", [child])
            # print(f"\nParent code = {code}")
            pre = ParentNode("pre", [code])
            # print(f"\nParent code = {pre}")
            HTMLnodes.append(pre)

    div_wrapper = ParentNode("div", HTMLnodes)
    # print(f"\nFinal HTML = {div_wrapper.to_html()}")

    return div_wrapper

# md = """
# ```
# This is text that _should_ remain
# the **same** even with inline stuff
# ```
# """
# node = markdown_to_html_node(md)
# print(f"\nThe last print {node.to_html()}")