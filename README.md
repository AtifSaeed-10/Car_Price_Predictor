# 🏎️ Car Price Predictor

**Live App → [https://akjq65jkmgct4nhf8vdukc.streamlit.app/](https://akjq65jkmgct4nhf8vdukc.streamlit.app/)**

A machine learning web app that estimates used car prices in the Pakistani market. Enter your car's details and get an instant PKR valuation.

---

## What It Does

Plug in your car's brand, model, year, mileage, fuel type, seats, and condition — and the model spits out a price estimate based on real market data.

**Supported brands:** Toyota, Suzuki, Honda, Hyundai, Nissan, Kia, Daihatsu, and others

**Supported models:** Alto, Aqua, Baleno, Civic, Corolla, Cultus, Fortuner, Prius, Sportage, Vitz, and 30+ more

---

## Run It Locally

**Requirements:** Python 3.8+

```bash
# Clone the repo
git clone <your-repo-url>
cd <repo-folder>

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run Car.py
```

The app will open at `http://localhost:8501`

> Make sure `car_price_model.pkl` is in the same folder as `Car.py`.

---

## Project Files

| File | Purpose |
|------|---------|
| `Car.py` | Main Streamlit app |
| `car_price_model.pkl` | Trained ML model |
| `requirements.txt` | Python dependencies |

---

## How the Model Works

The model is trained on Pakistani used car listings and uses features like car age (derived from model year), mileage, number of seats, condition score, brand, model, and fuel type. These are one-hot encoded and fed into a regression model to predict market price in PKR.

---

## Dependencies

- `streamlit` — web UI
- `scikit-learn` — ML pipeline
- `xgboost` — regression model
- `pandas` — data handling
- `joblib` — model loading
