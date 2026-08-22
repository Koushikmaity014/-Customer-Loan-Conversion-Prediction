<div align="center">

🏦 Customer Loan Conversion Prediction

🎯 Predicting Which Bank Customers Are Most Likely to Accept a Personal Loan

<p>
  <a href="https://customer-loan-conversion-prediction-cr9k.onrender.com/">
    <img src="https://img.shields.io/badge/🚀%20LIVE%20DEMO-TRY%20THE%20MODEL-00C853?style=for-the-badge&logo=streamlit&logoColor=white">
  </a>
  <a href="https://github.com/Koushikmaity014/-Customer-Loan-Conversion-Prediction">
    <img src="https://img.shields.io/badge/💻%20GITHUB-SOURCE%20CODE-181717?style=for-the-badge&logo=github&logoColor=white">
  </a>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat-square&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?style=flat-square&logo=scikit-learn&logoColor=white">
  <img src="https://img.shields.io/badge/Optuna-Hyperparameter%20Tuning-4B8BBE?style=flat-square">
  <img src="https://img.shields.io/badge/Streamlit-Deployment-FF4B4B?style=flat-square&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/Render-Deployed-46E3B7?style=flat-square&logo=render&logoColor=black">
</p>

</div>

🚀 Project at a Glance

📌

Details

Domain

Banking / Financial Marketing

Problem

Personal Loan Conversion Prediction

Dataset

Bank Personal Loan Modelling

Source

Kaggle

Customers

5,000

Positive Customers

480

Positive Rate

9.6%

Final Model

Tuned Gradient Boosting

Feature Selection

Permutation Importance

Hyperparameter Tuning

Optuna

Validation

Stratified 5-Fold Cross-Validation

Final Features

Income, Education, Family, CCAvg

Optimized Threshold

0.3815

Test F1 Score

93.62%

ROC-AUC

99.80%

PR-AUC

98.53%

Deployment

Streamlit + Render

🌐 Live Application

<div align="center">

🚀 Try the deployed machine learning model

<a href="https://customer-loan-conversion-prediction-cr9k.onrender.com/">

<img src="https://img.shields.io/badge/OPEN%20LIVE%20APPLICATION-00C853?style=for-the-badge&logo=streamlit&logoColor=white">

</a>

<br><br>

Live URL:
https://customer-loan-conversion-prediction-cr9k.onrender.com/

</div>

📌 1. Project Overview

Customer Loan Conversion Prediction is an end-to-end machine learning project developed to predict whether an existing bank customer is likely to accept a personal loan.

The project is based on customer demographic, financial, and banking relationship information. The goal is to identify high-potential customers so that a bank can target its marketing campaigns more efficiently.

Instead of contacting the complete customer base, the model can help the bank prioritize customers who have a higher probability of accepting a personal loan.

The project covers the complete machine learning lifecycle:

Data → EDA → Preprocessing → Model Comparison → Feature Selection → Cross-Validation → Optuna Tuning → Threshold Optimization → Evaluation → Model Serialization → Deployment

🎯 2. Business Problem

A bank may have thousands of existing liability customers, but only a small percentage may be interested in a personal loan.

A marketing campaign that contacts every customer can consume significant time and budget.

The business question is:

Which existing customers are most likely to accept a personal loan?

Business Objective

flowchart LR
    A["🏦 Existing Customers"] --> B["📊 Customer Data"]
    B --> C["🤖 ML Prediction"]
    C --> D["📈 Loan Probability"]
    D --> E["🎯 High-Potential Customers"]
    E --> F["📣 Targeted Campaign"]
    F --> G["💰 Better Marketing Efficiency"]

Expected Business Benefits

🎯 More targeted marketing

💰 Reduced campaign cost

📈 Better conversion potential

⚡ Efficient allocation of marketing resources

👥 Identification of high-potential customers

📊 3. Dataset

The project uses the Bank Personal Loan Modelling dataset obtained from Kaggle.

The dataset contains 5,000 customer records with demographic, financial, and banking relationship information.

Dataset Summary

Metric

Value

👥 Total Customers

5,000

❌ Loan Not Accepted

4,520

✅ Loan Accepted

480

🎯 Positive Class

9.6%

🎯 Target

Personal Loan

Target Distribution

pie showData
    title Personal Loan Distribution
    "Did Not Accept Loan - 90.4%" : 4520
    "Accepted Loan - 9.6%" : 480

The dataset is highly imbalanced. Only 480 out of 5,000 customers accepted the personal loan.

Because of this imbalance, accuracy alone is not sufficient for evaluating the model.

The project therefore emphasizes:

Precision + Recall + F1 Score + ROC-AUC + PR-AUC

🧩 4. Feature Description

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

🔎 5. Exploratory Data Analysis

The EDA stage was used to understand:

Dataset structure

Data types

Missing values

Duplicate observations

Numerical distributions

Categorical distributions

Outliers

Correlations

Feature-target relationships

Customer characteristics

Key Findings

The target variable is highly imbalanced with a 9.6% positive rate.

Income showed a strong relationship with personal-loan acceptance.

Age and Experience are strongly related.

Income and CCAvg are strongly related.

No missing values were found.

No duplicate rows were found.

💰 6. Income and Loan Conversion

Income was one of the most important variables in the final model.

Higher-income customers generally showed a greater tendency to accept the personal loan.

xychart-beta
    title "Illustrative Relationship: Income and Loan Conversion"
    x-axis "Income Level" [Low, Medium, High]
    y-axis "Relative Loan Conversion" 0 --> 100
    bar [10, 28, 65]

The chart above is a conceptual visualization of the observed relationship. It is included to explain the business pattern; it is not presented as an exact recalculation of the original dataset.

🎓 7. Education and Loan Conversion

Education level was also analyzed to understand differences in loan acceptance across customer groups.

xychart-beta
    title "Loan Acceptance Across Education Levels"
    x-axis "Education Level" [Undergraduate, Graduate, Advanced]
    y-axis "Relative Acceptance" 0 --> 100
    bar [15, 30, 55]

The analysis helped identify customer characteristics that could contribute to loan conversion.

🔗 8. Correlation Analysis

Correlation analysis was performed to understand relationships between numerical variables.

Important relationships included:

flowchart LR
    A["Age"] <-->|"Strong relationship"| B["Experience"]
    C["Income"] <-->|"Strong relationship"| D["CCAvg"]

These relationships were considered during feature analysis and model development.

🧹 9. Data Preparation

The data preparation process included:

Checking the dataset structure

Checking data types

Checking missing values

Checking duplicates

Separating features and target

Preparing the preprocessing workflow

Splitting the dataset into training and testing sets

Train-Test Split

pie showData
    title Dataset Split
    "Training Set - 70%" : 70
    "Testing Set - 30%" : 30

The test set was kept separate and used only for final evaluation.

🤖 10. Machine Learning Workflow

The complete workflow is:

flowchart TD
    A["📥 Raw Dataset"] --> B["🧹 Data Cleaning"]
    B --> C["🔎 Exploratory Data Analysis"]
    C --> D["✂️ Train/Test Split"]
    D --> E["⚙️ Data Preprocessing"]
    E --> F["🤖 Baseline Models"]
    F --> G["🔄 Stratified 5-Fold CV"]
    G --> H["📌 Permutation Feature Importance"]
    H --> I["🧠 Feature Selection"]
    I --> J["📊 Model Comparison"]
    J --> K["⚡ Optuna Hyperparameter Tuning"]
    K --> L["🎚️ Threshold Optimization"]
    L --> M["📈 Final Evaluation"]
    M --> N["💾 Model Serialization"]
    N --> O["🖥️ Streamlit Application"]
    O --> P["☁️ Render Deployment"]

🧪 11. Model Development

Different classification approaches were evaluated during model development.

The models were evaluated using Stratified 5-Fold Cross-Validation.

Stratification was important because the target variable contains only 9.6% positive cases.

The primary model-selection metric was F1 Score, supported by Precision, Recall, ROC-AUC, and PR-AUC.

🧠 12. Feature Selection

Permutation-based feature importance was used to identify the most informative predictors.

The final selected features for the Gradient Boosting model were:

flowchart TD
    A["🎯 Final Feature Set"]
    A --> B["💰 Income"]
    A --> C["🎓 Education"]
    A --> D["👨‍👩‍👧‍👦 Family"]
    A --> E["💳 CCAvg"]

Why Feature Selection?

Feature selection helps to:

Reduce unnecessary variables

Improve model simplicity

Improve interpretability

Reduce potential noise

Create a compact prediction interface

The final deployed application therefore uses only:

Income + Education + Family + CCAvg

⚙️ 13. Model Comparison

The classification models were compared using Stratified 5-Fold Cross-Validation.

The model comparison process identified Gradient Boosting as the strongest candidate for further optimization.

flowchart LR
    A["Candidate Models"] --> B["Cross-Validation"]
    B --> C["F1 / Precision / Recall"]
    C --> D["Model Comparison"]
    D --> E["🌳 Gradient Boosting"]

🌳 14. Gradient Boosting + Optuna

The selected Gradient Boosting model was optimized using Optuna.

Optuna searched for a better combination of hyperparameters rather than relying only on manually selected values.

Parameters explored included:

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

xychart-beta
    title "Gradient Boosting F1 Score Improvement"
    x-axis ["Baseline", "Optuna Tuned"]
    y-axis "F1 Score" 0.90 --> 0.95
    bar [0.9274, 0.9393]

The tuned model improved the cross-validation F1 score from 0.9274 to 0.9393.

🎚️ 15. Classification Threshold Optimization

The default classification threshold is:

Probability ≥ 0.50 → Class 1
Probability < 0.50 → Class 0

However, 0.50 is not necessarily the best threshold for an imbalanced marketing problem.

The model probabilities were therefore evaluated across different thresholds.

Selected Threshold

Default Threshold   : 0.5000
Optimized Threshold : 0.3815

flowchart LR
    A["Model Probability"] --> B{"Threshold"}
    B -->|"≥ 0.3815"| C["🎯 Predict Loan Accepted"]
    B -->|"< 0.3815"| D["Predict Not Accepted"]

The optimized threshold improved the balance between Precision and Recall.

📈 16. Final Model Performance

The final model is a Tuned Gradient Boosting Classifier.

Test Set Performance

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

Performance Overview

xychart-beta
    title "Final Model Performance"
    x-axis ["Accuracy", "Precision", "Recall", "F1", "ROC-AUC", "PR-AUC"]
    y-axis "Score (%)" 0 --> 100
    bar [98.80, 95.65, 91.67, 93.62, 99.80, 98.53]

🎯 17. Confusion Matrix

The test-set confusion matrix was:

                 Predicted
                 No      Yes
Actual No        900       4
Actual Yes         8      88

Interpretation



Predicted No

Predicted Yes

Actual No

900

4

Actual Yes

8

88

The model correctly identified 88 of the 96 actual positive customers while producing only 4 false positives.

📈 18. ROC-AUC

The final model achieved a ROC-AUC of 99.80%.

This indicates strong discrimination between customers who accepted and did not accept the personal loan.

flowchart LR
    A["ROC-AUC"] --> B["99.80%"]
    B --> C["Strong Class Separation"]

📊 19. Precision-Recall Performance

The final model achieved a PR-AUC of 98.53%.

PR-AUC is particularly useful here because the positive class represents only 9.6% of the dataset.

flowchart LR
    A["Imbalanced Dataset"] --> B["9.6% Positive"]
    B --> C["Precision-Recall Evaluation"]
    C --> D["PR-AUC = 98.53%"]

💡 20. Business Interpretation

The model can be used to rank existing customers according to their likelihood of accepting a personal loan.

Instead of contacting every customer:

flowchart TD
    A["5,000 Existing Customers"]
    A --> B["ML Prediction"]
    B --> C["Loan Probability"]
    C --> D["Customer Ranking"]
    D --> E["🎯 High-Potential Customers"]
    E --> F["📣 Targeted Marketing"]
    F --> G["📈 Potentially Better Conversion"]

This creates a more data-driven customer targeting strategy.

🚀 21. Deployment

The final model was serialized using Joblib and deployed through Streamlit on Render.

The deployed application uses the four selected features:

Input

Purpose

💰 Income

Customer income

🎓 Education

Education category

👨‍👩‍👧‍👦 Family

Family size

💳 CCAvg

Average credit-card spending

Prediction Flow

flowchart LR
    A["User Inputs"] --> B["Preprocessing"]
    B --> C["Trained Gradient Boosting"]
    C --> D["Probability"]
    D --> E["Threshold = 0.3815"]
    E --> F["🎯 Final Prediction"]

🖥️ 22. Application

The deployed Streamlit application provides an interactive interface for entering customer information and receiving a real-time prediction.

Application Output

🎯 Predicted Class
📊 Loan Acceptance Probability
⚙️ Optimized Decision Threshold

Live Application

<a href="https://customer-loan-conversion-prediction-cr9k.onrender.com/">
🚀 Open Customer Loan Conversion Prediction
</a>

🛠️ 23. Technology Stack

Category

Technologies

🐍 Programming

Python

📊 Data Processing

Pandas, NumPy

📈 Visualization

Matplotlib, Seaborn

🤖 Machine Learning

Scikit-learn

🌳 Final Model

Gradient Boosting

⚙️ Optimization

Optuna

💾 Serialization

Joblib

🖥️ Application

Streamlit

☁️ Deployment

Render

🔧 Version Control

Git, GitHub

📁 24. Project Structure

Customer-Loan-Conversion-Prediction/
│
├── README.md
├── app.py
├── requirements.txt
├── .gitignore
│
├── data/
│   └── Bank_Personal_Loan_Modelling.csv
│
├── models/
│   └── bank_loan_model.pkl
│
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_modeling.ipynb
│
└── reports/
    └── analysis_report.html

💻 25. Run Locally

Clone the repository

git clone https://github.com/Koushikmaity014/-Customer-Loan-Conversion-Prediction.git

Navigate to the project

cd Customer-Loan-Conversion-Prediction

Install dependencies

pip install -r requirements.txt

Run the application

streamlit run app.py

📌 26. Project Highlights

<div align="center">

Achievement

Result

👥 Dataset

5,000 Customers

🎯 Positive Class

9.6%

🧠 Final Features

4

🌳 Final Model

Tuned Gradient Boosting

⚡ Hyperparameter Tuning

Optuna

🔄 Validation

Stratified 5-Fold CV

🎚️ Optimized Threshold

0.3815

📈 Test F1

93.62%

🎯 ROC-AUC

99.80%

📊 PR-AUC

98.53%

🚀 Deployment

Streamlit + Render

</div>

📚 27. Learning Outcomes

This project demonstrates practical experience with:

Exploratory Data Analysis

Data preprocessing

Imbalanced classification

Feature selection

Permutation feature importance

Model comparison

Stratified cross-validation

Gradient Boosting

Optuna hyperparameter optimization

Classification threshold optimization

Precision

Recall

F1 Score

ROC-AUC

PR-AUC

Confusion matrix analysis

Model serialization

Streamlit development

Cloud deployment

🔗 28. Project Links

💻 GitHub Repository

https://github.com/Koushikmaity014/-Customer-Loan-Conversion-Prediction

🚀 Live Application

https://customer-loan-conversion-prediction-cr9k.onrender.com/

👨‍💻 29. Author

<div align="center">

Koushik Maity

M.Sc. Mathematics & Computing

Indian Institute of Technology Guwahati

<a href="https://github.com/Koushikmaity014">
<img src="https://img.shields.io/badge/GitHub-Koushikmaity014-181717?style=for-the-badge&logo=github&logoColor=white">
</a>

<br><br>

<a href="https://customer-loan-conversion-prediction-cr9k.onrender.com/">
<img src="https://img.shields.io/badge/Live%20Project-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
</a>

</div>

<div align="center">

⭐ If you found this project useful, consider giving the repository a star!

Thank you for visiting! 🚀

</div>

