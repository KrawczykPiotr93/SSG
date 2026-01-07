import unittest
from block_to_blocktype import BlockType, block_to_block_type

class test_block_to_blocktype(unittest.TestCase):
    def test_heading(self):
        test_text = '### Test'
        result = block_to_block_type(test_text)
        self.assertEqual(BlockType.HEADING, result)

    def test_heading_no_match(self):
        test_text = '####### Test'
        result = block_to_block_type(test_text)
        self.assertEqual(BlockType.PARAGRAPH, result)

    def test_code(self):
        test_text = '```Test```'
        result = block_to_block_type(test_text)
        self.assertEqual(BlockType.CODE, result)

    def test_code_no_match(self):
        test_text = '``Test``'
        result = block_to_block_type(test_text)
        self.assertEqual(BlockType.PARAGRAPH, result)

    def test_quote(self):
        test_text = '>AAAAA\n>BBB\n>CCC\n>DDDD'
        result = block_to_block_type(test_text)
        self.assertEqual(BlockType.QUOTE, result)

    def test_quote_no_match(self):
        test_text = '>AAAAA\n>BBB\n>CCC\nD'
        result = block_to_block_type(test_text)
        self.assertEqual(BlockType.PARAGRAPH, result)

    def test_UL(self):
        test_text = '- AAAAA\n- BBB\n- CCC\n- DDDD\n- E'
        result = block_to_block_type(test_text)
        self.assertEqual(BlockType.UNORDERED_LIST, result)

    def test_UL_no_match(self):
        test_text = '- AAAAA\n-BBB\n- CCC\n- DDDD\n- E'
        result = block_to_block_type(test_text)
        self.assertEqual(BlockType.PARAGRAPH, result)

    def test_OL(self):
        test_text = '1. AAAAA\n2. A'
        result = block_to_block_type(test_text)
        self.assertEqual(BlockType.ORDERED_LIST, result)

    def test_OL_no_match(self):
        test_text = '1. AAAA\n 2.AAA'
        result = block_to_block_type(test_text)
        self.assertEqual(BlockType.PARAGRAPH, result)


if __name__ == "__main__":
    unittest.main()