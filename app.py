import streamlit as st

def calculate_gtt_prices(current_price):
    """
    Calculate GTT buy/sell trigger prices based on Zerodha rules:
    - If price >= 50, min trigger distance = 0.25% of price
    - Else, min trigger distance = ₹0.09
    """
    if current_price >= 50:
        min_distance = current_price * 0.0025
    else:
        min_distance = 0.09

    gtt_buy = round(current_price - min_distance, 2)
    gtt_sell = round(current_price + min_distance, 2)

    return gtt_buy, gtt_sell

st.title("Zerodha GTT Price Calculator")

st.markdown("""
**Zerodha GTT Trigger Price Rules:**  
- For stocks priced ₹50 or more: Trigger price must be at least 0.25% away from current price  
- For stocks under ₹50: Trigger price must be at least ₹0.09 away  
Use this calculator to find valid buy and sell trigger prices.
""")

price = st.number_input("Enter Current Stock Price (₹):", min_value=0.01, format="%.2f")

if price:
    buy_trigger, sell_trigger = calculate_gtt_prices(price)
    st.success(f"✅ GTT Buy Trigger: ₹{buy_trigger}")
    st.success(f"✅ GTT Sell Trigger: ₹{sell_trigger}")
