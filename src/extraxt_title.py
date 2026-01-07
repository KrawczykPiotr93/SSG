
def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise Exception("There is no h1 title in the markdown")


# md = '''
# # Tolkien Fan Club

# ![JRR Tolkien sitting](/images/tolkien.png)

# Here's the deal, **I like Tolkien**.

# > "I am in fact a Hobbit in all but size."
# >
# > -- J.R.R. Tolkien

# ## Blog posts
# '''

# print(extract_title(md))