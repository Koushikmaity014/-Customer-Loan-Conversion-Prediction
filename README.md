<div align="center">

🏦 Customer Loan Conversion Prediction

End-to-End Machine Learning System for Personal Loan Conversion

<p>
  <a href="https://customer-loan-conversion-prediction-cr9k.onrender.com/">
    <img src="https://img.shields.io/badge/🚀%20LIVE%20DEMO-Visit%20Application-00C853?style=for-the-badge&logo=streamlit&logoColor=white">
  </a>
  <a href="https://github.com/Koushikmaity014/-Customer-Loan-Conversion-Prediction">
    <img src="https://img.shields.io/badge/💻%20GITHUB-Source%20Code-181717?style=for-the-badge&logo=github&logoColor=white">
  </a>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat-square&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?style=flat-square&logo=scikit-learn&logoColor=white">
  <img src="https://img.shields.io/badge/Optuna-Hyperparameter%20Tuning-4B8BBE?style=flat-square">
  <img src="https://img.shields.io/badge/Streamlit-Deployment-FF4B4B?style=flat-square&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/Render-Cloud%20Deployment-46E3B7?style=flat-square&logo=render&logoColor=black">
</p>

</div>

📸 Application Preview

<p align="center">
  <img src="images/app_screenshot.png" width="850">
</p>

<p align="center">
  <b>Interactive Streamlit application for real-time customer loan conversion prediction.</b>
</p>

📌 Project Overview

Customer Loan Conversion Prediction is an end-to-end machine learning project developed to predict whether an existing bank customer is likely to accept a personal loan.

The project uses customer demographic, financial, and banking relationship information to identify high-potential customers and support more targeted marketing campaigns.

The complete workflow covers Exploratory Data Analysis, Data Preprocessing, Feature Selection, Model Comparison, Stratified Cross-Validation, Optuna Hyperparameter Optimization, Classification Threshold Optimization, Model Evaluation, Model Serialization, and Streamlit Deployment.

🎯 Business Problem

Banks have a large number of existing customers who use their deposit and other banking services. Some of these customers may also be potential personal-loan customers.

The objective is to identify customers who are more likely to accept a personal loan so that the bank can focus its marketing campaign on high-potential customers instead of contacting the entire customer base.

Business Benefits

🎯 Better customer targeting

📈 Higher potential loan conversion

💰 Reduced marketing expenditure

⚡ More efficient campaigns

👥 Identification of high-potential customers

📊 Dataset

The project uses the Bank Personal Loan Modelling dataset obtained from Kaggle.

The dataset contains information about 5,000 bank customers, including demographic, financial, and banking relationship attributes.

Dataset Summary

Property

Value

👥 Total Customers

5,000

✅ Loan Accepted

480

❌ Loan Not Accepted

4,520

🎯 Positive Class

9.6%

🎯 Target Variable

Personal Loan

Target Variable

Personal Loan = 0 → Customer did not accept the loan
Personal Loan = 1 → Customer accepted the loan

The dataset has a significant class imbalance because only 9.6% of customers accepted the personal loan.

Therefore, model evaluation focuses on Precision, Recall, F1 Score, ROC-AUC, and PR-AUC, rather than relying only on accuracy.

🧩 Features

Feature

Description

Age

Customer age

Experience

Years of professional experience

Income

Annual income in $1,000s

ZIP Code

Customer ZIP code

Family

Number of family members

CCAvg

Average monthly credit-card spending in $1,000s

Education

Education level

Mortgage

Mortgage value

Securities Account

Whether the customer has a securities account

CD Account

Whether the customer has a CD account

Online

Whether the customer uses online banking

CreditCard

Whether the customer has the bank's credit card

Personal Loan

Target variable

🔎 Exploratory Data Analysis

The dataset was explored to understand customer characteristics, feature distributions, relationships between variables, and factors associated with personal-loan acceptance.

Analysis Performed

📋 Dataset structure and data types

🔍 Missing-value analysis

🔁 Duplicate detection

📊 Target-class distribution

📈 Numerical feature distributions

📊 Categorical feature analysis

📦 Outlier analysis

🔗 Correlation analysis

🎯 Feature-versus-target analysis

👥 Customer segmentation analysis

Key Findings

The target variable is highly imbalanced, with only 9.6% positive cases.

Income showed a strong relationship with personal-loan acceptance.

Age and Experience are highly correlated.

Income and CCAvg are highly correlated.

No missing values were found.

No duplicate rows were found.

Because of the class imbalance, accuracy alone was not considered sufficient for model evaluation. Precision, Recall, F1 Score, ROC-AUC, and PR-AUC were also considered.

🎯 Target Distribution

<p align="center">
  <img src="images/target_distribution.png" width="750">
</p>

The dataset contains 4,520 customers who did not accept the loan and 480 customers who accepted it.

This results in a positive-class rate of 9.6%, making this an imbalanced classification problem.

💰 Income and Loan Conversion

<p align="center">
  <img src="images/income_vs_loan.png" width="750">
</p>

Income was one of the most informative variables for predicting personal-loan acceptance. Customers with higher income levels showed a greater tendency toward loan acceptance.

🎓 Education and Loan Conversion

<p align="center">
  <img src="images/education_vs_loan.png" width="750">
</p>

Education level was also analyzed to understand its relationship with personal-loan acceptance and customer behavior.

🔗 Feature Correlation

<p align="center">
  <img src="images/correlation_heatmap.png" width="800">
</p>

The correlation analysis identified several important relationships, including the strong relationship between Age and Experience and between Income and CCAvg.

🧹 Data Preparation

The data preparation stage included:

Checking data types

Checking missing values

Checking duplicate observations

Separating features and target

Removing unnecessary variables where appropriate

Preparing the preprocessing pipeline

Splitting the dataset into training and testing sets

The dataset was divided into:

Training Set → 70%
Testing Set  → 30%

The test set was kept separate for final model evaluation.

🤖 Machine Learning Workflow

The complete machine learning workflow is:

Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Train/Test Split
     ↓
Data Preprocessing
     ↓
Baseline Classification Models
     ↓
Stratified 5-Fold Cross-Validation
     ↓
Permutation Feature Importance
     ↓
Feature Selection
     ↓
Model Comparison
     ↓
Optuna Hyperparameter Tuning
     ↓
Classification Threshold Optimization
     ↓
Final Model Evaluation
     ↓
Model Serialization
     ↓
Streamlit Deployment

🧪 Model Development

Multiple classification approaches were evaluated during the modelling process.

The models were compared using Stratified 5-Fold Cross-Validation.

Stratification was used because the target variable is highly imbalanced. It ensures that each fold maintains approximately the same proportion of positive and negative customers.

The model selection process focused particularly on F1 Score, while also considering Precision, Recall, ROC-AUC, and PR-AUC.

🧠 Feature Selection

Permutation-based feature importance was used to identify the most informative predictors.

<p align="center">
  <img src="images/feature_importance.png" width="800">
</p>

The final selected feature set for the Gradient Boosting model was:

Income
Education
Family
CCAvg

These four features provided strong predictive performance while keeping the final model compact and interpretable.

⚙️ Model Comparison

Multiple classification models and feature combinations were evaluated using Stratified 5-Fold Cross-Validation.

<p align="center">
  <img src="images/model_comparison.png" width="800">
</p>

Gradient Boosting performed particularly well and was selected for further optimization.

🌳 Gradient Boosting + Optuna

The selected Gradient Boosting model was optimized using Optuna.

The optimization process explored important hyperparameters including:

n_estimators

learning_rate

max_depth

min_samples_split

min_samples_leaf

subsample

max_features

Cross-Validation Improvement

Model Stage

CV F1 Score

Baseline Gradient Boosting

0.9274

Tuned Gradient Boosting

0.9393

The tuned model improved the cross-validation F1 score from 0.9274 to 0.9393.

🎚️ Classification Threshold Optimization

The default classification threshold of 0.50 was not assumed to be optimal.

Instead, predicted probabilities were evaluated across different thresholds to find a better balance between Precision and Recall.

<p align="center">
  <img src="images/threshold_optimization.png" width="800">
</p>

Selected Threshold

Default Threshold   : 0.5000
Optimized Threshold : 0.3815

The optimized threshold improved the balance between Precision and Recall and increased the out-of-fold F1 score.

This is particularly useful in a marketing campaign where identifying more potential customers can be more valuable than simply maximizing overall accuracy.

📈 Final Model Performance

The final Tuned Gradient Boosting Classifier achieved the following results on the held-out test set:

Metric

Score

Accuracy

98.80%

Precision

95.65%

Recall

91.67%

F1 Score

93.62%

ROC-AUC

99.80%

PR-AUC

98.53%

🎯 Confusion Matrix

<p align="center">
  <img src="images/confusion_matrix.png" width="650">
</p>

Test Set Results

                 Predicted
                 No      Yes
Actual No        900       4
Actual Yes         8      88

The model correctly identified 88 of the 96 actual positive customers while producing only 4 false positives on the test set.

📈 ROC Curve

<p align="center">
  <img src="images/roc_curve.png" width="750">
</p>

The final model achieved a ROC-AUC of 99.80%, demonstrating strong discrimination between customers who accepted and did not accept the personal loan.

📊 Precision-Recall Curve

<p align="center">
  <img src="images/precision_recall_curve.png" width="750">
</p>

The model achieved a PR-AUC of 98.53%, which is particularly useful for evaluating performance on this imbalanced classification problem.

💡 Business Interpretation

The final model provides a practical way to identify customers who are more likely to accept a personal loan.

Instead of contacting every existing customer, the bank can prioritize customers with a higher predicted probability of accepting a personal loan.

The model therefore provides a data-driven approach to customer targeting and can help the bank allocate marketing resources more efficiently.

Existing Customers
        ↓
Machine Learning Prediction
        ↓
Loan Acceptance Probability
        ↓
Identify High-Potential Customers
        ↓
Targeted Marketing Campaign
        ↓
Potentially Higher Conversion

🚀 Deployment

The final trained model was serialized using Joblib and deployed as an interactive Streamlit web application.

The application uses the four selected features:

💰 Income
🎓 Education
👨‍👩‍👧‍👦 Family
💳 CCAvg

The application generates:

🎯 Predicted Class
📊 Probability of Loan Acceptance
⚙️ Classification Threshold

🖥️ Application Demo

<p align="center">
  <img src="images/app_screenshot.png" width="850">
</p>

The application provides a simple interface where users can enter customer information and receive a real-time loan conversion prediction.

Prediction Interpretation

Class 0 → Customer is predicted not to accept the loan

Class 1 → Customer is predicted to accept the loan

🌐 Live Demo

<p align="center">

<a href="https://customer-loan-conversion-prediction-cr9k.onrender.com/">

<img src="https://img.shields.io/badge/🚀%20TRY%20THE%20LIVE%20MODEL-00C853?style=for-the-badge&logo=streamlit&logoColor=white">

</a>

</p>

🛠️ Technology Stack

Category

Technologies

🐍 Programming

Python

📊 Data Analysis

Pandas, NumPy

📈 Visualization

Matplotlib, Seaborn

🤖 Machine Learning

Scikit-learn

🌳 Final Model

Gradient Boosting

⚙️ Hyperparameter Optimization

Optuna

💾 Model Serialization

Joblib

🖥️ Web Application

Streamlit

☁️ Deployment

Render

🔧 Version Control

Git, GitHub

📁 Project Structure

Customer-Loan-Conversion-Prediction/
│
├── README.md
├── app.py
├── requirements.txt
├── .gitignore
│
├── data/
│   └── README.md
│
├── models/
│   └── bank_loan_model.pkl
│
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_modeling.ipynb
│
├── reports/
│   └── pandas_profiling_report.html
│
└── images/
    ├── app_screenshot.png
    ├── target_distribution.png
    ├── income_vs_loan.png
    ├── education_vs_loan.png
    ├── correlation_heatmap.png
    ├── feature_importance.png
    ├── model_comparison.png
    ├── threshold_optimization.png
    ├── confusion_matrix.png
    ├── roc_curve.png
    └── precision_recall_curve.png

💻 Installation

1. Clone the Repository

git clone https://github.com/Koushikmaity014/-Customer-Loan-Conversion-Prediction.git

2. Navigate to the Project Directory

cd Customer-Loan-Conversion-Prediction

3. Install Dependencies

pip install -r requirements.txt

4. Run the Streamlit Application

streamlit run app.py

📌 Project Highlights

<div align="center">

Metric

Result

👥 Dataset Size

5,000 Customers

🎯 Positive Class

9.6%

🧠 Selected Features

4

🌳 Final Model

Tuned Gradient Boosting

⚙️ Optimization

Optuna

🔄 Validation

Stratified 5-Fold CV

🎚️ Optimized Threshold

0.3815

📈 Test F1 Score

93.62%

🎯 ROC-AUC

99.80%

📊 PR-AUC

98.53%

🚀 Deployment

Streamlit + Render

</div>

📚 Learning Outcomes

This project demonstrates practical experience with:

Exploratory Data Analysis

Data preprocessing

Imbalanced classification

Feature selection

Model comparison

Stratified cross-validation

Permutation feature importance

Hyperparameter optimization

Optuna

Classification threshold optimization

Precision and Recall analysis

F1 Score

ROC-AUC

PR-AUC

Confusion matrix analysis

Model serialization

Streamlit application development

Cloud deployment

🔗 Project Links

💻 GitHub Repository

https://github.com/Koushikmaity014/-Customer-Loan-Conversion-Prediction

🚀 Live Application

https://customer-loan-conversion-prediction-cr9k.onrender.com/

👨‍💻 Author

<div align="center">

Koushik Maity

M.Sc. Mathematics & Computing

Indian Institute of Technology Guwahati

<p>

<a href="https://github.com/Koushikmaity014">
<img src="https://img.shields.io/badge/GitHub-Koushikmaity014-181717?style=for-the-badge&logo=github&logoColor=white">
</a>

<a href="https://customer-loan-conversion-prediction-cr9k.onrender.com/">
<img src="https://img.shields.io/badge/Live%20Project-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
</a>

</p>

</div>

<div align="center">

⭐ If you found this project useful, consider giving the repository a star!

Thank you for visiting! 🚀

</div>

