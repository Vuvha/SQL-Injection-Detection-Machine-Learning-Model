# -*- coding: utf-8 -*-
"""SQL_Injection_source.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q7y_45HmpvmV9BYbrYcOglf3hEgrTrzx

#Load dữ liệu
"""

import pandas as pd

data = pd.read_csv('/content/drive/MyDrive/DATA học máy /Modified_SQL_Dataset.csv')

data.describe()

"""Tạo dữ liệu huấn luyện"""

import numpy as np
#Tạo dữ liệu huấn luyện 
X = data.Query
y = data.Label

"""#Khám phá dữ liệu"""

import numpy as np

count = np.unique(y, return_counts=True)

count[0]

count[1]

"""Trực quan hóa dữ liệu"""

import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(x=count[0], y=count[1])

"""#Mã hóa dữ liệu"""

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

encoder = CountVectorizer(ngram_range =(1,1))
encoder.fit(X)

encoder.vocabulary_

X_encoder = encoder.transform(X)

"""#Chuẩn bị dữ liệu"""

#chia data ban đầu thành train 80% test 20%
from sklearn.model_selection import train_test_split

X_train_encoder, X_test_encoder, y_train, y_test = train_test_split(X_encoder, y, test_size=0.2)

"""#Huấn luyện mô hình

Logistic Regression
"""

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(X_train_encoder, y_train)

y_pred_LGR = lr.predict(X_test_encoder)

"""KNN"""

from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier(n_neighbors=1)
kn.fit(X_train_encoder, y_train)

y_pred_KNN = kn.predict(X_test_encoder)

"""Decision Tree"""

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()
dt.fit(X_train_encoder, y_train)

y_pred_DT = dt.predict(X_test_encoder)

"""Random Forest"""

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(X_train_encoder, y_train)

y_pred_RF = rf.predict(X_test_encoder)

"""SVM"""

from sklearn import svm
sm = svm.SVC()
sm.fit(X_train_encoder, y_train)

y_pred_SVM = sm.predict(X_test_encoder)

"""#Đánh giá mô hình

##Logistic Regression
"""

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

print('LogisticRegress')
precision = accuracy_score(y_test, y_pred_LGR)
print('Accuracy: %f' % precision)

precision = precision_score(y_test, y_pred_LGR, average='macro')
print('Precision: %f' % precision)

recall = recall_score(y_test, y_pred_LGR, average='macro')
print('Recall: %f' % recall)

f1 = f1_score(y_test, y_pred_LGR, average='macro')
print('F1 score: %f' % f1)

"""Ma trận nhầm lẫn"""

from sklearn.metrics import confusion_matrix
cf_LGR= confusion_matrix(y_test, y_pred_LGR)

import seaborn as sn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sn.set(font_scale=1.4)
sn.heatmap(cf_LGR, annot=True, annot_kws={"size": 16}, fmt='d')

plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

"""##KNN"""

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

print('KNN')
precision = accuracy_score(y_test, y_pred_KNN)
print('Accuracy: %f' % precision)

precision = precision_score(y_test, y_pred_KNN, average='macro')
print('Precision: %f' % precision)

recall = recall_score(y_test, y_pred_KNN, average='macro')
print('Recall: %f' % recall)

f1 = f1_score(y_test, y_pred_KNN, average='macro')
print('F1 score: %f' % f1)

"""Ma trận nhầm lẫn"""

from sklearn.metrics import confusion_matrix
cf_KNN= confusion_matrix(y_test, y_pred_KNN)

import seaborn as sn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sn.set(font_scale=1.4)
sn.heatmap(cf_KNN, annot=True, annot_kws={"size": 16}, fmt='d')

plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

"""##Decision Tree"""

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

print('Decision Tree')
precision = accuracy_score(y_test, y_pred_DT)
print('Accuracy: %f' % precision)

precision = precision_score(y_test, y_pred_DT, average='macro')
print('Precision: %f' % precision)

recall = recall_score(y_test, y_pred_DT, average='macro')
print('Recall: %f' % recall)

f1 = f1_score(y_test, y_pred_DT, average='macro')
print('F1 score: %f' % f1)

"""Ma trận nhầm lẫn"""

from sklearn.metrics import confusion_matrix
cf_DT= confusion_matrix(y_test, y_pred_DT)

import seaborn as sn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sn.set(font_scale=1.4)
sn.heatmap(cf_DT, annot=True, annot_kws={"size": 16}, fmt='d')

plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

"""##Random Forest"""

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

print('Random Forest')
precision = accuracy_score(y_test, y_pred_RF)
print('Accuracy: %f' % precision)

precision = precision_score(y_test, y_pred_RF, average='macro')
print('Precision: %f' % precision)

recall = recall_score(y_test, y_pred_RF, average='macro')
print('Recall: %f' % recall)

f1 = f1_score(y_test, y_pred_RF, average='macro')
print('F1 score: %f' % f1)

"""Ma trận nhầm lẫn"""

from sklearn.metrics import confusion_matrix
cf_RF= confusion_matrix(y_test, y_pred_RF)

import seaborn as sn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sn.set(font_scale=1.4)
sn.heatmap(cf_RF, annot=True, annot_kws={"size": 16}, fmt='d')

plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

"""##SVM"""

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

print('SVM')
precision = accuracy_score(y_test, y_pred_SVM)
print('Accuracy: %f' % precision)

precision = precision_score(y_test, y_pred_SVM, average='macro')
print('Precision: %f' % precision)

recall = recall_score(y_test, y_pred_SVM, average='macro')
print('Recall: %f' % recall)

f1 = f1_score(y_test, y_pred_SVM, average='macro')
print('F1 score: %f' % f1)

"""Ma trận nhầm lẫn"""

from sklearn.metrics import confusion_matrix
cf_SVM= confusion_matrix(y_test, y_pred_SVM)

import seaborn as sn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sn.set(font_scale=1.4)
sn.heatmap(cf_SVM, annot=True, annot_kws={"size": 16}, fmt='d')

plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

"""#Demo"""

READ_Label = {
  1: "positve (Dương tính)",
  0: "negative (Âm tính)"
}

print("Nhập vào mẫu thử: ")
input_text = input()

input_encoder = encoder.transform([input_text])
label = sm.predict(input_encoder)

print("Nhãn của câu vừa nhập là: {}".format(READ_Label[label[0]]))