from PIL import Image
import numpy as np
def pca(x):
    #x:訓練データを行ベクトルにしたものをまとめ、行列にしたもの。
    #写像fから出てきた行列を出力。
    num_data,dim=x.shape#行列xの次元を取得。
    #センタリング
    mean_x=x.mean(axis=0)#行方向の平均をとる。列ベクトルになる。
    x=x-mean_x
    if dim>num_data:
        M=np.dot(x,x.T)#xとx^tの積
        e,EV=np.linalg.eigh(M) #Mの固有値e,固有ベクトルEVを求める。
        tmp=np.dot(x.T,EV).T
        V=tmp[::-1]
        S=np.sqrt(e)[::-1]
        for i in range(V.shape[1]):
            V[:i]/=S
    else:
        U,S,V=np.linalg.svd(x)
        V=V[:num_data]
        
    return V,S,mean_x