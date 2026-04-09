import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler, SMOTE


# Custom Data Set Creation
X, y = make_classification(n_samples=1000,
n_features=10,
n_informative=6,
n_redundant=2,
n_clusters_per_class=1,
weights=[0.9, 0.1],
random_state=42)
df = pd.DataFrame(X)
df['target'] = y
print(df['target'].value_counts())

sns.countplot(x='target', data=df)
plt.title("Original Class Distribution")
plt.show()

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.3, random_state=42, stratify=y
)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("=== Original Imbalanced Data ===")
print("Accuracy:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Random Under Sampling (Removes samples from the majority class.)
rus = RandomUnderSampler(random_state=42)
X_rus, y_rus = rus.fit_resample(X_train, y_train)
print("After Under-Sampling:")
print(pd.Series(y_rus).value_counts())
# After Under-Sampling:
# 0 73
# 1 73
# Name: count, dtype: int64

model_rus = LogisticRegression(max_iter=1000)
model_rus.fit(X_rus, y_rus)
y_pred_rus = model_rus.predict(X_test)
print("=== Random Under-Sampling ===")
print("Accuracy:", accuracy_score(y_test, y_pred_rus))
print(confusion_matrix(y_test, y_pred_rus))
print(classification_report(y_test, y_pred_rus))


# Random Over-Sampling (Duplicates samples from the minority class.)
ros = RandomOverSampler(random_state=42)
X_ros, y_ros = ros.fit_resample(X_train, y_train)
print("After Over-Sampling:")
print(pd.Series(y_ros).value_counts())
model_ros = LogisticRegression(max_iter=1000)
model_ros.fit(X_ros, y_ros)
y_pred_ros = model_ros.predict(X_test)
print("=== Random Over-Sampling ===")
print("Accuracy:", accuracy_score(y_test, y_pred_ros))
print(confusion_matrix(y_test, y_pred_ros))
print(classification_report(y_test, y_pred_ros))

# SMOTE (Synthetic Minority Oversampling Technique) [Creates synthetic samples for the minority class instead of duplicating e
smote = SMOTE(random_state=42)
X_sm, y_sm = smote.fit_resample(X_train, y_train)
print("After SMOTE:")
print(pd.Series(y_sm).value_counts())
model_sm = LogisticRegression(max_iter=1000)
model_sm.fit(X_sm, y_sm)
y_pred_sm = model_sm.predict(X_test)
print("=== SMOTE ===")
print("Accuracy:", accuracy_score(y_test, y_pred_sm))
print(confusion_matrix(y_test, y_pred_sm))
print(classification_report(y_test, y_pred_sm))
# Class Weighting (Assigns higher penalty to minority class during training.)
model_wt = LogisticRegression(class_weight='balanced', max_iter=1000)
model_wt.fit(X_train, y_train)
y_pred_wt = model_wt.predict(X_test)
print("=== Class Weighting ===")
print("Accuracy:", accuracy_score(y_test, y_pred_wt))
print(confusion_matrix(y_test, y_pred_wt))
print(classification_report(y_test, y_pred_wt))


results = {
"Original": classification_report(y_test, y_pred, output_dict=True)["1"]["f1-score"],
"UnderSampling": classification_report(y_test, y_pred_rus, output_dict=True)["1"]["f1-score"],
"OverSampling": classification_report(y_test, y_pred_ros, output_dict=True)["1"]["f1-score"],
"SMOTE": classification_report(y_test, y_pred_sm, output_dict=True)["1"]["f1-score"],
"ClassWeight": classification_report(y_test, y_pred_wt, output_dict=True)["1"]["f1-score"]
}
print(results)
plt.bar(results.keys(), results.values())
plt.title("F1-score Comparison for Minority Class")
plt.ylabel("F1-score")
plt.xticks(rotation=20)
plt.show()