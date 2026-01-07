from textnode import TextType, TextNode
from copy_to_public import delete_from_public, copy_to_public, public_path, static_path
from generate_pages_recursive import generate_pages_recursive
import sys

def main():
    try:
        basepath = sys.argv[1] 
    except:
        basepath = "/"
    print(f"Basepath = {basepath}")

    delete_from_public()
    copy_to_public(static_path, public_path)

    generate_pages_recursive("content", "template.html", "public", "content", basepath)
    
main()