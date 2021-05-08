# Import sas7bdat using sas7bdat 
from sas7bdat import SAS7BDAT
with SAS7BDAT('posts-100.sas7bdat') as sas_file:    
	users_sas_df = sas_file.to_data_frame()
sas_file
dir(sas_file)
sas_file.column_names
sas_file.header
type(users_sas_df)

# Using pandas
import pandas as pd
posts_sas = pd.read_sas('posts-100.sas7bdat')
type(posts_sas)
posts_sas.head()
posts_sas.columns
posts_sas_reader = pd.read_sas('posts-100.sas7bdat', chunksize=10)
posts_sas_reader.read()

#-----------

# Import stata with pandas
import pandas as pd
posts_stata = pd.read_stata('posts-100.dta')
type(posts_stata)
dir(posts_stata)
posts_stata.columns
posts_stata.head()

#------------

# Import hdf5 using h5py
import h5py
file = h5py.File("posts-100.h5",'r')
dataset = file['posts']
for x in dataset['table']:
    print(x)

# Using pandas
import pandas as pd
posts_hdf = pd.read_hdf('posts-100.h5', 'posts')
posts_hdf.columns
posts_hdf.keys()
pd.read_hdf('posts-100.h5', 'posts', start=2, stop=5, columns=['CreationDate','Title','Tags']).head()
pd.read_hdf('posts-100.h5', 'posts', columns=['Score', 'Tags'], where='Score>10 or Tags = "<machine-learning>"').head()

#-----------
# Import matlab files using scipy.io
import scipy.io
posts_mat = scipy.io.loadmat('posts-100.mat')
type(posts_mat)
posts_mat.keys()
posts_mat['posts']

#-----------

# Import pickle files using the pickle library
import pickle
with open('posts-100.pkl.gz', 'rb') as pickle_file:
    posts_pickle = pickle.load(pickle_file)
type(posts_pickle)
posts_pickle.columns
posts_pickle.head()

# Import using pandas
import pandas as pd
posts_pickle = pd.read_pickle('posts-100.pkl')
type(posts_pickle)
posts_pickle.columns
posts_pickle.head()


