# csv geodata filter

 - filters geodata stored in csv filetypes by their haversine distance from a given coordinate
 - edit coords, radius, datafile in script and run

![imagen](https://user-images.githubusercontent.com/78174712/180298550-7f5bee8b-0a2a-4b86-9c32-b94272738f5d.png)
[view fullscreen](https://umap.openstreetmap.fr/es/map/canada-trip_790135)

## howto:

 1. make a route using [GraphHopper](https://graphhopper.com/maps/)
 2. export route to .gpx file format by hitting the `gpx` button below waypoint input, and selecting the `track` checkbox
 3. export points of interest data to .csv filetype
	if using overpass-turbo data mining utility, export data as .gpx & convert to .csv with gpx_converter:
	```
	$ pip install gpx-converter
	$ python3
	>>> from gpx_converter import Converter
	>>> Converter(input_file='sample.gpx').gpx_to_csv(output_file='output.csv')
	```
 4. edit `filter.py` to include all the necessary files (GPXfile, poi file)
 5. run `filter.py`
 6. view output as csv or graphically with [umap](https://umap.openstreetmap.fr/es/map/new/) (`ctrl+I` import out.csv)

## possible future expansions:

 - instead of only selecting points within radius of a given point, select points within radius of a given path (or google maps route), to narrow down candidates for visitation on a roadtrip
 - instead of only taking data from csv coordinates, also take data from alltrails to find hiking trails along the way/ nearby

## further info:

 - data for this project from [skytruth](https://skytruth.org/2015/10/mapping-abandoned-coal-mines/)
 - additional geodata can be obtained through the [overpass-turbo](https://overpass-turbo.eu/) utility
	- [guide](https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example)
	- [example map features](https://wiki.openstreetmap.org/wiki/ES:Objetos_del_mapa)
 - openstreetmap.org
 - [haversine formula derivation](https://web.archive.org/web/20200120134215/http://mathforum.org/library/drmath/view/51879.html)
 - [AMLIS database](https://www.osmre.gov/programs/e-amlis)
 - [metal mines](https://skytruth-org.carto.com/tables/mrds_pp_nam_comtype_b_m_null/public)
 - [metal mines ii](https://skytruth-org.carto.com/viz/8e8d33f1-9a26-442a-93be-365df5c94190/public_map)
 - [AML hazards and problem types](https://www.dep.pa.gov/Business/Land/Mining/AbandonedMineReclamation/AMLProgramInformation/Pages/AMLHazards.aspx)

 - an interesting story about a west virginia [mining disaster](https://www.cheat.org/about/history/)
