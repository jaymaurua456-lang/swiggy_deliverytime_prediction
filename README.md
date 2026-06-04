![Swiggy Banner](swiggy.jpg)
# 🍔 Swiggy Food Delivery Time Prediction Model & Web App

![Swiggy Food Delivery Banner](https://images.unsplash.com/photo-1526367790999-0150786486a2?auto=format&fit=crop&w=1200&q=80)

---

### 📌 Overview
This project is a Machine Learning-based web application designed to predict the estimated delivery time for Swiggy food orders[cite: 1]. In the on-demand food delivery business, providing accurate delivery estimates is crucial for customer satisfaction and operational efficiency[cite: 1]. The primary goal of this application is to analyze real-time external factors—such as distance, weather, and traffic conditions—to deliver highly accurate, live travel time predictions[cite: 1].

---

### 🛠️ Tech Stack Used
* **Programming Language:** Python[cite: 1]
* **Data Science Libraries:** Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn[cite: 1]
* **Machine Learning Model:** Linear Regression[cite: 1]
* **Web Framework:** Streamlit (for building the interactive User Interface)
* **Version Control & Deployment:** Git, GitHub, and Streamlit Cloud

---

### 📊 Dataset & Feature Engineering
The model is trained on a comprehensive dataset capturing various food delivery scenarios[cite: 1]. To optimize prediction accuracy, several crucial features were processed and analyzed[cite: 1]:
* **Distance_km:** The geographical distance between the restaurant and the customer[cite: 1].
* **Weather Condition:** Weather impacts such as Clear, Rainy, Foggy, Snowy, and Windy conditions[cite: 1].
* **Traffic Level:** Road congestion stages categorized into Low, Medium, and High[cite: 1].
* **Time of Day:** Distribution of orders across Morning, Afternoon, Evening, and Night[cite: 1].
* **Preparation Time & Experience:** The food preparation time at the kitchen and the courier's total years of experience[cite: 1].

Data preprocessing involved handling missing values, encoding categorical variables using Label Encoding, and visualizing data trends using heatmaps and box plots before split-training the model[cite: 1].

---

### 🚀 How It Works
1. **User Input:** Users interact with sliders and dropdown menus on the web UI sidebar to input delivery details.
2. **ML Backend:** The application feeds the user's real-time parameters into the trained backend `LinearRegression` model[cite: 1].
3. **Live Prediction:** The model processes the inputs and instantly displays the expected delivery time in minutes on the main dashboard[cite: 1].

---

### 📁 How to Run Locally
1. Clone this repository: `git clone <your-repo-link>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `streamlit run app.py`
