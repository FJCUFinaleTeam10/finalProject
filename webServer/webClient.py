# now let's save the visualization into the temp file and render it
from webserver import NamedTemporaryFile
tmp = NamedTemporaryFile()
folium_map.save(tmp.name)
with open(tmp.name) as f:
    folium_map_html = f.read()

run_html_server(folium_map_html)