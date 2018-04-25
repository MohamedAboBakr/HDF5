import numpy as np
import h5py

# create random matrices
matrix1 = np.random.random(size=(1000, 1000))
matrix2 = np.random.random(size=(10000, 100))

# create dataset contains matrix1 & matrix2


with h5py.File('./hdf5_dataset1.h5', 'w') as hdf:
  hdf.create_dataset('dataset1', data=matrix1)
  hdf.create_dataset('dataset2', data=matrix2)
