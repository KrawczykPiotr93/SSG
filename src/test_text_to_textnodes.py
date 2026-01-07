import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextType, TextNode
from markdown_to_blocks import markdown_to_blocks

class test_single_code_blocks(unittest.TestCase):
    def test_code_block(self):
        test_text = "`PROGRAMMERINHO`"
        nodes = text_to_textnodes(test_text)
        self.assertEqual(
            [
                TextNode("PROGRAMMERINHO", TextType.CODE),
            ],
            nodes
        )

    def test_bold_block(self):
        test_text = "**FATTY**"
        nodes = text_to_textnodes(test_text)
        self.assertEqual(
            [
                TextNode("FATTY", TextType.BOLD_TEXT),
            ],
            nodes
        )     

    def test_image_block(self):
        test_text = "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
        nodes = text_to_textnodes(test_text)
        self.assertEqual(
            [
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            nodes
        ) 


    def test_italic_block(self):
        test_text = "_ITALY_"
        nodes = text_to_textnodes(test_text)
        self.assertEqual(
            [
                TextNode("ITALY", TextType.ITALIC_TEXT),
            ],
            nodes
        ) 

    def test_link_block(self):
        test_text = "[linkerinho](https://boot.dev)"
        nodes = text_to_textnodes(test_text)
        self.assertEqual(
            [
                TextNode("linkerinho", TextType.LINK, "https://boot.dev")
            ],
            nodes
        ) 

class test_two_blocks(unittest.TestCase):
    def test_block_and_link(self):
        test_text = "Yo! This is [linkerinho](https://boot.dev) and **BOLDER**"
        nodes = text_to_textnodes(test_text)
        self.assertEqual(
            [
                TextNode("Yo! This is ", TextType.PLAIN_TEXT),
                TextNode("linkerinho", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.PLAIN_TEXT),
                TextNode("BOLDER", TextType.BOLD_TEXT),
            ],
            nodes
        )         

    def test_code_and_image(self):
        test_text = "Yo! This is `CODERINHO` and ![imaginios](https://boot.dev)"
        nodes = text_to_textnodes(test_text)
        self.assertEqual(
            [
                TextNode("Yo! This is ", TextType.PLAIN_TEXT),
                TextNode("CODERINHO", TextType.CODE),
                TextNode(" and ", TextType.PLAIN_TEXT),
                TextNode("imaginios", TextType.IMAGE, "https://boot.dev"),
            
            ],
            nodes
        )

    def test_link_and_image(self):
        test_text = "[linkerinho](https://boot.dev)![imaginios](https://boot.dev)"
        nodes = text_to_textnodes(test_text)
        self.assertEqual(
            [
                TextNode("linkerinho", TextType.LINK, "https://boot.dev"),                
                TextNode("imaginios", TextType.IMAGE, "https://boot.dev"),        
            ],
            nodes
        )            

    def test_all(self):
        test_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(test_text)
        self.assertEqual(
            [
                TextNode("This is ", TextType.PLAIN_TEXT),
                TextNode("text", TextType.BOLD_TEXT),
                TextNode(" with an ", TextType.PLAIN_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT),
                TextNode(" word and a ", TextType.PLAIN_TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.PLAIN_TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.PLAIN_TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),      
            ],
            nodes
        )            

class test_markdown_to_blocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )         

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

if __name__ == "__main__":
    unittest.main()