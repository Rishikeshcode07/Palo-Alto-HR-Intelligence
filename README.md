# Palo Alto HR Intelligence Dashboard 

(image alt )! (https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://palo-alto-dashboard.streamlit.app/)

##  Project Overview (STAR Framework)

###  Situation
In large organizations like Palo Alto Networks, HR departments often struggle to identify employees who are at a high risk of attrition due to career stagnation or lack of timely promotions. Understanding employee segments based on their experience, role tenure, and promotion gaps is critical for retaining top talent.

###  Task
The objective of this project was to build a data-driven HR analytics solution. The task involved processing employee data, identifying stagnation risks, and building a highly interactive dashboard to help HR managers visualize these insights easily and make proactive retention decisions.

###  Action
To solve this, I developed an interactive web application using **Python** and **Streamlit**. 
- Performed Data Analysis and segmentation using **Pandas**.
- Created advanced, interactive visualizations using **Plotly**, including custom-themed 3D scatter plots and bar charts optimized for dark mode.
- Handled UI/UX issues to ensure the dashboard is highly readable and professional.
- Deployed the final application on **Streamlit Community Cloud** for global, permanent access.

###  Result
Successfully launched a live, interactive HR Intelligence Dashboard. The tool allows HR teams to visually identify "Promotion-Stalled / Stagnant Profiles" versus "Fast-Trackers". This actionable intelligence empowers management to reduce attrition and improve employee satisfaction.

---

##  Live Dashboard
**Access the live project here:** [Palo Alto HR Dashboard](https://palo-alto-dashboard.streamlit.app/)

---

##  Project Screenshots

### 1. Dashboard Overview
> *(Add your screenshot here showing the main top section of the dashboard)*
![Dashboard Overview](link-to-screenshot-1)

### 2. 3D Role Stagnation & Experience Mapping
> *(Add your screenshot here showing the 3D Scatter Plot with the dark mode fix)*
![image alt].(https://github.com/user-attachments/assets/9e7ac552-496b-4b0a-bc3e-274f7c2d1428)

### 3. Career Segment Distribution
> *(Add your screenshot here showing the Bar Chart and clear legends)*
![Segment Distribution](link-to-screenshot-3)

---

##  Tech Stack
* **Language:** Python
* **Web Framework:** Streamlit
* **Data Manipulation:** Pandas, NumPy
* **Data Visualization:** Plotly Express
* **Deployment:** Streamlit Community Cloud

---

##  How to Run Locally

1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   python -m streamlit run 3_app.py
