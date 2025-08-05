import pandas as pd 


def preprocess(df, region_df):
    #Filtering for summer olyampics
    df = df[df['Season']=='Summer']
    #Merge with region_df 
    df = df.merge(region_df, on="NOC",how='left')
    #Drop Duplicates
    df.drop_duplicates(inplace=True)
    #One Hot encoding medals
    df = pd.concat([df,pd.get_dummies(df['Medal'])],axis=1)
    return df