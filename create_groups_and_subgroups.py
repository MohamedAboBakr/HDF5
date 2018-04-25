import numpy as np
import h5py

matrix1 = np.random.random(size=(1000, 1000))
matrix2 = np.random.random(size=(1000, 1000))
matrix3 = np.random.random(size=(1000, 1000))
matrix4 = np.random.random(size=(1000, 1000))

with h5py.File('./hdf5_groups.h5', 'w') as hdf:
  # create group1
  g1 = hdf.create_group('Group1')
  # create datasets inside g1
  g1.create_dataset('dataset1', data=matrix1)
  g1.create_dataset('dataset2', data=matrix2)

  # create group2 with subgroups g3 & g4
  g3 = hdf.create_group('Group2/SubGroup1')
  g3.create_dataset('dataset3', data=matrix3)

  g4 = hdf.create_group('Group2/SubGroup2')
  g4.create_dataset('dataset4', data=matrix4)
