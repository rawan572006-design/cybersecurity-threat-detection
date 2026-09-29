# 🛡️ Cybersecurity Threat Detection

A machine learning project that detects whether network traffic is **Normal** or represents a potential **Cybersecurity Attack**.

The project includes data exploration, feature engineering, machine learning model training, model inference, and a FastAPI-based web interface for real-time predictions.

---

## 📌 Project Overview

Cybersecurity systems generate large amounts of network traffic data. Detecting malicious traffic manually can be difficult and time-consuming.

This project uses **Machine Learning** to analyze network traffic features and classify each connection as:

* 🟢 **Normal**
* 🔴 **Attack**

The trained model is integrated into a web application where users can enter network traffic information and receive a prediction with a confidence score.

---

## 🗂️ Project Structure

```text
cybersecurity-threat-detection/
│
├── app/
│   └── index.html
│
├── data/
│   └── raw/
│       └── cybersecurity.csv
│
├── models/
│   └── cybersecurity_model.joblib
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering_modeling.ipynb
│   └── 03_model_inference.ipynb
│
├── src/
│   └── api.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

The dataset contains network traffic information used to identify potential cybersecurity threats.

The main features used by the model include:

| Feature               | Description                               |
| --------------------- | ----------------------------------------- |
| `src_port`            | Source port number                        |
| `dst_port`            | Destination port number                   |
| `protocol`            | Network protocol                          |
| `bytes_sent`          | Number of bytes sent                      |
| `bytes_received`      | Number of bytes received                  |
| `user_agent`          | User agent information                    |
| `is_internal_traffic` | Indicates whether the traffic is internal |

The target represents whether the traffic is **Normal** or an **Attack**.

---

## 🔎 Data Exploration

The first notebook:

`01_data_exploration.ipynb`

is used for exploring and understanding the dataset.

It includes:

* Dataset inspection
* Data types
* Missing values
* Statistical analysis
* Target distribution
* Feature analysis
* Data visualization

---

## ⚙️ Feature Engineering & Model Training

The second notebook:

`02_feature_engineering_modeling.ipynb`

contains the preprocessing and machine learning workflow.

The workflow includes:

1. Preparing the input features
2. Handling categorical features
3. Feature preprocessing
4. Splitting the data
5. Training the machine learning model
6. Evaluating the model
7. Saving the trained model

The trained model is saved as:

```text
models/cybersecurity_model.joblib
```

---

## 🧪 Model Inference

The third notebook:

`03_model_inference.ipynb`

is used to test the trained model with new network traffic data.

The model returns:

* Predicted class
* Prediction probability
* Human-readable result
* Confidence percentage

Example:

```text
Prediction: Attack
Confidence: 100%
```

or:

```text
Prediction: Normal
Confidence: 100%
```

---

## 🚀 FastAPI

The trained model is integrated into a **FastAPI** application.

The API is implemented in:

```text
src/api.py
```

The API provides a prediction endpoint:

```text
POST /predict
```

It receives network traffic information and returns the model prediction and confidence.

---

## 🌐 Web Interface

The project also includes a simple web interface:

```text
app/index.html
```

Users can enter:

* Source Port
* Destination Port
* Protocol
* Bytes Sent
* Bytes Received
* User Agent
* Internal Traffic

After clicking **Predict**, the application displays the detected class and confidence.

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone <repository-url>
cd cybersecurity-threat-detection
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

#### Windows

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the FastAPI server

From the project root:

```bash
uvicorn src.api:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

From the documentation page, the `/predict` endpoint can be tested directly.

---

## 💻 Using the Web Interface

Open:

```text
http://127.0.0.1:8000/app
```

Enter the network traffic information and click:

**Predict**

The application will display:

```text
Result: Attack
Confidence: 100%
```

or:

```text
Result: Normal
Confidence: 90%
```

depending on the model prediction.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib
* FastAPI
* HTML
* JavaScript
* Jupyter Notebook
* Git & GitHub

---

## 🎯 Project Goal

The main goal of this project is to demonstrate how machine learning can be integrated into a cybersecurity workflow to automatically detect potentially malicious network traffic.

The project combines:

**Data Analysis → Feature Engineering → Machine Learning → Model Inference → API → Web Interface**

---

## 👩‍💻 Project Workflow

```text
Network Traffic Data
        ↓
Data Exploration
        ↓
Feature Engineering
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Saved ML Model
        ↓
FastAPI
        ↓
Web Interface
        ↓
Attack / Normal Prediction
```

---

## 📌 Future Improvements

Possible future improvements include:

* Adding more machine learning models
* Improving model evaluation
* Adding additional cybersecurity features
* Improving the web interface
* Adding prediction history
* Deploying the API online
* Adding authentication and security features

---

## 📄 License

This project was created for educational and academic purposes.
