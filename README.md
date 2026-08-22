# 🏦 Customer Loan Conversion Prediction

An end-to-end machine learning project for predicting whether an existing bank customer is likely to accept a personal loan.

The project combines exploratory data analysis, feature selection, model comparison, stratified cross-validation, Optuna hyperparameter optimization, classification-threshold tuning, and deployment using Streamlit.

### 🚀 Live Demo

**[Try the deployed application](https://customer-loan-conversion-prediction-cr9k.onrender.com/)**

### 💻 GitHub Repository

**[View the complete source code](https://github.com/Koushikmaity014/-Customer-Loan-Conversion-Prediction/)**

---

## 🎯 Business Problem

Banks often have a large base of existing customers who use deposit and other banking services but may also be potential personal-loan customers.

The objective of this project is to identify customers who are more likely to accept a personal loan so that the bank can focus its marketing campaign on high-potential customers instead of contacting the entire customer base.

This can help improve campaign efficiency while reducing unnecessary marketing expenditure.

---

## 📊 Dataset

The project uses the **Bank Personal Loan Modelling** dataset obtained from Kaggle.

The dataset contains information about **5,000 bank customers** and includes demographic, financial, and banking-relationship attributes.

The target variable is:

* `Personal Loan = 1` → Customer accepted the personal loan
* `Personal Loan = 0` → Customer did not accept the personal loan

The dataset contains 480 positive cases out of 5,000 customers, resulting in a positive-class rate of approximately **9.6%**.

The exploratory profiling confirmed 5,000 observations, no missing cells, and no duplicate rows in the analyzed dataset.

---

## 🧩 Features

| Feature            | Description                                      |
| ------------------ | ------------------------------------------------ |
| Age                | Customer age                                     |
| Experience         | Years of professional experience                 |
| Income             | Annual income in $1,000s                         |
| ZIP Code           | Customer ZIP code                                |
| Family             | Number of family members                         |
| CCAvg              | Average monthly credit-card spending in $1,000s  |
| Education          | Education level                                  |
| Mortgage           | Mortgage value                                   |
| Securities Account | Whether the customer has a securities account    |
| CD Account         | Whether the customer has a CD account            |
| Online             | Whether the customer uses online banking         |
| CreditCard         | Whether the customer uses the bank's credit card |
| Personal Loan      | Target variable                                  |

---

## 🔎 Exploratory Data Analysis

The analysis included:

* Data structure and data-type analysis
* Missing-value analysis
* Duplicate detection
* Target-class distribution
* Numerical feature distributions
* Categorical feature analysis
* Outlier analysis
* Correlation analysis
* Feature-versus-target analysis
* Customer segmentation analysis

### Key findings

* The target variable is highly imbalanced, with only **9.6% positive cases**.
* `Income` has a strong relationship with personal-loan acceptance.
* `Age` and `Experience` are highly correlated.
* `Income` and `CCAvg` are highly correlated.
* No missing values were found.
* No duplicate rows were found.

Because of the class imbalance, accuracy alone was not used as the primary model-selection criterion.

---

## 🤖 Machine Learning Approach

The project follows the following workflow:

```text
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
```

---

## 🧠 Feature Selection

Permutation-based feature importance was used to identify the most useful predictors.

The final selected feature set for the Gradient Boosting model was:

```text
Income
Education
Family
CCAvg
```

Reducing the model to these features provided a compact model while maintaining strong predictive performance.

---

## ⚙️ Model Selection

Multiple classification approaches were evaluated using **Stratified 5-Fold Cross-Validation**.

Gradient Boosting performed particularly well and was selected for further optimization.

The model was then optimized using **Optuna** to search for an effective combination of hyperparameters.

The tuned Gradient Boosting model improved the cross-validation F1 score from approximately **0.9274 to 0.9393**.

---

## 🎚️ Classification Threshold Optimization

Because only 9.6% of customers accepted the loan, using the default classification threshold of 0.5 is not necessarily optimal.

Instead of directly using:

```python
model.predict(X)
```

the project uses predicted probabilities and evaluates alternative thresholds.

The optimized threshold was approximately:

```text
0.3815
```

This improved the out-of-fold F1 score while increasing recall and maintaining high precision.

This approach is particularly useful for a marketing campaign where identifying more potential customers can be more valuable than simply maximizing overall accuracy.

---

## 📈 Final Model Performance

The final tuned Gradient Boosting model achieved the following results on the held-out test set:

| Metric    |      Score |
| --------- | ---------: |
| Accuracy  | **98.80%** |
| Precision | **95.65%** |
| Recall    | **91.67%** |
| F1 Score  | **93.62%** |
| ROC-AUC   | **99.80%** |
| PR-AUC    | **98.53%** |

### Confusion Matrix

```text
                 Predicted
                 No      Yes
Actual No        900       4
Actual Yes         8      88
```

The model correctly identified **88 of the 96 actual positive customers** in the test set while producing only **4 false positives**.

---

## 🚀 Deployment

The final model was serialized using Joblib and deployed as an interactive **Streamlit** web application.

The application allows users to enter:

* Annual Income
* Education Level
* Number of Family Members
* Monthly Credit Card Spending

and generates:

* Predicted class
* Probability of loan acceptance
* Classification threshold

The deployed application loads the trained pipeline, selected feature list, and optimized threshold directly from the saved model artifact.

### 🌐 Live Application

**[Customer Loan Conversion Prediction](https://customer-loan-conversion-prediction-cr9k.onrender.com/)**

---

## 🛠️ Tech Stack

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Scikit-learn**
* **Optuna**
* **Joblib**
* **Streamlit**
* **Git/GitHub**
* **Render**

---

## 📁 Project Structure

```text
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
    ├── target_distribution.png
    ├── feature_importance.png
    ├── model_comparison.png
    ├── confusion_matrix.png
    └── app_screenshot.png
```

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/Koushikmaity014/-Customer-Loan-Conversion-Prediction.git
cd -Customer-Loan-Conversion-Prediction
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📌 Key Takeaways

This project demonstrates an end-to-end machine learning workflow rather than only model training.

Key components include:

* Business problem formulation
* Exploratory data analysis
* Handling an imbalanced classification problem
* Feature selection
* Multiple-model comparison
* Stratified cross-validation
* Hyperparameter optimization with Optuna
* Classification-threshold optimization
* Evaluation using precision, recall, F1, ROC-AUC and PR-AUC
* Model serialization
* Interactive Streamlit application
* Cloud deployment

---

## 👨‍💻 Author

**Koushik Maity**

M.Sc. Mathematics & Computing
IIT Guwahati

[GitHub](https://github.com/Koushikmaity014)

