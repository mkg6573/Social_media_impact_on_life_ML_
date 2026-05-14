## 📌 Dataset Overview

- This dataset analyzes the impact of social media and AI usage on students' daily lives.  

- It contains detailed information about students’:
  - Demographics  
  - Usage behavior  
  - Lifestyle patterns  

- Key features included in the dataset:
  - Age  
  - Gender  
  - Academic Level  
  - Daily Usage Hours  
  - Most Frequently Used Digital Platforms  

- It also captures important aspects of student well-being:
  - Academic Performance  
  - Sleep Patterns  
  - Mental Health  

- The dataset aims to:
  - Explore the effects of AI and social media usage  
  - Understand both positive and negative impacts  
  - Provide an overall impact indicator (beneficial or harmful)  

- Suitable for:
  - Exploratory Data Analysis (EDA)  
  - Data Visualization  
  - Machine Learning Model Building  

- Helps in:
  - Identifying patterns and trends  
  - Building predictive models  
  - Understanding the role of technology in student life  

---
# 🌐 Model Deployment

## 🚀 Live Demo
Click the link below to access the deployed machine learning model:

👉 [Open Deployed App](https://impact-of-social-media-on-health-us.streamlit.app/)

---

# 📊 Exploratory Data Analysis (EDA) Overview

Exploratory Data Analysis (EDA) is the process of analyzing and understanding a dataset before building a machine learning model.  
It helps in discovering patterns, detecting missing values, identifying outliers, and understanding relationships between features.

In this project, EDA was performed on the **Social Media Impact on Life** dataset to study how social media usage affects students' lives.

The analysis included:

- Understanding dataset structure
- Checking missing and duplicate values
- Analyzing categorical and numerical features
- Visualizing data distributions using graphs
- Studying correlations between variables
- Detecting outliers
- Identifying the target variable for classification

The target column in this dataset is:-

- `Overall_Impact`

which represents the overall effect of social media on a student's life (Positive, Negative, or Neutral).

- Notebook Link: [EDA Notebook](https://github.com/mkg6573/Social_media_impact_on_life_ML_/blob/main/Analysis/EDA.ipynb)

EDA helps in understanding the dataset, improving data quality, detecting patterns, and preparing the data for machine learning model development.
## 🐼 Pandas Profiling

Pandas Profiling is an automated EDA tool that generates a detailed report of the dataset, including missing values, correlations, distributions, and statistics.  
It helps quickly understand the dataset and identify important patterns before machine learning model building.


# Supervised Learning Algorithms 🚀

This folder contains implementations of different **Supervised Machine Learning Algorithms** applied on the **Social Media Impact on Life Dataset** for prediction and analysis.

---

# 📌 Algorithms Used

## 1. Logistic Regression
A statistical algorithm used for classification problems. It predicts output using probability.

**Accuracy:** 87.39%

- Notebook Link: [Logistic Regression Notebook](https://github.com/mkg6573/social_media_impact_on_life_ml_/blob/main/Supervised%20Learning%20Algorithms/Logistic_Regression.ipynb)
---

## 2. Decision Tree Classifier
A tree-based model that splits data into branches based on conditions to make predictions.

**Accuracy:** 92.08% 

- Notebook Link: [Decision Tree Classifier](https://github.com/mkg6573/social_media_impact_on_life_ml_/blob/main/Supervised%20Learning%20Algorithms/Decision_Tree.ipynb)
---

## 3. Random Forest Classifier
An ensemble learning algorithm that combines multiple decision trees for better accuracy and reduced overfitting.

**Accuracy:** 96.45%

- Notebook Link: [Random Forest](https://github.com/mkg6573/social_media_impact_on_life_ml_/blob/main/Supervised%20Learning%20Algorithms/Random_forest.ipynb)
---

## 4. K-Nearest Neighbors (KNN)
A distance-based algorithm that classifies data based on nearest neighboring points.

**Accuracy:** 92%

- Notebook Link: [KNN](https://github.com/mkg6573/social_media_impact_on_life_ml_/blob/main/Supervised%20Learning%20Algorithms/KNN.ipynb)
---

## 5. Support Vector Machine (SVM)
An algorithm that finds the best boundary (hyperplane) to separate classes.

**Accuracy:** 92.3%

- Notebook Link: [SVM](https://github.com/mkg6573/social_media_impact_on_life_ml_/blob/main/Supervised%20Learning%20Algorithms/SVM_GridSearchCV.ipynb)
---

## 6. Naive Bayes
A probability-based classification algorithm based on Bayes’ Theorem.

**Accuracy:** 83%

- Notebook Link: [SVM](https://github.com/mkg6573/social_media_impact_on_life_ml_/blob/main/Supervised%20Learning%20Algorithms/NaiveBayes_GridSearchCV.ipynb)
---

# ⚙️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit

---



# 📈 Model Comparison

The performance of all classification algorithms was compared using accuracy scores.

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 87.39%   |
| Decision Tree       | 92.08%   |
| Random Forest       | 96.45%   |
| KNN                 | 92.00%   |
| Naive Bayes         | 83.5%   |
| SVM                 | 92.30%   |
| XGBoost             | 98.82%   |

---

