import sklearn
import random


def convert_string_to_float(lst,n):
    column=0
    while column<n:
        lst[column]=float(lst[column])
        column+=1
    return lst


def loadDataset(split,train=[],test=[],train_labels=[],test_labels=[]):
    for line in open(r'iris.txt','r'):
        temp=convert_string_to_float(line[0:-1].split(','),4)
        temp.pop(0)
        temp.pop(0)
        if random.random()<split:
            train.append(temp[0:-1])
            train_labels.append(temp[-1])
        else:
            test.append(temp[0:-1])
            test_labels.append(temp[-1])
    return train,test,train_labels,test_labels


def accuracy(split):
    train,test,train_labels,test_labels = loadDataset(split)
    from sklearn.naive_bayes import GaussianNB
    gnb=GaussianNB()
    model=gnb.fit(train,train_labels)     
    preds=gnb.predict(test)
    from sklearn.metrics import accuracy_score
    acc=accuracy_score(test_labels,preds)*100
    acc=round(acc,2)
    #print('Accuracy of Naive Bayes with Petal : '+str(acc)+' %')
    return acc
     
#accuracy(0.7)
