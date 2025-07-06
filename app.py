import streamlit as st

def calculate_gtt_prices(current_price, rounding_multiple):
    """
    Calculate GTT buy/sell trigger prices based on Zerodha rules:
    - If price >= 50, min trigger distance > 0.25% of price
    - Else, min trigger distance = ₹0.09
    """
    if current_price >= 50:
        min_distance = current_price * 0.00256
    else:
        min_distance = 0.09

    # GTT prices should be a multiple of "rounding_multiple"
    gtt_buy = current_price - min_distance
    gtt_buy = round(gtt_buy/rounding_multiple) * rounding_multiple
    gtt_buy = round(gtt_buy, 2)

    gtt_sell = current_price + min_distance
    gtt_sell = round(gtt_sell/rounding_multiple) * rounding_multiple
    gtt_sell = round(gtt_sell, 2)

    return gtt_buy, gtt_sell

st.title("Zerodha GTT Price Calculator")

st.markdown("""
**Zerodha GTT Trigger Price Rules:**  
- For stocks priced ₹50 or more: Trigger price must be at least 0.25% away from current price.  
- For stocks under ₹50: Trigger price must be at least ₹0.09 away.
- GTT price should be a multiple of 0.05

Use this calculator to find valid buy and sell trigger prices.
""")

user_input = st.text_input("Enter Current Stock Price (₹):", placeholder="e.g. 115.50")

rounding_multiple = st.number_input(
    "Round trigger prices to nearest multiple of:",
    value=0.05, step=0.05, format="%.2f"
)

if user_input:
    try:
        price = float(user_input)
        if price > 0:
            buy_trigger, sell_trigger = calculate_gtt_prices(price, rounding_multiple)
            st.success(f"✅ GTT Buy Trigger: ₹{buy_trigger}")
            st.success(f"✅ GTT Sell Trigger: ₹{sell_trigger}")
        else:
            st.warning("❌ Please enter a price greater than 0.")
    except ValueError:
        st.error("❌ Invalid input. Please enter a valid number.")
