augmented_df = data_df.copy()
augmented_df.loc[:,'img'] = augmented_df.loc[:,'img'].apply(flip_image)
augmented_df.loc[:,'steering'] = augmented_df.loc[:,'steering'].apply(reverse_steering)
data_df = pd.concat([data_df,augmented_df])
data_df = shuffle(data_df,random_state = 0)