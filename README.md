# Breast Cancer Classification using Random Forest (From Scratch)

##  Project Overview
This project implements a **Random Forest classifier from scratch in Python** to predict whether a breast tumor is **malignant (M)** or **benign (B)** using the **Wisconsin Diagnostic Breast Cancer dataset (WDBC)**.

Instead of using built-in machine learning libraries like `sklearn.ensemble.RandomForestClassifier`, this implementation builds the algorithm manually to understand the internal working of **Decision Trees, Gini Impurity, Bagging, and Random Feature Selection**.

---

##  Key Concepts Implemented

- Decision Tree using **Gini Impurity**
- Random Feature Selection
- Bootstrapping (**Bagging**)
- Random Forest Ensemble Learning
- Majority Voting for Predictions
- Model Evaluation using **Accuracy and Confusion Matrix**

---

##  Dataset

Dataset used: **Wisconsin Diagnostic Breast Cancer (WDBC)**

Each sample contains:

- 30 numerical features describing cell nuclei characteristics
- A label indicating:
  - **M → Malignant**
  - **B → Benign**

Dataset source:

https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)

---


---

##  How the Model Works

###  Data Loading
The dataset is loaded using **Pandas** and converted into **NumPy arrays**.

###  Train-Test Split
The dataset is divided into:

- **75% Training Data**
- **25% Testing Data**

### Decision Tree Construction
Each decision tree:

- Uses **Gini Impurity** to determine the best split
- Recursively splits nodes until:
  - Maximum depth is reached
  - A pure node is found

###  Random Forest Training

The Random Forest is built by:

1. Randomly sampling training data (**Bootstrapping**)
2. Training multiple decision trees
3. Combining predictions using **majority voting**

###  Prediction

Each tree predicts a class label.  
Final prediction is determined using majority vote from the tree



---

##  Model Evaluation

Performance is evaluated using:

- **Accuracy**
- **Confusion Matrix**

Confusion matrix is visualized using **Seaborn Heatmap**.

---

##  Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn (for evaluation utilities)

---

##  Example Output
 Accurcy was around 96.5 percentage



Confusion Matrix visualization shows:

- True Positives
- True Negatives
- False Positives
- False Negatives

---

##  Learning Outcomes

This project helps understand:

- How **Decision Trees split data**
- How **Gini Impurity works**
- How **Random Forest improves model performance**
- How **ensemble methods reduce overfitting**

---
