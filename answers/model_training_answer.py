model.fit(train_imgs, train_labels,
      nb_epoch= 5,               
      validation_data = (test_imgs, test_labels),
      callbacks = [ ModelCheckpoint("./model_temp.h5", monitor='val_loss', verbose= 1, save_best_only=True, mode='min')
                 ]
      )