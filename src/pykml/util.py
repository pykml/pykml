""" pyKML Utility Module

The pykml.utility module provides utility functions that operate on KML 
documents
"""
import re

def count_elements(doc):
    "Counts the number of times each element is used in a document"
    summary = {}
    for el in doc.iter():
        try:
            namespace, element_name = re.search('^{(.+)}(.+)$', el.tag).groups()
        except:
            namespace = None
            element_name = el.tag
        if not summary.has_key(namespace):
            summary[namespace] = {}
        if not summary[namespace].has_key(element_name):
            summary[namespace][element_name] = 1
        else:
            summary[namespace][element_name] += 1
    return summary
    
def wrap_angle180(angle):
    # returns an angle such that -180 < angle <= 180
    try:
        # if angle is a sequence
        return [((a+180) % 360 ) - 180 for a in angle]
    except TypeError:
        return ((angle+180) % 360 ) - 180

def to_wkt_list(doc):
    '''converts all geometries to Well Know Text format'''
    from lxml import etree
    
    def ring_coords_to_wkt(ring):
        '''converts LinearRing coordinates to WKT style coordinates'''
        return(
            (
               ring.coordinates.text.strip()
            ).replace(' ','@@').replace(',',' ').replace('@@',', ')
        )
    
    ring_wkt_list = []
    context = etree.iterwalk(
             doc,
             events=("start",),
             tag="{http://www.opengis.net/kml/2.2}*",
    )
    for action, elem in context:
        if elem.tag in ['{http://www.opengis.net/kml/2.2}Polygon',
                        '{http://www.opengis.net/kml/2.2}MultiPolygon']:
            #print("%s: %s" % (action, elem.tag))
            if elem.tag == '{http://www.opengis.net/kml/2.2}Polygon':
                
                # outer boundary
                ringlist = [
                    '({0})'.format(
                        ring_coords_to_wkt(elem.outerBoundaryIs.LinearRing)
                    )
                ]
                for obj in elem.innerBoundaryIs:
                    ringlist.append(
                        '({0})'.format(
                            ring_coords_to_wkt(obj.LinearRing)
                        )
                    )
                
                wkt = 'POLYGON ({rings})'.format(rings=', '.join(ringlist))
                ring_wkt_list.append(wkt)
    return(ring_wkt_list)