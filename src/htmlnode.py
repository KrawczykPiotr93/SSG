class HTMLnode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("HTMLnode base class doesnt have to_html method.")
    
    def props_to_html(self):
        string = ""
        if not self.props:
            return string
        for prop in self.props:
            string = f"{string} {prop}={self.props[prop]}" 
        return string
    
    def __repr__(self):
       return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLnode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes MUST have a value.")
        if not self.tag:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
 
    def __repr__(self):
       return f"LeafNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class ParentNode(HTMLnode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes MUST have a tag.")
        if not self.children:
            raise ValueError("Children list cannot be empty")
        string = f"<{self.tag}>" 
        for child in self.children:
            string += child.to_html()
        string += f"</{self.tag}>"
        return string

