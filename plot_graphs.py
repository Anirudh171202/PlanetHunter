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

def non_exoplanets(df):
    labels_1=[100,200,300]
    for i in labels_1:
        plt.hist(df.iloc[i,:], bins=200)
        plt.title("Gaussian Histogram for non_exoplanets")
        plt.xlabel("Flux values")
        plt.show()
def exoplanets(df):
    labels_1=[16,21,25]
    for i in labels_1:
        plt.hist(df.iloc[i,:], bins=200)
        plt.title("Gaussian Histogram for exoplanets")
        plt.xlabel("Flux values")
        plt.show()
