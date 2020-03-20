import matplotlib.pyplot as plt
from pylab import rcParams

def flux_dist(df):
	plt.title("Fluxvals")
	plt.xlabel("vals")
	plt.ylabel("intensts")

	plt.plot(df.iloc[0,:])
	plt.plot(df.iloc[1,])
	plt.plot(df.iloc[2,])
	plt.show()


