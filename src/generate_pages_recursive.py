import os
from markdown_to_html import markdown_to_html_node
from extraxt_title import extract_title
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, content_root):
    directory_contents = os.listdir(dir_path_content)

    for directory in directory_contents:
        directory_filepath = os.path.join(dir_path_content, directory)
        relative_path = os.path.relpath(directory_filepath, content_root)

        if not os.path.isfile(directory_filepath):
            generate_pages_recursive(directory_filepath, template_path, dest_dir_path, content_root)

        if os.path.isfile(directory_filepath): 
            with open(directory_filepath, "r") as f:
                markdown = f.read()
        
            with open(template_path, "r") as f:
                template = f.read()

            contents_in_html = markdown_to_html_node(markdown).to_html()
            title = extract_title(markdown)
            template = template.replace("{{ Title }}", title).replace("{{ Content }}", contents_in_html)

            dest_path = os.path.join(dest_dir_path, relative_path)
            dest_path = os.path.splitext(dest_path)[0] + ".html"
            dest_directory = os.path.dirname(dest_path)

            if not os.path.exists(dest_directory):
                os.makedirs(dest_directory)
            
            with open(dest_path, "w") as f:
                f.write(template)


# # Code with prints for debugging

# def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, content_root):
#     directory_contents = os.listdir(dir_path_content)
#     print("\n============")
#     print(f"\nDirectory contents = {directory_contents}")

#     for directory in directory_contents:
#         directory_filepath = os.path.join(dir_path_content, directory)
#         relative_path = os.path.relpath(directory_filepath, content_root)
#         print(f"\nIterating over {directory_filepath}")

#         if not os.path.isfile(directory_filepath):
#             print(f"\n{directory_filepath} is a folder. Calling recursion.")
#             generate_pages_recursive(directory_filepath, template_path, dest_dir_path, content_root)

#         if os.path.isfile(directory_filepath): 
#             with open(directory_filepath, "r") as f:
#                 markdown = f.read()
#             # print(markdown)  
        
#             with open(template_path, "r") as f:
#                 template = f.read()
#             # print(template)

#             contents_in_html = markdown_to_html_node(markdown).to_html()
#             title = extract_title(markdown)
#             template = template.replace("{{ Title }}", title).replace("{{ Content }}", contents_in_html)
#             # print(template)

#             dest_path = os.path.join(dest_dir_path, relative_path)
#             dest_path = os.path.splitext(dest_path)[0] + ".html"
#             print(f"\nDestination path = {dest_path}")       
#             dest_directory = os.path.dirname(dest_path)
#             print(f"\nDestination direcotry = {dest_directory}") 

#             if not os.path.exists(dest_directory):
#                 os.makedirs(dest_directory)
            
#             with open(dest_path, "w") as f:
#                 f.write(template)
#                 print(f"\n{dest_path} has been written successfully")

