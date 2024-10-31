def build_xml_element(tag, content, **attributes):
    attr_str = ''.join(f' {k}="{v}"' for k, v in attributes.items())
    return f"<{tag}{attr_str}>{content}</{tag}>"

print(build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))