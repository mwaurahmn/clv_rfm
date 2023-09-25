# Data loading and preprocessing
import pandas as pd

# Visualization
import seaborn as sns
import matplotlib.pyplot as plt

# Visualization Display
plt.rcParams['font.size'] = 20
plt.rcParams['figure.figsize'] = (15, 8)

# Modeling - Association Rule Mining
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules