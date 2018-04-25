import pandas as pd
import h5py


with pd.HDFStore('./hdf_pandas.h5', mode='r') as hdf:
  keys = hdf.keys()
  for key in keys:
    df = hdf.get(key)
    print(df.head())
