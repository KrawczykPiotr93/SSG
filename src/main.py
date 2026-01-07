from textnode import TextType, TextNode
from copy_to_docs import delete_from_docs, copy_to_docs, docs_path, static_path
from generate_pages_recursive import generate_pages_recursive
import sys

def main():
    try:
        basepath = sys.argv[1] 
    except:
        basepath = "/"
    print(f"Basepath = {basepath}")

    delete_from_docs()
    copy_to_docs(static_path, docs_path)

    generate_pages_recursive("content", "template.html", "docs", "content", basepath)
    
main()