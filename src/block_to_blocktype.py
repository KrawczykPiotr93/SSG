from enum import Enum
import re
from textnode import TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(markdown_block):
    if re.findall(r"^(#{1,6})\s+(.+)$", markdown_block):
        return BlockType.HEADING
    
    if markdown_block.startswith("```") and markdown_block.endswith("```"):
        return BlockType.CODE
    
    split = markdown_block.split("\n")
    code_block_flag = True
    for item in split:
        if item.startswith(">"):
            continue
        else:
            code_block_flag = False
    if code_block_flag:
        return BlockType.QUOTE
    
    split = markdown_block.split("\n")
    unordered_list_flag = True
    for item in split:
        if item.startswith("- "):
            continue
        else:
            unordered_list_flag = False
    if unordered_list_flag:
        return BlockType.UNORDERED_LIST 
    
    split = markdown_block.split("\n")
    ordered_list_flag = True
    for i in range(len(split)):
        if split[i].startswith(f"{i + 1}. "):
            continue
        else:
            ordered_list_flag = False
    if ordered_list_flag:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

