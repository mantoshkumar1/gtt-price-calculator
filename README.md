# Zerodha GTT Price Calculator

A simple Streamlit app to calculate valid Good Till Triggered (GTT) buy and sell trigger prices based on Zerodha’s rules.

Website: https://gtt-calculator.streamlit.app/

**Note:** Any change to this codebase is automatically reflected on the above **streamlit.app** 

---

## Features:

- Calculates minimum trigger prices based on Zerodha’s requirements:
  - For stocks priced ₹50 or above, trigger price must be at least 0.25% away from current price.
  - For stocks priced below ₹50, trigger price must be at least ₹0.09 away.
- Interactive web app you can run locally or deploy easily.

---

## Installation

1. Clone or download this repository.

2. Make sure you have Python 3.7+ installed.

3. (Optional but recommended) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
````

4. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the App Locally

Run this command in your terminal:

```bash
streamlit run app.py
```

Your default browser should open the app. If not, visit `http://localhost:8501`.

---

## Usage

* Enter the current stock price in the input box.
* The app will show you the minimum valid GTT buy and sell trigger prices according to Zerodha’s rules.

---

## Deploying Online

You can easily deploy this app on [Streamlit Cloud](https://share.streamlit.io) by connecting your GitHub repo.