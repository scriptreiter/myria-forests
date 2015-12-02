def denormalize_file(file_name, out_name):
  with open(file_name, 'r') as data_file:
    with open(out_name, 'w') as out_file:
      for i,entry in enumerate(data_file):
        info = entry.rstrip().split(',')
    
        # Write out entries for every feature
        for j,feature in enumerate(info):
          out_file.write(','.join([str(col) for col in [i, j, feature]]) + '\n')


denormalize_file('train.csv', 'train_denorm.csv')
denormalize_file('test.csv', 'test_denorm.csv')
