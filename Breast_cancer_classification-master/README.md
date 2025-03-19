# Breast Tumor Classification using Machine Learning

## Types of Tumor

- BENIGN TUMOR
  - Non-Cancerous
  - Capsulated
  - Slow growing 
  - Do Not Metastasize (don’t spread to other parts of the body)
  - Cells are normal
- MALIGNANT TUMOR
  - Cancerous
  - Non-Capsulated
  - Fast Growing
  - Metastasize (spread to other parts of the body)
  - Cells with large, dark nuclei, may have abnormal shape.

## Fine Needle Aspiration

Fine needle aspiration is a type of biopsy procedure. In fine needle aspiration, a thin needle is inserted into an area of abnormal appearing tissue or body fluid. As with other types of biopsies, the sample collected during fine needle aspiration can help make a diagnosis or rule out a condition such as cancer.

## Workflow

1. **Customer Data:** Collect the required data from all the customers.
2. **Data Pre-processing:** Preparing the raw data and making it suitable for a machine learning model. 
3. **Train Test Split:** A train test split is when you split your data into a training set and a testing set.
4. **Logistic Regression Model:** Logistic regression is the process of modeling the probability of a discrete outcome given an input variable.
5. **New Data for Trained Logistic Regression Model:** Provide new data to the trained Logistic Regression Model to check the accuracy of the model.
6. **Prediction:** The trained logistic regression model will now predict whether the given data will be Benign or Malignant.

## Libraries used:-

- Numpy: the standard for working with numerical data in Python.
- Pandas: Python library used for working with data sets.
- Matplotlib: Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. 
- Seaborn: Seaborn is a Python data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
- SK Learn: a Python library to implement machine learning models and statistical modeling. 
- Pickle: Python's Pickle module is a popular format used to serialize and deserialize data types.

## About Dataset

This is a classic dataset for training and benchmarking machine learning algorithms.
- Biopsy features for classification of 569 malignant (cancer) and benign (not cancer) breast masses.
- Features were computationally extracted from digital images of fine needle aspirate biopsy slides. Features correspond to properties of cell nuclei, such as size, shape, and regularity. The mean, standard error, and worst value of each of the 10 nuclear parameters are reported for a total of 30 features.
