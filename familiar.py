# Import libraries
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency

# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')

# Print lifespan data
print(lifespans.head())

# Save lifespans for vein pack subscribers
vein_pack_lifespans = lifespans.lifespan[lifespans.pack == 'vein']

# Calculate average lifespan for vein pack
print(np.mean(vein_pack_lifespans))

# Run one-sample t-test
tstat, pval = ttest_1samp(vein_pack_lifespans, 73)
print(pval)

# Save lifespans for artery pack subscribers
artery_pack_lifespans = lifespans.lifespan[lifespans.pack == 'artery']

# Calculate average lifespan for artery pack
print(np.mean(artery_pack_lifespans))

# Run two-sample t-test
tstat, pval = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print(pval)

# Print iron data
print(iron.head())

# Create contingency table
Xtab = pd.crosstab(iron.pack, iron.iron)
print(Xtab)

# Run Chi-Square test
chi2, pval, dof, exp = chi2_contingency(Xtab)
print(pval)

