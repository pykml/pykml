'''
Create LXML ElementMaker objects that create KML objects using the 
appropriate namespace
'''

from lxml import etree, objectify

nsmap={
    None: "http://www.opengis.net/kml/2.2",
    'atom': "http://www.w3.org/2005/Atom",
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
    nsmap={'atom': "http://www.w3.org/2005/Atom"}
)

def write_python_script_for_kml_document(doc):
    "Generate a python script that will construct a given KML document"
    import StringIO
    
    def separate_namespace(qname):
        "Separate the namespace from the element"
        import re
        try:
            namespace, element_name = re.search('^{(.+)}(.+)$', qname).groups()
        except:
            namespace = None
            element_name = qname
        return namespace, element_name
    
    def get_factory_object(namespace):
        "Returns the correct factory object for a given namespace"
        
        factory_map = {
            'http://www.opengis.net/kml/2.2': 'KML',
            'http://www.w3.org/2005/Atom': 'ATOM',
        }
        if factory_map.has_key(namespace):
            factory_object = factory_map[namespace]
        else:
            factory_object = 'KML'
        return factory_object
    
    output = StringIO.StringIO()
    indent_size = 2
    
    # add the namespace declaration section
    output.write('from pykml.kml_ogc.factory import KML_ElementMaker as K\n')
    output.write('from pykml.kml_ogc.factory import ATOM_ElementMaker as ATOM\n')
    output.write('\n')
    
    level = 0
    events = ("start", "end")
    context = etree.iterwalk(doc, events=events)
    output.write('doc = ')
    #import ipdb; ipdb.set_trace()
    last_action = None
    for action, elem in context:
        if action in ('start','end'):
            namespace, element_name = separate_namespace(elem.tag)
            if action in ('start'):
                if last_action==None:
                    newline = ''
                    indent = ''
                elif last_action=='start':
                    newline = '\n'
                    indent = ' ' * level * indent_size
                else:
                    newline = ',\n'
                    indent = ' ' * level * indent_size
                level += 1
                
                if elem.text:
                    text = '"{0}"'.format(elem.text)
                else:
                    text = ''
                output.write('{newline}{indent}{factory}.{tag}({text}'.format(
                    newline = newline,
                    indent = indent,
                    factory = get_factory_object(namespace),
                    tag = element_name,
                    text = text,
                ))
            elif action in ('end'):
                level -= 1
                if last_action == 'start':
                    newline1 = ''
                    indent = ''
                    newline2 = ''
                else:
                    newline1 = '\n'
                    indent = ' ' * level * indent_size
                    newline2 = ''
                output.write('{newline1}{indent}){newline2}'.format(
                    newline1 = newline1,
                    indent = indent,
                    newline2 = newline2
                ))
                
#        elif action == 'start-ns':
#            print("Level {level} - {action}: {elem}".format(
#                level=level, action=action, elem=elem)
#            )
#        else:
#            print(action)
#            pass
        last_action = action
    import ipdb; ipdb.set_trace()
    
    return str