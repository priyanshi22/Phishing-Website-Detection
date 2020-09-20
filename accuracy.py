import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.tree import DecisionTreeClassifier

def acc1():
	legitimate_urls = pd.read_csv(r"C:\Users\Dell\Desktop\Final\extracted_csv_files\l.csv")
	phishing_urls = pd.read_csv(r"C:\Users\Dell\Desktop\final\extracted_csv_files\p.csv")

	# print(len(legitimate_urls))
	# print(len(phishing_urls))

	urls = legitimate_urls.append(phishing_urls)
	urls.head(5)

	urls = urls.drop(urls.columns[[0,3,5,9,17]],axis=1)
	# print(urls.columns)

	urls = urls.sample(frac=1).reset_index(drop=True)

	urls_without_labels = urls.drop('label',axis=1)
	urls_without_labels.columns
	labels = urls['label']

	random.seed(100)
	data_train, data_test, labels_train, labels_test = train_test_split(urls_without_labels, labels, test_size=0.20, random_state=100)
	# print(len(data_train),len(data_test),len(labels_train),len(labels_test))
	# print(labels_train.value_counts())
	# print(labels_test.value_counts())

	DTmodel = DecisionTreeClassifier(random_state=0)
	DTmodel.fit(data_train,labels_train)
	pred_label = DTmodel.predict(data_test)
	print("Accuracy before adding both the features with Decision Tree: ",accuracy_score(labels_test,pred_label)) 
	
def acc2():
	legitimate_urls = pd.read_csv(r"C:\Users\Dell\Desktop\Final\extracted_csv_files\l.csv")
	phishing_urls = pd.read_csv(r"C:\Users\Dell\Desktop\final\extracted_csv_files\p.csv")
	urls = legitimate_urls.append(phishing_urls)
	urls.head(5)
	urls = urls.drop(urls.columns[[0,3,5]],axis=1)
	urls = urls.sample(frac=1).reset_index(drop=True)
	urls_without_labels = urls.drop('label',axis=1)
	urls_without_labels.columns
	labels = urls['label']
	random.seed(100)
	data_train, data_test, labels_train, labels_test = train_test_split(urls_without_labels, labels, test_size=0.20, random_state=100)
	DTmodel = DecisionTreeClassifier(random_state=0)
	DTmodel.fit(data_train,labels_train)
	pred_label = DTmodel.predict(data_test)
	print("Accuracy after adding both the features with Decision Tree: ",accuracy_score(labels_test,pred_label)) 

def acc3():
	legitimate = pd.read_csv(r"C:\Users\Dell\Desktop\Final\extracted_csv_files\l.csv")
	phishing = pd.read_csv(r"C:\Users\Dell\Desktop\Final\extracted_csv_files\p.csv")
	url = legitimate.append(phishing)
	url.head(5)
	url = url.drop(url.columns[[0,3,5,9,17]],axis=1)
	url = url.sample(frac=1).reset_index(drop=True)
	urls_without_labels = url.drop('label',axis=1)
	urls_without_labels.columns
	labels = url['label']
	random.seed(100)
	data_train, data_test, labels_train, labels_test = train_test_split(urls_without_labels, labels, test_size=0.20, random_state=100)
	RFmodel = RandomForestClassifier()
	RFmodel.fit(data_train,labels_train)
	rf_pred_label = RFmodel.predict(data_test)
	print("Accuracy before adding both the features with Random Forest: ",accuracy_score(labels_test,rf_pred_label) )
	return accuracy_score(labels_test,rf_pred_label)

def acc4():
	legitimate = pd.read_csv(r"C:\Users\Dell\Desktop\Final\extracted_csv_files\l.csv")
	phishing = pd.read_csv(r"C:\Users\Dell\Desktop\Final\extracted_csv_files\p.csv")
	url = legitimate.append(phishing)
	url.head(5)
	url = url.drop(url.columns[[0,3,5]],axis=1)
	url = url.sample(frac=1).reset_index(drop=True)
	urls_without_labels = url.drop('label',axis=1)
	urls_without_labels.columns
	labels = url['label']
	random.seed(100)
	data_train, data_test, labels_train, labels_test = train_test_split(urls_without_labels, labels, test_size=0.20, random_state=100)
	RFmodel = RandomForestClassifier()
	RFmodel.fit(data_train,labels_train)
	rf_pred_label = RFmodel.predict(data_test)
	print("Accuracy after adding both the features with Random Forest: ",accuracy_score(labels_test,rf_pred_label) )
	return accuracy_score(labels_test,rf_pred_label)


