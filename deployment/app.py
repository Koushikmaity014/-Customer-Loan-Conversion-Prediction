import joblib
import pandas as pd
import streamlit as st


# --------------------------------------------------
# Page settings
# --------------------------------------------------

st.set_page_config(
    page_title="Personal Loan Prediction",
    page_icon="🏦",
    layout="centered"
)


# --------------------------------------------------
# Load model
# --------------------------------------------------

model_data = joblib.load("bank_loan_model.pkl")

model = model_data["pipeline"]
features = model_data["features"]
threshold = float(model_data["threshold"])


# --------------------------------------------------
# Page heading
# --------------------------------------------------

st.title("🏦 Personal Loan Prediction")

st.write(
    "This application predicts whether a customer is likely "
    "to accept a personal loan."
)

st.divider()


# --------------------------------------------------
# Input form
# --------------------------------------------------

st.subheader("Customer Information")

with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:

        income = st.number_input(
            "Annual Income (in $1,000s)",
            min_value=0.0,
            value=50.0,
            step=1.0,
            help="Example: 50 means $50,000 per year."
        )

        family = st.selectbox(
            "Number of Family Members",
            options=[1, 2, 3, 4]
        )

    with col2:

        education_name = st.selectbox(
            "Education Level",
            options=[
                "Undergraduate (UG)",
                "Postgraduate (PG)",
                "Advanced / Professional"
            ]
        )

        ccavg = st.number_input(
            "Monthly Credit Card Spending (in $1,000s)",
            min_value=0.0,
            value=1.0,
            step=0.1,
            help="Example: 1.5 means $1,500 per month."
        )

    predict_button = st.form_submit_button(
        "Predict Loan Acceptance",
        type="primary",
        use_container_width=True
    )


# --------------------------------------------------
# Convert education value
# --------------------------------------------------

education_mapping = {
    "Undergraduate (UG)": 1,
    "Postgraduate (PG)": 2,
    "Advanced / Professional": 3
}


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if predict_button:

    education = education_mapping[education_name]

    input_data = pd.DataFrame({
        "Income": [float(income)],
        "Education": [int(education)],
        "Family": [int(family)],
        "CCAvg": [float(ccavg)]
    })

    # Keep the same feature order used during training
    input_data = input_data[features]

    # Probability of class 1
    probability = model.predict_proba(input_data)[0, 1]

    # Convert probability into class 0 or 1
    prediction = int(probability >= threshold)

    st.divider()
    st.subheader("Prediction Result")

    if prediction == 1:

        st.success(
            "Predicted Class: 1\n\n"
            "The customer is likely to accept the personal loan."
        )

    else:

        st.info(
            "Predicted Class: 0\n\n"
            "The customer is unlikely to accept the personal loan."
        )

    st.metric(
        label="Final Predicted Class",
        value=prediction
    )

    with st.expander("View prediction details"):

        st.write(
            f"Probability of accepting the loan: "
            f"{probability:.2%}"
        )

        st.write(
            f"Classification threshold: "
            f"{threshold:.2%}"
        )

        st.dataframe(
            input_data,
            use_container_width=True,
            hide_index=True
        )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Class 0: Customer will not accept the loan | "
    "Class 1: Customer will accept the loan"
)

st.caption(
    "Model: Tuned Gradient Boosting Classifier"
)
