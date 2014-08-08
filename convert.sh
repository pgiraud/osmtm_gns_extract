#!/bin/bash
for file in export/*.shp
do
    echo $file 
    ogr2ogr -f 'CSV' $file.csv $file
done
