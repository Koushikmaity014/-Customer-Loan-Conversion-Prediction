<div align="center">

# 🏦 Customer Loan Conversion Prediction

### 🎯 Predicting Which Bank Customers Are Most Likely to Accept a Personal Loan

<a href="https://customer-loan-conversion-prediction-cr9k.onrender.com/">
<img src="https://img.shields.io/badge/🚀%20LIVE%20DEMO-TRY%20THE%20MODEL-00C853?style=for-the-badge&logo=streamlit&logoColor=white">
</a>

&nbsp;&nbsp;

<a href="https://github.com/Koushikmaity014/-Customer-Loan-Conversion-Prediction">
<img src="https://img.shields.io/badge/💻%20GITHUB-SOURCE%20CODE-181717?style=for-the-badge&logo=github&logoColor=white">
</a>

<br><br>

<img src="image/project_first_page.png" width="1000" height="500">

</div>

---
# 📌 Project Overview

**Customer Loan Conversion Prediction** is an end-to-end machine learning project developed to predict whether an existing bank customer is likely to accept a personal loan.

The project uses customer demographic, financial, and banking relationship information to identify customers who have a higher probability of accepting a personal loan. The main goal is to help the bank perform more **targeted and data-driven marketing** instead of contacting every customer.

The project follows a complete machine learning workflow, starting from **data exploration and preprocessing** and continuing through **model development, feature selection, cross-validation, hyperparameter optimization, threshold optimization, model evaluation, and deployment**.

### 🎯 Objective

> **To build a classification model that can identify customers with a high probability of accepting a personal loan and support more effective targeted marketing campaigns.**

### 🔄 Project Workflow

<p align="center">
  <img src="image/project overview.png" width="950">
</p>
</div>

---
# 💼 Business Problem

Banks have a large number of existing customers, but only a small proportion of them may be interested in purchasing a personal loan.

In this project, the bank wants to identify customers who are more likely to accept a personal loan so that marketing campaigns can focus on high-potential customers rather than contacting the entire customer base.

The previous campaign had a conversion rate of **9.6%**, with only **480 out of 5,000 customers** accepting the personal loan. This creates a challenging **imbalanced classification problem** where accurately identifying the positive customers is more important than simply maximizing overall accuracy.

## 🎯 Business Goal

The primary goal is to build a machine learning system that can:

- 🎯 Identify customers with a higher probability of accepting a personal loan.
- 📣 Support targeted marketing campaigns.
- 💰 Reduce unnecessary marketing efforts.
- 📈 Improve the efficiency of customer targeting.
- 🤝 Help the bank focus on customers with higher conversion potential.

### 🔄 From Mass Marketing to Targeted Marketing
<p align="center">
  <img src="image/business_problem.png" width="500">
</p>
</div>

---
# 📊 Dataset

The project uses the **Bank Personal Loan Modelling** dataset obtained from **Kaggle**. The dataset contains **5,000 bank customers** with demographic, financial, and banking relationship information.

<p align="center">
  <img src="image/data_samary.png" width="800">
</p>

### 🎯 Target Variable

The target variable is **`Personal Loan`**, which indicates whether a customer accepted the personal loan offered during the previous campaign.

**0 → Did not accept the personal loan**  
**1 → Accepted the personal loan**

### ⚠️ Class Distribution

<table>
<tr>

<td width="55%" valign="middle">

Only **480 customers (9.6%)** accepted the loan, while **4,520 customers (90.4%)** did not.

This makes the dataset a **highly imbalanced binary classification problem**.

Because of this class imbalance, model performance is evaluated using **Precision, Recall, F1 Score, ROC-AUC, and PR-AUC** rather than relying on accuracy alone.

</td>

<td width="45%" align="center">

<img src="image/02_target_distribution.png" width="350">

</td>

</tr>
</table>
</div>


---
#  🔎 Exploratory Data Analysis

Exploratory Data Analysis was performed to understand customer characteristics,
feature distributions, relationships between variables, and patterns associated
with personal-loan acceptance.

<p align="center">
  <img src="image/customer_overview.png" width="950">
</p>

### 💡 Key Findings

| Insight | Observation |
|---|---|
| 💰 Income | Strong relationship with loan acceptance |
| 🎓 Education | Different acceptance patterns across education levels |
| 💳 CCAvg | Higher spending is associated with higher loan potential |
| 👤 Age & Experience | Strongly correlated |
| 💵 Income & CCAvg | Strongly correlated |

These observations were used to guide the subsequent **feature selection and model development** stages.

---
# 🧠 Feature Selection

To identify the most informative variables for predicting personal-loan acceptance, **Permutation Feature Importance** was used. This approach measures how much model performance changes when the values of a feature are randomly shuffled.

<p align="center">
  <img src="image/08_feature_importance.png" width="750">
</p>

### 🎯 Selected Features

The feature-selection process identified the following features as the most informative:

| Feature | Description |
|---|---|
| 💰 `Income` | Customer income |
| 🎓 `Education` | Education level |
| 👨‍👩‍👧 `Family` | Number of family members |
| 💳 `CCAvg` | Average credit-card spending |

These selected features were then used in the **subsequent model training and hyperparameter optimization stages**.

### 💡 Key Insight

Feature selection helped reduce the model input to the variables providing the strongest predictive information, resulting in a more focused and interpretable model.

---
# 🤖 Machine Learning Models

Several classification algorithms were evaluated to determine the most suitable model for predicting personal-loan acceptance.

### 🧪 Models Evaluated

| Model | Purpose |
|---|---|
| Logistic Regression | Linear classification baseline |
| K-Nearest Neighbors | Distance-based classification |
| Naive Bayes | Probabilistic classification |
| Decision Tree | Rule-based classification |
| Random Forest | Ensemble-based classification |
| Gradient Boosting | Sequential ensemble learning |
| Support Vector Machine | Margin-based classification |

The models were evaluated using **Stratified 5-Fold Cross-Validation** to maintain the class distribution across validation folds.

### 📏 Evaluation Metrics

Because the dataset is highly imbalanced, multiple evaluation metrics were considered:

- **Precision** — How many predicted positive customers actually accepted the loan.
- **Recall** — How many actual loan customers were correctly identified.
- **F1 Score** — Balance between Precision and Recall.
- **ROC-AUC** — Overall ability to distinguish between the two classes.
- **PR-AUC** — Performance focused on the minority positive class.

The model comparison provided a baseline for selecting the most promising algorithm before applying **feature selection and Optuna hyperparameter optimization**.

---
# ⚡ Hyperparameter Optimization

After comparing the baseline classification models, **Optuna** was used to optimize the hyperparameters of the selected model.

Optuna performs automated hyperparameter search by exploring different parameter combinations and identifying the configuration that provides the best validation performance.

<p align="center">
  <img src="image/04_optuna_improvement.png" width="800">
</p>

### 🎯 Optimization Strategy

The optimization process focused on improving the model's **F1 Score**, which is particularly important for this imbalanced classification problem.

<p align="center">
  <img src="image/optuna.png" width="800">
</p>

---
# 🎚️ Classification Threshold Optimization

The default classification threshold of **0.50** was further optimized to improve the balance between **Precision and Recall**.

Instead of directly using the default probability threshold, different threshold values were evaluated on the validation data and the threshold providing the best **F1 Score** was selected.

<p align="center">
  <img src="image/07_threshold_optimization.png" width="750">
</p>

### 🔄 Optimization Process
<p align="center">
  <img src="image/optimaization_process.png" width="750">
</p>
---
# 🏆 Final Model Performance

After feature selection, Optuna hyperparameter optimization, and classification threshold tuning, the final model was evaluated on the **unseen test dataset**.

<p align="center">
  <img src="image/05_final_model_performance.png" width="800">
</p>

### 📊 Final Test Performance

| Metric | Score |
|---|---:|
| ⚖️ F1 Score | **93.62%** |
| 📈 ROC-AUC | **99.80%** |

### 💡 Performance Summary

The final model achieved a **93.62% F1 Score** and **99.80% ROC-AUC** on the unseen test dataset.

The **F1 Score** reflects the balance between Precision and Recall, while the high **ROC-AUC** indicates that the model has a strong ability to distinguish between customers who accepted and did not accept the personal loan.

The final model combines:

- 🧠 Feature Selection
- ⚡ Optuna Hyperparameter Optimization
- 🎚️ Classification Threshold Optimization
- 🏆 Final Model Evaluation
---
# 🖥️ Streamlit Application

The trained machine learning model was integrated into an interactive **Streamlit application** that allows users to enter customer information and receive a real-time personal-loan prediction.

<p align="center">
  <img src="image/streamlit_screansort.png" width="750">
</p>

### 🎯 Application Features

- 👤 Customer information input
- 💰 Financial and banking information
- 🤖 Real-time loan acceptance prediction
- 📈 Loan acceptance probability
- 🎚️ Optimized classification threshold
- 🧠 Final predicted class

### 🔄 Prediction Flow
<p align="center">
  <img src="image/prediction_flowchart.png" width="750">
</p>
