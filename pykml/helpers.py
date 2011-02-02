from pykml.factory import KML_ElementMaker as K

def separate_namespace(qname):
    "Separate the namespace from the element"
    import re
    try:
        namespace, element_name = re.search('^{(.+)}(.+)$', qname).groups()
    except:
        namespace = None
        element_name = qname
    return namespace, element_name

def set_max_decimal_places(doc, max_decimals=4):
    "Reduces the number of decimal places used in elements"
    
    for el in doc.findall(".//{http://www.opengis.net/kml/2.2}longitude"):
        new_val = round(float(el.text), max_decimals)
        el.getparent().longitude = K.longitude(new_val)
    for el in doc.findall(".//{http://www.opengis.net/kml/2.2}latitude"):
        new_val = round(float(el.text), max_decimals)
        el.getparent().latitude = K.latitude(new_val)
    for el in doc.findall(".//{http://www.opengis.net/kml/2.2}altitude"):
        new_val = round(float(el.text), max_decimals)
        el.getparent().altitude = K.altitude(new_val)
    for el in doc.findall(".//{http://www.opengis.net/kml/2.2}heading"):
        new_val = round(float(el.text), max_decimals)
        el.getparent().heading = K.heading(new_val)
    for el in doc.findall(".//{http://www.opengis.net/kml/2.2}tilt"):
        new_val = round(float(el.text), max_decimals)
        el.getparent().tilt = K.tilt(new_val)
    for el in doc.findall(".//{http://www.opengis.net/kml/2.2}range"):
        new_val = round(float(el.text), max_decimals)
        el.getparent().range = K.range(new_val)
    # reduce decimals in the coordinate string using nested list comprehension
    for el in doc.findall(".//{http://www.opengis.net/kml/2.2}coordinates"):
        new_coord_string = ' '.join([
            ','.join([
                str(round(float(dimension), max_decimals))
                for dimension in vertex.split(',')
            ]) for vertex in el.text.split(' ')
        ])
        el.getparent().coordinates = K.coordinates(new_coord_string)

