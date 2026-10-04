# 🫁 Lung Cancer Prediction App

A Machine Learning web application that predicts whether a patient is classified as a lung cancer patient based on selected input features.

The application is built using **Python, KNN, Scikit-learn, Streamlit, and MySQL**.

> ⚠️ **Disclaimer:** This project is created for educational and portfolio purposes only. It is not intended to provide medical diagnosis or clinical advice.

---

## 📌 Project Overview

The **Lung Cancer Prediction App** combines Machine Learning, web application development, and database management into a single end-to-end project.

Users can enter patient-related information through an interactive Streamlit interface. The trained **K-Nearest Neighbors (KNN)** model processes the input after feature scaling and generates a prediction.

The prediction details are then stored in a MySQL database as prediction history.

---

## 🛠️ Technologies Used

* **Python**
* **Scikit-learn**
* **K-Nearest Neighbors (KNN)**
* **Streamlit**
* **MySQL**
* **PyMySQL**
* **Pillow**
* **Pickle**

---

## 🔄 Project Workflow

```text
User Input
     ↓
Feature Creation
     ↓
Feature Scaling
     ↓
Trained KNN Model
     ↓
Prediction
     ↓
Display Result
     ↓
Store Prediction in MySQL
```

---

## ✨ Key Features

* Interactive Streamlit user interface
* Patient input fields
* Input validation
* Feature scaling before prediction
* KNN-based classification
* Prediction result display
* Prediction history stored in MySQL
* Simple and user-friendly interface

---

## 📊 Input Features

The application currently uses the following features:

| Feature             | Description                    |
| ------------------- | ------------------------------ |
| Age                 | Patient age                    |
| Smoking Score       | Smoking-related input value    |
| Area Quality        | Area/environment quality input |
| Alcohol Consumption | Alcohol consumption input      |

---

## 🧠 Machine Learning Model

The application uses the **K-Nearest Neighbors (KNN)** classification algorithm.

Because KNN is distance-based, the input features are scaled using the same scaler that was used during model training.

The trained model and scaler are stored as:

```text
knn_model.sav
knn_scaler.sav
```

---

## 🗄️ Database Integration

The application stores prediction history in a MySQL database.

Database table:

```text
prediction_history
```

Stored information includes:

* Age
* Smoking score
* Area quality
* Alcohol consumption
* Prediction result

The database credentials are stored separately using Streamlit secrets rather than being hard-coded in the application.

---

## 📂 Project Structure

```text
lung-cancer-prediction-app/
│
├── app.py
├── knn_model.sav
├── knn_scaler.sav
├── lung_image.png
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit/
    └── secrets.toml
```

> `secrets.toml` should remain local and should never be uploaded to GitHub.

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/lung-cancer-prediction-app.git
```

### 2. Open the project folder

```bash
cd lung-cancer-prediction-app
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

Create the required MySQL database and table.

Configure your local Streamlit secrets file:

```text
.streamlit/secrets.toml
```

Example:

```toml
[mysql]
host = "localhost"
user = "root"
password = "YOUR_PASSWORD"
database = "lung"
```

### 5. Run the Streamlit application

```bash
streamlit run app.py
```

---

## 🖥️ Application Preview

<img width="1000" height="815" alt="Home_screen" src="https://github.com/user-attachments/assets/4728cec1-93ab-445b-a31c-163fc9f9e78d" />



### Input Screen

*Add your Streamlit application screenshot here.*

### Prediction Result

<img width="1117" height="896" alt="Prediction_result" src="https://github.com/user-attachments/assets/3695f707-cc6f-437a-be28-f54172038a33" />


---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

* Building a Machine Learning classification application
* Using KNN for prediction
* Feature scaling
* Developing interactive applications with Streamlit
* Connecting Python applications with MySQL
* Storing prediction history in a database
* Organizing and documenting a Machine Learning project

---

## 👩‍💻 Author

**Jasna V J**

**Skills:** Python | Machine Learning | KNN | Scikit-learn | Streamlit | MySQL | Data Science
