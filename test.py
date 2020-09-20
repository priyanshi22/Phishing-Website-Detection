import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import feature
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.utils import shuffle
from sklearn.tree import DecisionTreeClassifier
legitimate_urls = pd.read_csv(r"C:\Users\Tanu\Desktop\Final\extracted_csv_files\l.csv")
phishing_urls = pd.read_csv(r"C:\Users\Tanu\Desktop\Final\extracted_csv_files\p.csv")

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
rf_pred = RFmodel.predict(data_test)
cm2 = confusion_matrix(labels_test,rf_pred)

def getResult(lst):	
	lst=lst.drop(lst.columns[[0,3,5,13]],axis=1)
	lst = lst.sample(frac=1).reset_index(drop=True)
	print(lst)
	rf_pred_label = RFmodel.predict(lst)
	print(rf_pred_label)
	rf_pred_label.astype(int)
	if rf_pred_label==1:
		return "Phishing URL"
	else:
		return "Legitimate URL"	


legi = pd.read_csv(r"C:\Users\Tanu\Desktop\Final\extracted_csv_files\test_l.csv")
phish = pd.read_csv(r"C:\Users\Tanu\Desktop\Final\extracted_csv_files\test_p.csv")
url = legi.append(phish)
url = shuffle(url)
column_names = ["Domain", "Path", "Protocol","Prediction"]
u = pd.DataFrame(columns = column_names)
u['Domain']=url['Domain']
u['Path']=url['Path']
u['Protocol']=url['Protocol']
url = url.drop(url.columns[[0,3,5]],axis=1)
url = url.sample(frac=1).reset_index(drop=True)
test_data = url.drop('label',axis=1)
u['Label']= url['label']
rf_pred_label = RFmodel.predict(test_data)
new_series = pd.Series(rf_pred_label)
u["Prediction"]=new_series
pd.set_option('display.max_rows', u.shape[0]+1)
print(u)
print(cm2)
print("Accuracy with Random Forest: ",accuracy_score(labels_test,rf_pred) )






