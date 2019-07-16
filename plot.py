import sepal_knn,petal_knn,sepal_petal_knn
import sepal_nb,petal_nb,sepal_petal_nb
import sepal_dt,petal_dt,sepal_petal_dt
import sepal_lg,petal_lg,sepal_petal_lg

split=0.70

knnS=sepal_knn.accuracy(split)
knnP=petal_knn.accuracy(split)
knnSP=sepal_petal_knn.accuracy(split)
nbS=sepal_nb.accuracy(split)
nbP=petal_nb.accuracy(split)
nbSP=sepal_petal_nb.accuracy(split)
dtS=sepal_dt.accuracy(split)
dtP=petal_dt.accuracy(split)
dtSP=sepal_petal_dt.accuracy(split)
lgS=sepal_lg.accuracy(split)
lgP=petal_lg.accuracy(split)
lgSP=sepal_petal_lg.accuracy(split)
#print(knnS,knnP,knnSP,nbS,nbP,nbSP,dtS,dtP,dtSP,lgS,lgP,lgSP)
import matplotlib.pyplot as plt
import numpy as np

def sepal_bar_graph():
    algorithms=('KNN','Naive Bayes','Decision Tree','Logical Regression')
    x_pos=np.arange(len(algorithms))
    accuracy=[knnS,nbS,dtS,lgS]
    plt.bar(x_pos,accuracy,align='center')
    plt.xticks(x_pos,algorithms)
    plt.ylabel('Accuracy')
    plt.title('Accuracy of Algorithms')
    plt.show()
    
def petal_bar_graph():
    algorithms=('KNN','Naive Bayes','Decision Tree','Logical Regression')
    x_pos=np.arange(len(algorithms))
    accuracy=[knnP,nbP,dtP,lgP]
    plt.bar(x_pos,accuracy,align='center')
    plt.xticks(x_pos,algorithms)
    plt.ylabel('Accuracy')
    plt.title('Accuracy of Algorithms')
    plt.show()
    
def sepal_petal_bar_graph():
    algorithms=('KNN','Naive Bayes','Decision Tree','Logical Regression')
    x_pos=np.arange(len(algorithms))
    accuracy=[knnSP,nbSP,dtSP,lgSP]
    plt.bar(x_pos,accuracy,align='center')
    plt.xticks(x_pos,algorithms)
    plt.ylabel('Accuracy')
    plt.title('Accuracy of Algorithms')
    plt.show()

if __name__=='__main__':    
    sepal_bar_graph()
    petal_bar_graph()
    sepal_petal_bar_graph()
    
    
