import streamlit as st
import pickle
import pandas as pd

# Custom CSS for background color and header styling
st.markdown(
    """
    <style>
    .main {
        background-image: url('./bg.png');
        background-size: cover;
        background-position: center;
    }
    .header {
        font-size: 40px;
        font-weight: bold;
        color: #8B4513;
    }
    .streamlit-expanderHeader {
        color: #008000;  /* Change the expander header color */
    }
    .stButton>button {
        background-color: #FFA500; /* Button color */
        color: white;
    }
    .stButton>button:hover { 
        color: black; 
    }
    h1 { 
        color: green; 
    }


    /* Prediction output text */
    .stWrite {
        font-size: 20px;
        font-weight: bold;
    }

    .rainfall {
        color: #32CD32; /* Green for rainfall */
    }

    .no_rainfall {
        color: #FF6347; /* Tomato color for no rainfall */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the trained model from the dictionary in the pickle file
with open('rainfall_prediction_model.pkl', 'rb') as file:
    model_data = pickle.load(file)
    model = model_data["model"]  # Extract the model
    feature_names = model_data["feature_names"]  # Extract the feature names (optional)

# Define a function to make predictions
def predict_rainfall(input_data):
    prediction = model.predict([input_data])
    return prediction[0]

# Main page title and description
st.title("🌧️ Rainfall Prediction Web App")
st.write("This app predicts rainfall based on the provided weather features.")

# Sidebar for inputs
st.sidebar.title("Input Features")
st.sidebar.write("Provide values for each feature:")


# Input fields with tooltips and placeholders
feature_1 = st.sidebar.number_input("Pressure", value=None, step=1.0, placeholder="Enter value", help="Atmospheric pressure")
feature_2 = st.sidebar.number_input("Dewpoint", value=None, step=1.0, placeholder="Enter value", help="Temperature where air becomes saturated")
feature_3 = st.sidebar.number_input("Humidity", value=None, step=1.0, placeholder="Enter value", help="Humidity percentage")
feature_4 = st.sidebar.number_input("Cloud", value=None, step=1.0, placeholder="Enter value", help="Cloud coverage")
feature_5 = st.sidebar.number_input("Sunshine", value=None, step=1.0, placeholder="Enter value", help="Hours of sunshine")
feature_6 = st.sidebar.number_input("Wind Direction", value=None, step=1.0, placeholder="Enter value", help="Direction of wind in degrees")
feature_7 = st.sidebar.number_input("Wind Speed", value=None, step=1.0, placeholder="Enter value", help="Wind speed in km/h")

# "Clear All" button to reset inputs
if st.sidebar.button("Clear All"):
    feature_1, feature_2, feature_3, feature_4, feature_5, feature_6, feature_7 = None, None, None, None, None, None, None


# Prepare input data for prediction
input_data = [feature_1, feature_2, feature_3, feature_4, feature_5, feature_6, feature_7]

# Check if all input values are provided
if st.button("Predict Rainfall"):
    if None in input_data:
        # Display a warning message if the button is clicked without filling all fields
        st.warning("Please enter values for all the input fields before making a prediction.")
    else:
        # If all fields are filled, proceed with the prediction
        prediction = predict_rainfall(input_data)
        
        if prediction == 1:
            st.write("<p class='rainfall'>🌧️ There will be rainfall.</p>", unsafe_allow_html=True)
        else:
            st.write("<p class='no_rainfall'>🚫 There will not be rainfall.</p>", unsafe_allow_html=True)

# Expandable section with explanation
with st.expander("ℹ️ About This App"):
    st.write("""
        This app uses machine learning to predict rainfall based on various meteorological features.
        Input your data into the fields on the left, and click **Predict Rainfall** to get the prediction.
        The prediction values are estimates based on historical data and are meant for informational purposes.
    """)
    st.write("Model trained on features like Pressure, Dewpoint, Humidity, Cloud Coverage, Sunshine, Wind Direction, and Wind Speed.")