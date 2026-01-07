import re

def extract_markdown_images(text):
    alts = re.findall(r"\!\[(.*?)\]", text)
    urls = re.findall(r"\(([^\(\)]*)\)", text)
    return list(zip(alts, urls))

def extract_markdown_links(text):
    alts = re.findall(r"\[(.*?)\]", text)
    urls = re.findall(r"\(([^\(\)]*)\)", text)
    return list(zip(alts, urls))
