counter = 0
for i, neighbor in enumerate(knn8_bad.neighbors):

    if not set(knn8_bad.neighbors[neighbor]) == set(knn8.neighbors[neighbor]):
                                      counter +=1
print(f" {counter} ({np.round(len(knn8_bad.neighbors)/counter, 3)}%) of the tracts have incorrect neighbors")