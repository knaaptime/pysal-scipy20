#### 1

results = {}

for i in scag.county.unique():

    results[i] = MultiInformationTheory(scag[scag.county==i], pop_groups).statistic
    print(f"{i} Info Theory: {results[i]}")


#### 2

rside_gini = GiniSeg(scag[scag.county=='Riverside'], group_pop_var='n_hispanic_persons', total_pop_var='n_total_pop')
vent_gini = GiniSeg(scag[scag.county=='Ventura'], group_pop_var='n_hispanic_persons', total_pop_var='n_total_pop')

print(f"\nRiverside Gini: {rside_gini.statistic}")
print(f"Venura Gini: {vent_gini.statistic}")
ginitest = TwoValueTest(rside_gini, vent_gini)
print(f"test significance level = {ginitest.p_value}")
ginitest.plot()

#### 3
decomp = DecomposeSegregation(SpatialDissim(scag[scag.county=='Riverside'], group_pop_var='n_hispanic_persons', total_pop_var='n_total_pop'),
                              SpatialDissim(scag[scag.county=='Ventura'], group_pop_var='n_hispanic_persons', total_pop_var='n_total_pop'))
decomp.plot('maps')