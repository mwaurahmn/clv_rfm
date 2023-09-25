### DATA CLEANING ###

# Eliminate duplicate rows
def duplicate_rows(df):
    '''
    The function takes a dataframe.
    Counts duplicate entries.
    Eliminates the duplicates.
    Confirms all duplicate entries have been eliminated.
    Returns the respective counts and cleaned dataframe.
    '''
    b_duplicates = df.duplicated().sum()
    df = df.drop_duplicates()
    a_duplicates = df.duplicated().sum()
    return (b_duplicates, a_duplicates, df)

### PRODUCT BUNDLING ###

# Get list of antecedents
def antecedents_list(rules):
    '''
    The function takes the association rules dataframe.
    Converts the antecedents column into a list.
    Returns the list.
    '''
    antecedents = list(rules['antecedents'])
    ante_list = []
    for item in antecedents:
        i, = item # item is a frozenset
        ante_list.append(i)
    return ante_list

# Propose product bundling
def propose_bundles(customer_cart, rules, n = 3):
    '''
    The function proposes products ideal for bundling based on the contents of the customer's cart.

    Parameters
    -----------
    customer_cart : Set of items in the customer's cart (antecedents).
    rules : DataFrame outlining the association rules.
    n : Number of products proposed. (Default: 3)

    Returns
    --------
    A list of the proposed items (consequents).
    '''
    bundle = []
    bundle_set = []
    for index, row in rules.iterrows():
        antecedents = set(row['antecedents'])
        if antecedents.issubset(customer_cart):
            consequents = set(row['consequents'])
            bundle.extend(consequents.difference(customer_cart))
    for item in bundle:
        if item not in bundle_set:
            bundle_set.append(item)
    return bundle_set