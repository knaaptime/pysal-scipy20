"""
Solution for nb 00
"""
scag['county'] = scag.geoid.str[:5]     # add a column with the derived fips codes for a tract's county
counties = scag.county.unique()         # get the unique county codes
for county in counties:                 # loop over the counties and create the shapefiles
    gdf = scag[scag.county==county]
    gdf.to_file(f'data/{county}.shp')