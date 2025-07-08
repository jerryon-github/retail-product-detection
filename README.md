# 📊 Customer Churn Prediction Dashboard

A machine learning-powered dashboard for predicting customer churn using a Random Forest classifier. Built with Streamlit and designed for quick business insights.

---

## 🔧 Tech Stack

- **Python**  
- **Pandas** for data handling  
- **Scikit-learn** for machine learning  
- **Joblib** for model persistence  
- **Streamlit** for interactive UI

---

## 📁 Project Structure

```
customer_churn_dashboard/
├── data/
│   └── churn_data.csv              # Clean dataset
├── model/
│   └── churn_model.pkl             # Trained model
│   └── feature_list.pkl            # Feature schema
├── notebooks/
│   └── modeling.ipynb              # Model training notebook
├── src/
│   └── churn_dashboard.py          # Streamlit app
├── requirements.txt
├── LICENSE
├── README.md
```

---

## 🚀 How to Run Locally

1. **Clone this repository**  
   ```bash
   git clone https://github.com/yourusername/customer-churn-dashboard.git
   cd customer-churn-dashboard
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model (if not already saved)**  
   Open `notebooks/modeling.ipynb` and run all cells.

4. **Run the Streamlit dashboard**  
   ```bash
   streamlit run src/churn_dashboard.py
   ```

---

## 🧪 Sample Features Used

- Gender (Male/Female)  
- Age (numerical)  
- Monthly Charges  
- Tenure (in months)  
- Contract Type (Month-to-month, One year, Two year)

---

## 🌍 Deployment (Streamlit Cloud)

To deploy live:
1. Push this repo to your GitHub.
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Link your GitHub and select this repo.
4. Set the main app file to: `src/churn_dashboard.py`

✅ Your app will be live on the web!

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute it with proper attribution.

---

## 👤 Author

[Jerry]  
[https://github.com/jerryon-github]
