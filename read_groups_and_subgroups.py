import numpy as np
import h5py


def get_items(group, name, num_spaces):
  sp = ' ' * num_spaces
  print(sp + name)

  if type(group) is h5py._hl.dataset.Dataset:
    return

  items = list(group.keys())
  for item in items:
    get_items(group.get(item), item, num_spaces + 2)


try:
  hdf = h5py.File('./hdf5_groups.h5', 'r')
  get_items(hdf, 'Root', 0)
  hdf.close()

except IOError as e:
  print(e)
