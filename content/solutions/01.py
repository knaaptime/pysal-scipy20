"""
solution for notebook 01
"""
fj6 = mapclassify.FisherJenks(gdf.median_home_value, k=6)
gdf['fj6yb'] = fj6.yb
gdf['county'] = [geoid[:5] for geoid in gdf.geoid]

for county in counties:
    f, ax = plt.subplots(1, figsize=(12, 8))
    gdf[gdf.county==county].plot(column='fj6yb', categorical=True, k=6, ax=ax,
        edgecolor='grey', legend=True, cmap='Blues', alpha=0.6)
    plt.title(county)
    ax.set_axis_off()
    plt.show()
