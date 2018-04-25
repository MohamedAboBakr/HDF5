import numpy as np
import h5py
import os


def print_size(file_name):
  try:
    st = os.stat(file_name)
    print(str(st.st_size) + ' bytes')
  except OSError as e:
    print(e)



# create dataset without compression
matrix1 = [['abcde'] * 1000] * 1000
matrix2 = [['abcde'] * 1000] * 1000
matrix3 = [['abcde'] * 1000] * 1000
matrix4 = [['abcde'] * 1000] * 1000

with h5py.File('./hdf5_groups_no_compression.h5', 'w') as hdf:
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


# create dataset with compression

with h5py.File('./hdf5_groups_compressed.h5', 'w') as hdf:
  # create group1
  g1 = hdf.create_group('Group1')
  # create datasets inside g1
  g1.create_dataset('dataset1', data=matrix1, compression="gzip", compression_opts=9)
  g1.create_dataset('dataset2', data=matrix2, compression="gzip", compression_opts=9)

  # create group2 with subgroups g3 & g4
  g3 = hdf.create_group('Group2/SubGroup1')
  g3.create_dataset('dataset3', data=matrix3, compression="gzip", compression_opts=9)

  g4 = hdf.create_group('Group2/SubGroup2')
  g4.create_dataset('dataset4', data=matrix4, compression="gzip", compression_opts=9)


print_size('./hdf5_groups_no_compression.h5')
print_size('./hdf5_groups_compressed.h5')
