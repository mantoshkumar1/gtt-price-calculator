import streamlit as st
import math
from functools import partial

def calculate_gtt_prices(current_price, rounding_multiple):
    """
    Calculate GTT buy/sell trigger prices based on Zerodha rules:
    - If price >= 50, min trigger distance > 0.25% of price
    - Else, min trigger distance = ₹0.09

    @param current_price: Current stock price
    @param rounding_multiple: Rounding multiple for GTT prices (Rounding Multiple is the granularity at which the GTT price must be placed)
    @return: Tuple of (gtt_buy_price, gtt_sell_price, warning_message)
    """
    if current_price >= 50:
        min_distance = current_price * 0.00256
    else:
        min_distance = 0.09

    # GTT prices should be a multiple of "rounding_multiple"
    gtt_buy_price = current_price - min_distance
    gtt_sell_price = current_price + min_distance

    if rounding_multiple <= 0: # Handle zero or invalid rounding multiple gracefully
        gtt_buy_price = round(gtt_buy_price, 2)
        gtt_sell_price = round(gtt_sell_price, 2)
        warning_message = "⚠️ Trigger prices are not rounded. Use a value like 0.05 for valid prices."
        return gtt_buy_price, gtt_sell_price, warning_message

    gtt_buy_price = round(gtt_buy_price/rounding_multiple) * rounding_multiple
    gtt_buy_price = round(gtt_buy_price, 2)

    gtt_sell_price = round(gtt_sell_price/rounding_multiple) * rounding_multiple
    gtt_sell_price = round(gtt_sell_price, 2)

    warning_message = ""
    return gtt_buy_price, gtt_sell_price, warning_message

# ------------------ Session State Init ------------------

defaults = {
    "buy_shares": 0,
    "buy_amount": 0.0,
    "buy_last_edited": None,
    "sell_shares": 0,
    "sell_amount": 0.0,
    "sell_last_edited": None,
}

for k, v in defaults.items():
    st.session_state.setdefault(k, v)

# ------------------ Callbacks ------------------

def buy_shares_changed(buy_trigger):
    st.session_state.buy_last_edited = "shares"
    if st.session_state.buy_shares > 0:
        st.session_state.buy_amount = math.floor(st.session_state.buy_shares * buy_trigger * 100)/100

def buy_amount_changed(buy_trigger):
    st.session_state.buy_last_edited = "amount"
    if st.session_state.buy_amount > 0:
        st.session_state.buy_shares = math.floor(st.session_state.buy_amount / buy_trigger)

def sell_shares_changed(sell_trigger):
    st.session_state.sell_last_edited = "shares"
    if st.session_state.sell_shares > 0:
        st.session_state.sell_amount = math.floor(st.session_state.sell_shares * sell_trigger * 100)/100

def sell_amount_changed(sell_trigger):
    st.session_state.sell_last_edited = "amount"
    if st.session_state.sell_amount > 0:
        st.session_state.sell_shares = math.floor(st.session_state.sell_amount / sell_trigger)


# ------------------ UI ------------------

st.title("Zerodha GTT Price Calculator")

st.markdown("""
**Zerodha GTT Trigger Price Rules:**  
- For stocks priced ₹50 or more: Trigger price must be at least 0.25% away from current price.  
- For stocks under ₹50: Trigger price must be at least ₹0.09 away.
- GTT price should be a multiple of 0.05

Use this calculator to find valid buy and sell trigger prices.  
Optionally enter shares or amount to see order size automatically.
""")

user_input = st.text_input("Enter Current Stock Price (₹):", placeholder="e.g. 115.50")

rounding_multiple = st.number_input(
    "Round trigger prices to nearest multiple of:",
    value=0.05, step=0.05, format="%.2f"
)

if user_input:
    try:
        price = float(user_input)
        if price <= 0:
            st.warning("❌ Please enter a price greater than 0.")
            st.stop()

        buy_trigger, sell_trigger, rounding_note = calculate_gtt_prices(price, rounding_multiple)
        if rounding_note:
            st.warning(rounding_note)
            st.stop()

        # ------------------ BUY ORDER ------------------
        st.success(f"✅ GTT Buy Trigger: ₹{buy_trigger}")
        default_num_buy_shares = 1

        # Create two columns, 50% each
        col1, col2 = st.columns(2)

        with col1:
            st.number_input(
                "Buy Amount (₹)",
                min_value=default_num_buy_shares * buy_trigger,
                step=10000.0,
                format="%.2f",
                key="buy_amount",
                on_change=partial(buy_amount_changed, buy_trigger)
            )

        with col2:
            st.number_input(
                "Buy Shares",
                min_value=default_num_buy_shares,
                step=100,
                key="buy_shares",
                on_change=partial(buy_shares_changed, buy_trigger)
            )

        # ------------------ SELL ORDER ------------------
        st.success(f"✅ GTT Sell Trigger: ₹{sell_trigger}")
        default_num_sell_shares = 1

        # Create two columns, 50% each
        col1, col2 = st.columns(2)

        with col1:
            st.number_input(
                "Sell Amount (₹)",
                min_value=sell_trigger * default_num_sell_shares,
                step=10000.0,
                format="%.2f",
                key="sell_amount",
                on_change=partial(sell_amount_changed, sell_trigger)
            )

        with col2:
            st.number_input(
                "Sell Shares",
                min_value=default_num_sell_shares,
                step=100,
                key="sell_shares",
                on_change=partial(sell_shares_changed, sell_trigger)
            )

    except ValueError:
        st.error("❌ Invalid input. Please enter a valid number.")

