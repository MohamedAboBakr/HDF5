import numpy as np
import h5py

with h5py.File('./hdf5_dataset1.h5', 'r') as hdf:
  datasets_names = list(hdf.keys())
  for name in datasets_names:
    dataset = hdf.get(name)
    dataset = np.array(dataset)
    print(name, dataset.shape)
