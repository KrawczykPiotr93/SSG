import unittest
from extract_functions import extract_markdown_images, extract_markdown_links

class TextExtraction(unittest.TestCase):
    def test_extraction_markdown_images(self):
        test_text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_images(test_text)
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extraction_markdown_links(self):
        test_text = "This is text with an [link](www.google.pl)"
        matches = extract_markdown_links(test_text)
        self.assertListEqual([("link", "www.google.pl")], matches)        


if __name__ == '__main__':
    unittest.main()