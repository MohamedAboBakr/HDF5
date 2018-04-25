import pandas as pd
import h5py

data = {
    "Player": ["M.Salah", "C.Ronaldo", "Immobile", "Messi"],
    "Goals": [43, 42, 41, 40]
}

df = pd.DataFrame(data, columns=['Player', 'Goals'])

try:
  hdf = pd.HDFStore('./hdf_pandas.h5')
  hdf.put('Df', df, format='table', data_columns=True)
  hdf.close()
except IOError as e:
  print(e)
