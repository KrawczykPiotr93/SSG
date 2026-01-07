def markdown_to_blocks(markdown):
    split = markdown.split("\n\n")
    strip = list(block.strip() for block in split if block != '')
    return strip
