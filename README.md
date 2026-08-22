<div align="center">

# 🏦 Customer Loan Conversion Prediction

### End-to-End Machine Learning System for Personal Loan Conversion

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
  <img src="https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?style=flat-square&logo=scikit-learn&logoColor=white">
  <img src="https://img.shields.io/badge/Optuna-Hyperparameter%20Tuning-4B8BBE?style=flat-square">
  <img src="https://img.shields.io/badge/Streamlit-Deployment-FF4B4B?style=flat-square&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/Render-Cloud%20Deployment-46E3B7?style=flat-square&logo=render&logoColor=black">
</p>

</div>

---

## 📸 Application Preview

<p align="center">
  <img src="images/app_screenshot.png" width="850">
</p>

<p align="center">
  <b>Interactive Streamlit application for real-time customer loan conversion prediction.</b>
</p>

---

## 🚀 Live Application

<p align="center">

<a href="https://customer-loan-conversion-prediction-cr9k.onrender.com/">

<img src="https://img.shields.io/badge/OPEN%20LIVE%20APPLICATION-00C853?style=for-the-badge&logo=streamlit&logoColor=white">

</a>

</p>

---

# 📌 Project Overview

**Customer Loan Conversion Prediction** is an end-to-end machine learning project developed to predict whether an existing bank customer is likely to accept a personal loan.

The project uses customer demographic, financial, and banking relationship information to identify high-potential customers and support more targeted marketing campaigns.

The complete workflow covers **Exploratory Data Analysis, Data Preprocessing, Feature Selection, Model Comparison, Stratified Cross-Validation, Optuna Hyperparameter Optimization, Classification Threshold Optimization, Model Evaluation, Model Serialization, and Streamlit Deployment.**

---

# 🎯 Business Problem

Banks have a large number of existing customers who use their deposit and other banking services. Some of these customers may also be potential personal-loan customers.

The objective is to identify customers who are more likely to accept a personal loan so that the bank can focus its marketing campaign on high-potential customers instead of contacting the entire customer base.

### Business Benefits

- 🎯 Better customer targeting
- 📈 Higher potential loan conversion
- 💰 Reduced marketing expenditure
- ⚡ More efficient campaigns
- 👥 Identification of high-potential customers

---

# 📊 Dataset

The project uses the **Bank Personal Loan Modelling** dataset obtained from **Kaggle**.

The dataset contains information about **5,000 bank customers**, including demographic, financial, and banking relationship attributes.

### Dataset Summary

| Property | Value |
|---|---:|
| 👥 Total Customers | **5,000** |
| ✅ Loan Accepted | **480** |
| ❌ Loan Not Accepted | **4,520** |
| 🎯 Positive Class | **9.6%** |
| 🎯 Target Variable | **Personal Loan** |

### Target Variable

```text
Personal Loan = 0 → Customer did not accept the loan

Personal Loan = 1 → Customer accepted the loan

