from sklearn.decompostion  import PCA
def reduce_features(df):
    x_train= PCA().fit_transform(x_train)
    x_test= PCA().transform(x_test)
    total= sum(PCA().explained_variance_)
    curr_var=0
    while curr_var/total < 0.94:
        curr_var += PCA().explained_variance_[k]
        k=k+1
    print(k)
    
