import numpy as np

#minimising data consumed for each value hmm

def reducememory(df):
	initial_mem = df.memory_usage().sum/1024**2

	for col in df.columns:
		min_col = df[col].min()
		max_col = df[col].max()
		if df[col].dtype != object:

			if str(df[col].dtype) == "int":
				

				if min_col > np.iinfo(np.int8).min and max_col < np.iinfo(np.int8).max :
					df[col] = df[col].astype(np.int8)
				elif min_col > np.iinfo(np.int16).min and max_col < np.iinfo(np.int16).max :
					df[col] = df[col].astype(np.int16)
				elif min_col > np.iinfo(np.int32).min and max_col < np.iinfo(np.int32).max :
					df[col] = df[col].astype(np.int32)
				elif min_col > np.iinfo(np.int64).min and max_col < np.iinfo(np.int64).max :
					df[col] = df[col].astype(np.int64)
			else:
				if min_col > np.finfo(np.float16) and max_col < np.finfo(np.float16):
					df[col] = df[col].astype(np.float16)
				elif min_col > np.finfo(np.float32) and max_col < np.finfo(np.float32):
					df[col] = df[col].astype(np.float32)
				else:
					df[col] = df[col].astype(np.float64)
		else:
			df[col] = df[col].astype('category')

		final_mem = df.memory_usage.sum()/1024**2

		print(f"Initial memory : {initial_mem}\n Final Memory : {final_mem}\n")
		

		return df



