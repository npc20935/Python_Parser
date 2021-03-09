import pygal
from pygal_maps_world.i18n import COUNTRIES

worldMap = pygal.maps.world.World()
worldMap.title = "World Map"
for countryCode in sorted(COUNTRIES.keys()):
    # print("國家碼", countryCode, "國家名", COUNTRIES[countryCode])
    worldMap.add(COUNTRIES[countryCode], [countryCode])
worldMap.render_to_file('World_Map.svg')