import unittest

from delimiter_split import split_nodes_delimiter, index_finder, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestDelimiterSplit(unittest.TestCase):
    def test_delimiter_split_code(self):
        test_node1 = TextNode("This is text with a `code block` word", TextType.PLAIN_TEXT)
        nodes_list = [test_node1]
        result = split_nodes_delimiter(nodes_list, "`", TextType.CODE)
        self.assertEqual(len(result), 3)

    def test_delimiter_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN_TEXT),
                TextNode("bolded", TextType.BOLD_TEXT),
                TextNode(" word", TextType.PLAIN_TEXT),
            ],
            new_nodes,
        )

    def test_delimiter_code(self):
        node = TextNode("`The code section` is included in the text", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("The code section", TextType.CODE),
                TextNode(" is included in the text", TextType.PLAIN_TEXT),
            ],
            new_nodes,
        )

    def test_delimiter_italics(self):
        node = TextNode("This text includes a word in _italics_", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        self.assertListEqual(
            [
                TextNode("This text includes a word in ", TextType.PLAIN_TEXT),
                TextNode("italics", TextType.ITALIC_TEXT),
            ],
            new_nodes,
        )

    def test_two_identical_delimiters(self):
        node = TextNode("This **text** includes two words in **bold**", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertListEqual(
            [
                TextNode("This ", TextType.PLAIN_TEXT),
                TextNode("text", TextType.BOLD_TEXT),
                TextNode(" includes two words in ", TextType.PLAIN_TEXT),
                TextNode("bold", TextType.BOLD_TEXT),
            ],
            new_nodes,
        )
    
    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC_TEXT)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD_TEXT),
                TextNode(" and ", TextType.PLAIN_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT),
            ],
            new_nodes,
        )

class TestSplitImage(unittest.TestCase):
    def test_single_image(self):
        test_node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.PLAIN_TEXT)
        result = split_nodes_image([test_node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
        ],
         result
    )

    def test_two_images(self):
        test_node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.PLAIN_TEXT)
        result = split_nodes_image([test_node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
        ],
         result
    )

    def test_two_images_and_ending_text(self):
        test_node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) and text", TextType.PLAIN_TEXT)
        result = split_nodes_image([test_node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                TextNode(" and text", TextType.PLAIN_TEXT),
        ],
         result
    )    

    def test_only_image(self):
        test_node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png)", TextType.PLAIN_TEXT)
        result = split_nodes_image([test_node])
        self.assertListEqual([TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")],result)   

class TestSplitLink(unittest.TestCase):
    def test_single_link(self):
        test_node = TextNode("This is text with an [link](https://www.google.pl)", TextType.PLAIN_TEXT)
        result = split_nodes_link([test_node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("link", TextType.LINK, "https://www.google.pl")
        ],
        result
    )
        
    def test_two_links(self):
        test_node = TextNode("This is text with an [link](https://www.google.pl) and second link [better link](www.boot.dev)", TextType.PLAIN_TEXT)
        result = split_nodes_link([test_node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("link", TextType.LINK, "https://www.google.pl"),
                TextNode(" and second link ", TextType.PLAIN_TEXT),
                TextNode("better link", TextType.LINK, "www.boot.dev")
        ],
        result
    )

    def test_two_links_ending_text(self):
        test_node = TextNode("This is text with an [link](https://www.google.pl) and second link [better link](www.boot.dev) and some text at the end", TextType.PLAIN_TEXT)
        result = split_nodes_link([test_node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("link", TextType.LINK, "https://www.google.pl"),
                TextNode(" and second link ", TextType.PLAIN_TEXT),
                TextNode("better link", TextType.LINK, "www.boot.dev"),
                TextNode(" and some text at the end", TextType.PLAIN_TEXT),
        ],
        result
    )
        
    def online_link(self):
        test_node = TextNode("[link](https://www.google.pl)", TextType.PLAIN_TEXT)
        result = split_nodes_link([test_node])
        self.assertListEqual([TextNode("link", TextType.LINK, "https://www.google.pl")], result)

if __name__ == "__main__":
    unittest.main()