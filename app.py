# ============================================================
# LUNG CANCER PREDICTION APP
# ============================================================
# Technologies Used:
# Python | Streamlit | KNN | Scikit-learn | MySQL
#
# Purpose:
# This application predicts whether a person is classified
# as a lung cancer patient based on the input features.
# ============================================================


# -------------------- IMPORT LIBRARIES --------------------

import streamlit as st
import pickle
from PIL import Image
import pymysql


# -------------------- DATABASE CONNECTION --------------------

# Connect to MySQL database
conn = pymysql.connect(
    host=st.secrets["mysql"]["host"],
    user=st.secrets["mysql"]["user"],
    password=st.secrets["mysql"]["password"],
    db=st.secrets["mysql"]["database"]
)

cursor = conn.cursor()


# -------------------- APPLICATION FUNCTION --------------------

def main():

    # -------------------- PAGE TITLE --------------------

    st.set_page_config(
        page_title="Lung Cancer Prediction",
        layout="centered"
    )

    st.title('Lung Cancer Prediction')

    # -------------------- DISPLAY IMAGE --------------------

    img = Image.open('lung_image.png')
    st.image(img, width=700)


    # -------------------- USER INPUT --------------------

    st.subheader('Enter Patient Details')

    age = st.number_input(
        'Enter Age:',
        min_value=1,
        max_value=120,
        value=25
    )

    smoke = st.number_input(
        'Enter Smoking Score:',
        min_value=0.0
    )

    areaq = st.number_input(
        'Enter Area Quality:',
        min_value=0.0
    )

    alcohol = st.number_input(
        'Enter Alcohol Consumption:',
        min_value=0.0
    )


    # -------------------- CREATE FEATURE LIST --------------------

    # The order of features must be the same as the
    # order used while training the ML model.

    feature = [age, smoke, areaq, alcohol]


    # -------------------- LOAD ML MODEL --------------------

    # Load the trained KNN model
    knn = pickle.load(
        open('knn_model.sav', 'rb')
    )

    # Load the scaler used during model training
    scaler = pickle.load(
        open('knn_scaler.sav', 'rb')
    )

    # -------------------- PREDICTION BUTTON DESIGN --------------------

    st.markdown(
        """
        <style>

        /* Predict Button */
        div.stButton > button {
            background-color: #2563EB;
            color: white;
            width: 200px;
            height: 50px;
            font-size: 18px;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            margin: 20px auto;
            display: block;
            box-shadow: 0px 4px 10px rgba(37, 99, 235, 0.3);
        }

        /* Hover Effect */
        div.stButton > button:hover {
            background-color: #1D4ED8;
            color: white;
            box-shadow: 0px 6px 15px rgba(37, 99, 235, 0.4);
        }

        </style>
        """,
        unsafe_allow_html=True
    )


    # -------------------- PREDICTION --------------------

    if st.button('Predict'):

        # Scale the user input before making prediction
        scaled_feature = scaler.transform([feature])

        # Make prediction using the trained KNN model
        result = knn.predict(scaled_feature)

        # Convert prediction array into an integer
        result = int(result[0])


        # -------------------- DISPLAY RESULT --------------------

        if result == 0:
            st.success('Prediction: Not a cancer patient')
        else:
            st.error('Prediction: Cancer patient')


        # -------------------- SAVE PREDICTION --------------------

        # Store prediction details in MySQL database
        query = '''
        INSERT INTO prediction_history
        (age, smoke, areaq, alcohol, result)
        VALUES (%s, %s, %s, %s, %s)
        '''

        values = [
            age,
            smoke,
            areaq,
            alcohol,
            result
        ]

        cursor.execute(query, values)

        # Save changes to database
        conn.commit()

        st.info('Prediction data saved successfully.')


# -------------------- RUN APPLICATION --------------------

if __name__ == '__main__':
    main()