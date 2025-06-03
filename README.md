# 🏠 House Price Prediction using Machine Learning

This is a beginner-friendly Machine Learning project that predicts the sale prices of houses using various housing features. Built with `pandas`, `scikit-learn`, and deployed using `Streamlit`.

---

## 🚀 Demo

You can interact with the live app locally by running:

```bash
streamlit run app.py
```
## 📂 Project Structure
```bash
House-Price-Prediction/
│
├── train.csv               # Dataset used for training
├── model.pkl               # Trained Random Forest model
├── app.py                  # Streamlit web app code
├── notebook.ipynb          # Full ML workflow with EDA, training, and evaluation
└── README.md               # Project documentation
```
## 🧠 ML Workflow
1. Data Preprocessing

- Handle missing values

- Encode categorical features

- Feature scaling

2. Modeling

- Linear Regression

- Random Forest Regressor (final model)

3. Evaluation

- Mean Squared Error (MSE)

- R² Score

## 🖥️ Streamlit Web App
The Streamlit app allows users to input housing features and get a predicted house price instantly. It uses the trained model (model.pkl) for real-time inference.

## 🔧 Technologies Used
- Python

- pandas, numpy, scikit-learn

- Streamlit

- joblib

## 📈 Results
Random Forest R² Score: ~0.88

MSE: ~877,722,021

## 📦 How to Run
1. Clone the repo:
```bash
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the app:
```bash
streamlit run app.py
```
## 📌 Notes
- Dataset used: train.csv from Kaggle's House Prices competition.

- Make sure Python is added to your system PATH.

- If streamlit is not installed, run: pip install streamlit

📬 Contact
Feel free to reach out on LinkedIn or open an issue if you have questions!

