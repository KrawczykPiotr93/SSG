import unittest

from textnode import TextNode, TextType, text_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_name_not_eq(self):
        node = TextNode("This is a text node 1 ", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node 2", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)
    
    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT, url = "https://www.google.com")
        self.assertNotEqual(node, node2)

class test_node_to_html(unittest.TestCase):
    def test_not_text_type(self):
        node = TextNode("Arkham Horror is the best!", "Something")
        with self.assertRaises(ValueError):
            text_to_html_node(node)

    def test_text(self):
        node = TextNode("Arkham Horror is the best!", TextType.PLAIN_TEXT)
        html_node = text_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Arkham Horror is the best!")

    def test_bold(self):
        node = TextNode("Arkham Horror is the best!", TextType.BOLD_TEXT)
        html_node = text_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Arkham Horror is the best!")

    def test_italic(self):
        node = TextNode("Arkham Horror is the best!", TextType.ITALIC_TEXT)
        html_node = text_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Arkham Horror is the best!")

    def test_code(self):
        node = TextNode("Arkham Horror is the best!", TextType.CODE)
        html_node = text_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Arkham Horror is the best!")

    def test_link(self):
        node = TextNode("Arkham Horror is the best!", TextType.LINK, "https://www.google.com")
        html_node = text_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Arkham Horror is the best!")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"} )

    def test_img(self):
        node = TextNode("Arkham Horror is the best!", TextType.IMAGE, "https://www.google.com")
        html_node = text_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://www.google.com", "alt": "Arkham Horror is the best!"} )

if __name__ == "__main__":
    unittest.main()