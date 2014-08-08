Workflow
========

 - Load .csv file in CartoDB
 - Export as GeoJSON
 - Remove unrequired fields using jq

   {{{
   ./jq 'del(.features[].properties.cartodb_id,.features[].properties.created_at,.features[].properties.updated_at)' gnis_liberia_li_2014_03_23_ppl_osm.geojson > gnis_liberia_li_2014_03_23_ppl_osm_new.geojson
   }}}

 - create venv with requirements
 - launch
   {{{
   python extract.py
   }}}
 - launch
   {{{
   sh convert.sh
   }}}
