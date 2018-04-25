import numpy as np
import h5py


# create random matrices
matrix1 = np.random.random(size=(1000, 1000))

# create dataset contains matrix1 & matrix2
with h5py.File('./hdf5_dataset.h5', 'w') as hdf:
  dataset = hdf.create_dataset('dataset', data=matrix1)
  dataset.attrs['Class'] = 'Data'
  dataset.attrs['Date'] = '19:36'


with h5py.File('./hdf5_dataset.h5', 'r') as hdf:
  data = hdf.get('dataset')
  keys = list(data.attrs.keys())
  vals = list(data.attrs.values())
  for k, v in zip(keys, vals):
    print(k + ' : ' + v)
