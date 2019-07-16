import sklearn
import random


def convert_string_to_float(lst,n):
    column=0
    while column<4:
        lst[column]=float(lst[column])
        column+=1
    return lst


def loadDataset(split,train=[],test=[],train_labels=[],test_labels=[]):
    for line in open(r'iris.txt','r'):
        temp=convert_string_to_float(line[0:-1].split(','),4)
        if random.random()<split:
            train.append(temp[0:-1])
            train_labels.append(temp[-1])
        else:
            test.append(temp[0:-1])
            test_labels.append(temp[-1])
    return train,test,train_labels,test_labels


def accuracy(split):
    train,test,train_labels,test_labels = loadDataset(split)
    from sklearn.linear_model import LogisticRegression
    logisticRegr=LogisticRegression(solver='lbfgs',multi_class='multinomial',max_iter=1000)
    logisticRegr.fit(train,train_labels)
    predictions=logisticRegr.predict(test)
    score=logisticRegr.score(test,test_labels)
    acc=score*100
    acc=round(acc,2)    
    #print('Accuracy of Logistic Regression with Sepal & Petal : '+str(acc)+' %')
    return acc
     
#accuracy(0.7)
