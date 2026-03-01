import streamlit as st
import joblib
import pandas as pd
import datetime
import time

# 1. Page Configuration
st.set_page_config(
    page_title="Car Price Predictor | Pro",
    page_icon="🏎️",
    layout="wide"
)

# 2. Premium UI Styling (CSS)
bg_img_url = "https://images.unsplash.com/photo-1503376780353-7e6692767b70?q=80&w=1920"

st.markdown(f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.85)), url("{bg_img_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .main-title {{
        font-family: 'Helvetica Neue', sans-serif;
        color: #FFFFFF;
        font-weight: 800;
        font-size: 3.5rem;
        text-align: center;
        margin-bottom: 5px;
        letter-spacing: -1px;
    }}
    .sub-title {{
        color: #999;
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 40px;
        font-weight: 300;
        text-transform: uppercase;
        letter-spacing: 2px;
    }}
    .input-container {{
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 30px;
        backdrop-filter: blur(10px);
    }}
    label {{
        color: #ccc !important;
        font-size: 0.9rem !important;
        text-transform: uppercase;
    }}
    .result-card {{
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        backdrop-filter: blur(15px);
        box-shadow: 0 25px 50px rgba(0,0,0,0.5);
    }}
    .stButton>button {{
        width: 100%;
        background: #FFFFFF;
        color: #000;
        font-weight: 700;
        border-radius: 4px;
        border: none;
        height: 3.5em;
        margin-top: 20px;
    }}
    </style>
    """, unsafe_allow_html=True)

# 3. Load Model
@st.cache_resource
def load_model():
    import os
    model_path = os.path.join(os.path.dirname(__file__), 'car_price_model.pkl')
    return joblib.load(model_path)

model = load_model()

# EXACT columns as they appeared in your Notebook (Even if Daihatsu is missing here, reindex will fix it)
FEATURES = ['Car_Age', 'Mileage', 'Seats', 'Condition', 'Brand_Honda', 'Brand_Hyundai', 'Brand_Kia', 'Brand_Nissan', 'Brand_Others', 'Brand_Suzuki', 'Brand_Toyota', 'Model_Alto', 'Model_Aqua', 'Model_Baleno', 'Model_Bolan', 'Model_City', 'Model_Civic', 'Model_Corolla', 'Model_Cultus', 'Model_Dayz', 'Model_Elantra', 'Model_Fortuner', 'Model_Hilux', 'Model_Khyber', 'Model_Liana', 'Model_Mehran', 'Model_Moco', 'Model_N wgn', 'Model_Others', 'Model_Passo', 'Model_Prius', 'Model_Raize', 'Model_Ravi', 'Model_Santa fe', 'Model_Sonata', 'Model_Sorento', 'Model_Sportage', 'Model_Surf', 'Model_Swift', 'Model_Tucson', 'Model_Vezel', 'Model_Vitz', 'Model_Wagon r', 'Model_Yaris', 'Fuel_Hybrid', 'Fuel_Others', 'Fuel_Petrol']

# 4. Header
st.markdown("<h1 class='main-title'>CAR PRICE PREDICTOR</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Market Valuation Engine V1.0</p>", unsafe_allow_html=True)

# 5. Dashboard
_, center_col, _ = st.columns([1, 2, 1])

with center_col:
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        brand = st.selectbox("Vehicle Brand", ["Toyota", "Suzuki", "Honda", "Hyundai", "Nissan", "Kia", "Daihatsu", "Others"])
    with col_b:
        model_list = sorted([f.replace('Model_', '') for f in FEATURES if 'Model_' in f])
        model_name = st.selectbox("Vehicle Model", model_list)

    c1, c2 = st.columns(2)
    with c1:
        year = st.number_input("Model Year", 1990, 2026, 2020)
        fuel = st.selectbox("Engine Type", ["Petrol", "Hybrid", "Others"])
    with c2:
        mileage = st.number_input("Odometer (km)", 0, 500000, 50000)
        seats = st.selectbox("Seats", [2, 4, 5, 7, 8], index=2)
        
    condition = st.select_slider("Overall Grade (1-10)", options=list(range(1, 11)), value=8)
    
    predict_btn = st.button("RUN ANALYSIS")
    st.markdown('</div>', unsafe_allow_html=True)

# 6. Prediction Logic
if predict_btn:
    with st.spinner('Analyzing vehicle data...'):
        time.sleep(0.5) 
        
        car_age = datetime.datetime.now().year - year
        
        # Dictionary for input
        input_dict = {
            'Car_Age': car_age,
            'Mileage': mileage,
            'Seats': seats,
            'Condition': condition,
            f'Brand_{brand}': 1,
            f'Model_{model_name}': 1,
            f'Fuel_{fuel}': 1
        }
        
        df_input = pd.DataFrame([input_dict])

        try:
            # Check what model actually needs (Dynamic Fix)
            actual_needed_features = model.feature_names_in_
            
            # Reindex ensures all missing columns are 0 and order is 100% correct
            df_final = df_input.reindex(columns=actual_needed_features, fill_value=0)
            
            prediction = model.predict(df_final)[0]
            
            st.markdown(f"""
                <div class="result-card">
                    <p style='color: #aaa; letter-spacing: 2px; font-size: 0.8rem; margin-bottom: 0;'>ESTIMATED VALUE</p>
                    <h1 style='color: #FFF !important; font-size: 3.5rem; margin: 10px 0;'>PKR {prediction:,.0f}</h1>
                    <p style='color: #888; border-top: 1px solid #333; padding-top: 15px;'>
                        {brand.upper()} {model_name.upper()} | {year} | {fuel.upper()}
                    </p>
                </div>
                """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("<br><p style='text-align: center; color: #444; font-size: 0.7rem;'>AI DRIVEN VALUATION SYSTEM</p>", unsafe_allow_html=True)