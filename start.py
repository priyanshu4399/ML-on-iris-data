import sepal_knn,petal_knn,sepal_petal_knn
import sepal_nb,petal_nb,sepal_petal_nb
import sepal_dt,petal_dt,sepal_petal_dt
import sepal_lg,petal_lg,sepal_petal_lg
import predict_sepal_knn,predict_petal_knn,predict_sepal_petal_knn
import predict_sepal_nb,predict_petal_nb,predict_sepal_petal_nb
import predict_sepal_dt,predict_petal_dt,predict_sepal_petal_dt
import predict_sepal_lg,predict_petal_lg,predict_sepal_petal_lg
from plot import *

split=0.70

def analyse():
       while True:
              print('\nCHOOSE Part of Iris flower to analyse algorithms:-')
              print('1:SEPAL length & width')
              print('2:PETAL length & width')
              print('3:SEPAL and PETAL')
              print('4:Back to SELECT OPERATION\n')
              a_choice=input("ENTER OPTION:")
              if a_choice=='1':
                     while True:
                            print("Algorithm is Analysed....\n")
                            print("How you want to view")
                            print("1:as statements")
                            print("2:as Plot")
                            print("3:back to SELECT Part")
                            ac=input("Enter view option:")
                            if ac=='1':
                                   print("\nRESULTS:-")
                                   print("Accuracy of knn with Sepal:",sepal_knn.accuracy(split))
                                   print("Accuracy of Naive Bayes with Sepal:",sepal_nb.accuracy(split))
                                   print("Accuracy of Decision Tree with Sepal:",sepal_dt.accuracy(split))
                                   print("Accuracy of Logical Regression with Sepal:",sepal_lg.accuracy(split))
                            elif ac=='2':
                                   sepal_bar_graph()
                            elif ac=='3':
                                   break
                            else:
                                   print("ENTER VALID CHOICE...!")
              elif a_choice=='2':
                     while True:
                            print("Algorithm is Analysed....\n")
                            print("How you want to view")
                            print("1:as statements")
                            print("2:as Plot")
                            print("3:back to SELECT Part")
                            ac=input("Enter view option:")
                            if ac=='1':
                                   print("\nRESULTS:-")
                                   print("Accuracy of knn with Petal:",petal_knn.accuracy(split))
                                   print("Accuracy of Naive Bayes with Petal:",petal_nb.accuracy(split))
                                   print("Accuracy of Decision Tree with Petal:",petal_dt.accuracy(split))
                                   print("Accuracy of Logical Regression with Petal:",petal_lg.accuracy(split))
                            elif ac=='2':
                                   petal_bar_graph()
                            elif ac=='3':
                                   break
                            else:
                                   print("ENTER VALID CHOICE...!")

              elif a_choice=='3':
                     while True:
                            print("Algorithm is Analysed....\n")
                            print("How you want to view")
                            print("1:as statements")
                            print("2:as Plot")
                            print("3:back to SELECT Part")
                            ac=input("Enter view option:")
                            if ac=='1':
                                   print("\nRESULTS:-")
                                   print("Accuracy of knn with Sepal & Petal:",sepal_petal_knn.accuracy(split))
                                   print("Accuracy of Naive Bayes with Sepal & Petal:",sepal_petal_nb.accuracy(split))
                                   print("Accuracy of Decision Tree with Sepal & Petal:",sepal_petal_dt.accuracy(split))
                                   print("Accuracy of Logical Regression with Sepal & Petal:",sepal_petal_lg.accuracy(split))
                            elif ac=='2':
                                   sepal_petal_bar_graph()
                            elif ac=='3':
                                   break
                            else:
                                   print("ENTER VALID CHOICE...!")

              elif a_choice=='4':
                     break
              else:
                     print("ENTER VALID CHOICE...!")
                                 
       
def predict():
       while True:
              print('\nPREDICT Iris Species using:-')
              print('1:SEPAL length & width')
              print('2:PETAL length & width')
              print('3:SEPAL and PETAL')
              print('4:Back to SELECT OPERATION\n')
              p_choice=input("ENTER OPTION:")
              if p_choice=='1':
                     print("\nPrediction using KNN")
                     print(">predicted:",predict_sepal_knn.predict(split))
                     print("\nPrediction using Naive Bayes")
                     print(">predicted:",predict_sepal_nb.predict(split))
                     print("\nPrediction using Decision Tree")
                     print(">predicted:",predict_sepal_dt.predict(split))
                     print("\nPrediction using Logical Regression")
                     print(">predicted:",predict_sepal_lg.predict(split))
              elif p_choice=='2':
                     print("\nPrediction using KNN")
                     print(">predicted:",predict_petal_knn.predict(split))
                     print("\nPrediction using Naive Bayes")
                     print(">predicted:",predict_petal_nb.predict(split))
                     print("\nPrediction using Decision Tree")
                     print(">predicted:",predict_petal_dt.predict(split))
                     print("\nPrediction using Logical Regression")
                     print(">predicted:",predict_petal_lg.predict(split))
              elif p_choice=='3':
                     print("\nPrediction using KNN")
                     print(">predicted:",predict_sepal_petal_knn.predict(split))
                     print("\nPrediction using Naive Bayes")
                     print(">predicted:",predict_sepal_petal_nb.predict(split))
                     print("\nPrediction using Decision Tree")
                     print(">predicted:",predict_sepal_petal_dt.predict(split))
                     print("\nPrediction using Logical Regression")
                     print(">predicted:",predict_sepal_petal_lg.predict(split))
              elif p_choice=='4':
                     break                     
              else:
                     print("ENTER VALID CHOICE...!")
             

def main():
       print("<------Welcome to Iris Data Prediction & Algorithms Analysis Project------>")
       while True:
              print('\nOPERATION:')
              print('1:Analyse algorithms')
              print('2:Predict iris species')
              print('3:Exit')
              choice=input("\nSELECT OPERATION :")             
              if choice=='1': 
                     analyse()
              elif choice=='2':
                     predict()
              elif choice=='3':
                     break
              else:
                     print("ENTER VALID  CHOICE...!")                           
       print("visit again....\n ~ Developed by Priyanshu")                           
main()
