import unittest

from htmlnode import HTMLnode, LeafNode, ParentNode

class TestHTMLnode(unittest.TestCase):
    def test_props_to_html(self):
        test_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        test_node = HTMLnode(None, None, None, test_props)
        # print(test_node.props_to_html())

    def test_repr(self):
        test_props = {
            "href": "https://www.google123.com",
            "target": "_blank123",
        }
        test_node = HTMLnode("abc", "efg", ["hij", 2], test_props)
        # print(test_node.__repr__())

    def test_values(self):
        test_node = HTMLnode("div", "Hello world!")

        self.assertEqual(test_node.tag, "div")
        self.assertEqual(test_node.value, "Hello world!")
        self.assertEqual(test_node.children, None)
        self.assertEqual(test_node.props, None)

class testLeafNode(unittest.TestCase):
    def test_leat_to_html(self):
        node = LeafNode("p", "Test text!")
        self.assertEqual(node.to_html(), "<p>Test text!</p>")

    def test_leaf_to_html_a(self):
        test_props = {
            "href": "https://www.google.pl",
            "target": "_blank"
        }
        node = LeafNode("a", "Click me", test_props)
        self.assertEqual(node.to_html(), "<a href=https://www.google.pl target=_blank>Click me</a>")

    def test_leaf_no_tag(self):
        node = LeafNode(None, "Hello World!")
        self.assertEqual(node.to_html(), "Hello World!")

class testParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )
        
    def test_to_html_no_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_grandchildren_no_value(self):
        grandchild_node = LeafNode("b", None)
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
       
        with self.assertRaises(ValueError):
            parent_node.to_html()

