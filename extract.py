import fiona
from shapely.geometry import shape, mapping

grid = fiona.open('data/hot_osmtm_616.json', 'r')
print grid

for task in grid:
    print task['id']
    gns = fiona.open('data/li.shp', 'r')
    polygon = shape(task['geometry'])

    schema = gns.schema.copy()
    with fiona.collection('export/gns_%s.shp' % task['id'], 'w', 'ESRI Shapefile', schema=gns.schema, crs=gns.crs) as output:
        for point in gns:
            geom = shape(point['geometry'])
            if geom.within(polygon):
                output.write({'properties': point['properties'], 'geometry': mapping(shape(geom))})
