'''
Create LXML ElementMaker (factory) objects that create KML objects using the 
appropriate namespaces
'''

from lxml import etree, objectify

nsmap={
    None: "http://www.opengis.net/kml/2.2",
    'atom': "http://www.w3.org/2005/Atom",
    'gx': "http://www.google.com/kml/ext/2.2",
}

# create a factory object for creating objects in the KML namespace
KML_ElementMaker = objectify.ElementMaker(
    annotate=False,
    namespace=nsmap[None],
    nsmap=nsmap,
)
# create a factory object for creating objects in the ATOM namespace
ATOM_ElementMaker = objectify.ElementMaker(
    annotate=False,
    namespace="http://www.w3.org/2005/Atom",
    nsmap={'atom': "http://www.w3.org/2005/Atom"},
)
# Create a factory object for the KML Google Extension namespace
GX_ElementMaker = objectify.ElementMaker(
    annotate=False,
    namespace="http://www.google.com/kml/ext/2.2",
    nsmap={'gx': "http://www.google.com/kml/ext/2.2"},
)

def get_factory_object_name(namespace):
    "Returns the correct factory object for a given namespace"
    
    factory_map = {
        'http://www.opengis.net/kml/2.2': 'KML',
        'http://www.w3.org/2005/Atom': 'ATOM',
    }
    if factory_map.has_key(namespace):
        factory_object_name = factory_map[namespace]
    else:
        # use the KML factory object as the default, if no namespace is given
        factory_object_name = 'KML'
    return factory_object_name

def write_python_script_for_kml_document(doc):
    "Generate a python script that will construct a given KML document"
    import StringIO
    from pykml.helpers import separate_namespace
    
    output = StringIO.StringIO()
    indent_size = 2
    
    # add the namespace declaration section
    output.write('from pykml.factory import KML_ElementMaker as KML\n')
    output.write('from pykml.factory import ATOM_ElementMaker as ATOM\n')
    output.write('from pykml.factory import GX_ElementMaker as GX\n')
    output.write('\n')
    
    level = 0
    context = etree.iterwalk(doc, events=("start", "end"))
    output.write('doc = ')
    last_action = None
    for action, elem in context:
        if action in ('start','end'):
            namespace, element_name = separate_namespace(elem.tag)
            if action in ('start'):
                if last_action == None:
                    indent = ''
                else:
                    indent = ' ' * level * indent_size
                level += 1
                
                if elem.text:
                    # METHOD 1
#                    # treat all text string the same. this works but gets
#                    # messy for multi-line test strings
#                    text = repr(elem.text)
                    # METHOD 2 - format multiline strings differently
                    text_list = elem.text.split('\n')
                    if len(text_list) == 1:
                        text = repr(elem.text)
                    else: # len(text_list) > 1
                        # format and join all non-empty lines
                        text = '\n' + ''.join(
                                ['{indent}{content}\n'.format(
                                        indent=' '*(len(t)-len(t.lstrip())),
                                        content=repr(t.lstrip())
                                    ) for t in text_list if len(t.strip())>0
                                ]
                            ) + indent
                else:
                    text = ''
                output.write('{indent}{factory}.{tag}({text}\n'.format(
                    indent = indent,
                    factory = get_factory_object_name(namespace),
                    tag = element_name,
                    text = text,
                ))
            elif action in ('end'):
                level -= 1
                if last_action == 'start':
                    output.pos -= 1
                    indent = ''
                else:
                    indent = ' ' * level * indent_size
                for att,val in elem.items():
                    output.write('{0}{1}="{2}",'.format(indent,att,val))
                output.write('{0}),\n'.format(indent))
        last_action = action
    # remove the last comma
    output.pos -= 2
    output.truncate()
    output.write('\n')
    # add python code to print out the KML document
    output.write('from lxml import etree\n')
    output.write('print etree.tostring(doc,pretty_print=True)\n')
    
    return output.getvalue()