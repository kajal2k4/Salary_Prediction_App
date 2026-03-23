import streamlit as st
import pickle
import numpy as np  # import numpy for safe conversion

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit UI
st.title("Salary Prediction App")
exp = st.number_input("Enter experience (years)", min_value=0, max_value=50, value=1)

# Predict button
if st.button("Predict"):
    # Make prediction
    result = model.predict([[exp]])
    
    # Safely convert prediction to a scalar
    predicted_salary = int(np.array(result).item())
    
    # Display result
    st.write(f"Predicted salary: {predicted_salary}")
    