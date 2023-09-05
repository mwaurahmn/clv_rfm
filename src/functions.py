### DATA CLEANING ###

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