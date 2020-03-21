from sklearn.preprocessing import StandardScaler, normalize
from sklearn.decomposition import PCA
def data_normalize2(df):
    for col in df.columns:
        range_col = df[col].max() - df[col].min()
        mean_col = (df[col].max() + df[col].min())/2
        for val in df[col]:
            df[col][val] = (2*(df[col][val]-mean_col)/range_col).astype(np.int8)
    print(df.head())

def data_normalize(x_train, x_test):
    x_train = normalized = normalize(x_train)
    x_test = normalize(x_test)

def gaussian(x_train, x_test):
    x_train = filtered = ndimage.filters.gaussian_filter(x_train, sigma=10)
    x_test = ndimage.filters.gaussian_filter(x_test, sigma=10)
    return x_train,x_test
def dimensionality_red(x_train, x_test, alpha):
    pca = PCA() 
    X_train = pca.fit_transform(X_train)
    X_test = pca.transform(X_test)
    total=sum(pca.explained_variance_)
    k=0
    current_variance=0
    while current_variance/total < alpha:
        current_variance += pca.explained_variance_[k]
        k=k+1
    pca = PCA(n_components=37)
    x_train = pca.fit_transform(x_train)
    x_test = pca.transform(x_test)
    return x_train, x_test

def resample(x_train,y_train):
    sm = SMOTE(random_state=27, ratio = 1.0)
    x_train_res, y_train_res = sm.fit_sample(x_train, y_train.ravel())
    return x_train_res, y_train_res

