import fiona
from shapely.geometry import shape, mapping

grid = fiona.open('data/hot_osmtm_619.json', 'r')
print grid

for task in grid:
    print task['id']
    gns = fiona.open('data/gnis_liberia_li_2014_03_23_ppl_osm_new.geojson', 'r')
    polygon = shape(task['geometry'])

    schema = gns.schema.copy()
    p = task['properties']
    filename = 'export/gns_%s_%s_%s.shp' % (p['zoom'], p['x'], p['y'])
    with fiona.collection(filename, 'w', 'ESRI Shapefile', schema=gns.schema, crs=gns.crs) as output:
        for point in gns:
            geom = shape(point['geometry'])
            if geom.within(polygon):
                output.write({'properties': point['properties'], 'geometry': mapping(shape(geom))})
