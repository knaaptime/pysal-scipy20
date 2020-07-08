##### 1)

# create orange county data
oc = scag[scag.geoid.str[:5] == '06059']

# create cluster models where k==5,8
oc5 = KMeans(n_clusters=5).fit(scaler.fit_transform(oc[columns]))
oc8 = KMeans(n_clusters=8).fit(scaler.fit_transform(oc[columns]))

# calculate silhouette coefs and print them
sil5 = silhouette_score(scaler.fit_transform(oc[columns]), oc5.labels_)
sil8 = silhouette_score(scaler.fit_transform(oc[columns]), oc8.labels_)

print(f'5-cluster solution: {sil5}')
print(f'8-cluster solution: {sil8}')


##### 2)

rside = scag[scag.geoid.str[:5] == '06065']

rside['affprop'] = AffinityPropagation(damping=0.8, preference=-100,).fit(scaler.fit_transform(rside[columns])).labels_
print(f'There are {len(rside.affprop.unique())} unique clusters in Riverside')

print(f"The average home price in cluster 3 is ${rside.groupby('affprop').mean()['median_home_value'][3].astype(int)}")

##### 3)

print("With distance band weights, the solution will be spatially-influenced but the clusters are not guaranteed to be contiguous")

