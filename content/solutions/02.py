##### 1

knn4 = KNN.from_dataframe(df, k=4)
print(f"% Non-zero weights in KNN: {knn4.pct_nonzero}")

rk = Rook.from_dataframe(df)
print(f"% Non-zero weights in Rook: {rk.pct_nonzero}")

##### 2

tract_ids = []
for i in knn4.neighbors:
    if len(knn4[i]) > len(rk[i]):
        tract_ids.append(i)
print(f"There are {len(tract_ids)} that have fewer Rook neighbors than KNN neighbors")


##### 3

identical = []
qn = Queen.from_dataframe(df)
for i in rk.neighbors:
    if set(rk.neighbors[i]) == set(qn.neighbors[i]):
        identical.append(i)
print(f"There are {len(identical)} that have identical Queen and Rook neighbors")

