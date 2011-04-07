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

def set_max_decimal_places(doc, max_decimals):
    "Reduces the number of decimal places used in elements"
    
    if max_decimals.has_key('longitude'):
        for el in doc.findall(".//{http://www.opengis.net/kml/2.2}longitude"):
            new_val = round(float(el.text), max_decimals['longitude'])
            el.getparent().longitude = K.longitude(new_val)
    if max_decimals.has_key('latitude'):
        for el in doc.findall(".//{http://www.opengis.net/kml/2.2}latitude"):
            new_val = round(float(el.text), max_decimals['latitude'])
            el.getparent().latitude = K.latitude(new_val)
    if max_decimals.has_key('altitude'):
        for el in doc.findall(".//{http://www.opengis.net/kml/2.2}altitude"):
            new_val = round(float(el.text), max_decimals['altitude'])
            el.getparent().altitude = K.altitude(new_val)
    if max_decimals.has_key('heading'):
        for el in doc.findall(".//{http://www.opengis.net/kml/2.2}heading"):
            new_val = round(float(el.text), max_decimals['heading'])
            el.getparent().heading = K.heading(new_val)
    if max_decimals.has_key('tilt'):
        for el in doc.findall(".//{http://www.opengis.net/kml/2.2}tilt"):
            new_val = round(float(el.text), max_decimals['tilt'])
            el.getparent().tilt = K.tilt(new_val)
    if max_decimals.has_key('range'):
        for el in doc.findall(".//{http://www.opengis.net/kml/2.2}range"):
            new_val = round(float(el.text), max_decimals['range'])
            el.getparent().range = K.range(new_val)
    # reduce decimals in the coordinate string using nested list comprehension
    for el in doc.findall(".//{http://www.opengis.net/kml/2.2}coordinates"):
        vertex_str_list = []
        for vertex in el.text.strip().split(' '):
            coord_list = vertex.split(',')
            if len(coord_list)==2:
                vertex_str_list.append(
                    '{lon},{lat}'.format(
                        lon=round(float(coord_list[0]), max_decimals['longitude']),
                        lat=round(float(coord_list[1]), max_decimals['latitude']),
                    )
                )
            else:
                vertex_str_list.append(
                    '{lon},{lat},{alt}'.format(
                        lon=round(float(coord_list[0]), max_decimals['longitude']),
                        lat=round(float(coord_list[1]), max_decimals['latitude']),
                        alt=round(float(coord_list[2]), max_decimals['altitude']),
                    )
                )
        new_coord_string = ' '.join(vertex_str_list).strip()
        el.getparent().coordinates = K.coordinates(new_coord_string)

