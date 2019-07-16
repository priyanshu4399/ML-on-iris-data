import sklearn
import random

def convert_to_float(lst):
    column=0
    while column<len(lst):
        lst[column]=float(lst[column])
        column+=1
    return lst


def loadDataset(split,train=[],test=[],train_labels=[],test_labels=[]):
    for line in open(r'iris.txt','r'):
        temp=line[0:-1].split(',')
        if random.random()<split:
            train.append(convert_to_float(temp[0:-1]))
            train_labels.append(temp[-1])
        else:
            test.append(convert_to_float(temp[0:-1]))
            test_labels.append(temp[-1])
    return train,test,train_labels,test_labels

def accuracy(split):
    train,test,train_labels,test_labels = loadDataset(split)
    #Building the model
    #Decision Tree algorithm
    from sklearn import tree
    clf=tree.DecisionTreeClassifier()
    clf=clf.fit(train,train_labels)
    preds=clf.predict(test)

    from sklearn.metrics import accuracy_score
    acc=accuracy_score(test_labels,preds)*100
    acc=round(acc,2)    
    #print('Accuracy of Decision Tree with Sepal & Petal : '+str(acc)+' %')
    return acc
               
#accuracy(0.7)
