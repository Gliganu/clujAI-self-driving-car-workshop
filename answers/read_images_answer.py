data_df.loc[:,'img'] = data_df.loc[:,'img_path'].progress_apply(read_image)