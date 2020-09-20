import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import feature

def getResult(url):

	legitimate_urls = pd.read_csv(r"C:\Users\Dell\Desktop\Final\extracted_csv_files\l.csv")
	phishing_urls = pd.read_csv(r"C:\Users\Dell\Desktop\Final\extracted_csv_files\p.csv")

	urls = legitimate_urls.append(phishing_urls)
	urls.head(5)
	urls = urls.drop(urls.columns[[0,3,5]],axis=1)
	urls = urls.sample(frac=1).reset_index(drop=True)
	urls_without_labels = urls.drop('label',axis=1)
	urls_without_labels.columns
	labels = urls['label']
	random.seed(100)
	data_train, data_test, labels_train, labels_test = train_test_split(urls_without_labels, labels, test_size=0.20, random_state=100)
	RFmodel = RandomForestClassifier()
	RFmodel.fit(data_train,labels_train)
	#url="https://github.com/philomathic-guy/Malicious-Web-Content-Detection-Using-Machine-Learning/tree/master/dataset"
	lst=feature.getAttributess(url)
	rf_pred_label = RFmodel.predict(lst)
	if rf_pred_label==1:
		return "Phishing URL"
	else:
		return "Legitimate URL"
	

