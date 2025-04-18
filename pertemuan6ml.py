# -*- coding: utf-8 -*-
"""Pertemuan6ML.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-aX5B1h992MVD9z-bJxwjSRmyZwIPSuE

Nama : Irma Dwiyanti

NIM : 1227050059

Pertemuan 6 Praktikum Pembelajaran Mesin

Dataset : Breast Cancer Wisconsin Dataset
yang tersedia langsung di sklearn
"""

# Loading library
from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

# Load dataset
cancer = load_breast_cancer()

# Ubah ke DataFrame
cancer_df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
cancer_df['target'] = cancer.target

# Tampilkan statistik deskriptif
cancer_df.describe().T

# Tampilkan 10 baris pertama
print(cancer_df.head(10))

# Print seluruh data (opsional, hati-hati panjang)
print(cancer_df)

"""Melakukan pembagian data (Training dan Testing)"""

# Visualisasi data dengan Grafik pada data Iris
sns.pairplot(cancer_df,hue='target',palette='Set1')

# %%
from sklearn.model_selection import train_test_split

# Pisahkan fitur dan target
x = cancer_df.drop('target', axis=1)
y = cancer_df['target']

# Split data ke training dan testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=10)

print(len(x_train))

"""Membuat Report Hasil Klasifikasi"""

# %%
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# Buat dan latih model decision tree
model = DecisionTreeClassifier(random_state=10)
model.fit(x_train, y_train)

# Prediksi terhadap data test
y_pred = model.predict(x_test)

# Tampilkan classification report
print(classification_report(y_test, y_pred))

"""Melakukan Evaluasi"""

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Buat confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Visualisasikan confusion matrix
fig, ax = plt.subplots(figsize=(7, 7))
sns.set(font_scale=1.4)  # Ukuran font label
sns.heatmap(cm, ax=ax, annot=True, fmt='d', cmap='Blues', annot_kws={"size": 16})  # Tambahkan fmt dan cmap biar lebih bagus

# Label dan judul
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()

"""Menampilkan visualisasi Tree (Decision Tree)"""

# Ambil nama fitur dari dataframe, kecuali kolom 'target'
features = cancer_df.drop('target', axis=1).columns

# Visualisasi tree
fig, ax = plt.subplots(figsize=(25, 20))
tree.plot_tree(model, feature_names=features, class_names=['malignant', 'benign'], filled=True)
plt.show()

"""Ujicoba data diluar Data Testing"""

# %%
# Contoh data pasien baru (gunakan fitur dari breast cancer dataset)
cancer_test_data = {
    'mean radius': 14.0,
    'mean texture': 20.0,
    'mean perimeter': 90.0,
    'mean area': 600.0,
    'mean smoothness': 0.1,
    'mean compactness': 0.12,
    'mean concavity': 0.1,
    'mean concave points': 0.07,
    'mean symmetry': 0.2,
    'mean fractal dimension': 0.06,
    'radius error': 0.5,
    'texture error': 1.0,
    'perimeter error': 3.0,
    'area error': 40.0,
    'smoothness error': 0.005,
    'compactness error': 0.03,
    'concavity error': 0.04,
    'concave points error': 0.01,
    'symmetry error': 0.02,
    'fractal dimension error': 0.003,
    'worst radius': 16.0,
    'worst texture': 25.0,
    'worst perimeter': 100.0,
    'worst area': 800.0,
    'worst smoothness': 0.13,
    'worst compactness': 0.25,
    'worst concavity': 0.3,
    'worst concave points': 0.15,
    'worst symmetry': 0.3,
    'worst fractal dimension': 0.08
}

# Pastikan urutan fitur sesuai
feature_order = cancer_df.drop('target', axis=1).columns
prediction_input_df = pd.DataFrame([cancer_test_data])
prediction = model.predict(prediction_input_df[feature_order])

# Tampilkan hasil prediksi
print("Prediksi klasifikasi:", "Benign (1)" if prediction[0] == 1 else "Malignant (0)")