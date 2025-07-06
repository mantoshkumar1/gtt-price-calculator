def calculate_gtt_prices(current_price):
    """
    Calculates GTT Buy and Sell trigger prices based on Zerodha's minimum distance rule.

    Zerodha Rule:
    - If stock price >= ₹50 → trigger must be ≥ 0.25% away from LTP
    - If stock price < ₹50 → trigger must be ≥ ₹0.09 away from LTP

    GTT Buy → Set below LTP
    GTT Sell → Set above LTP
    """

    # 🔍 Rule 1: Determine the minimum distance allowed for GTT trigger
    if current_price >= 50:
        min_distance = current_price * 0.0025  # 0.25% of the price
    else:
        min_distance = 0.09  # Fixed ₹0.09 if stock is below ₹50

    # ✅ GTT Buy Trigger = Current Price - Min Distance
    gtt_buy = round(current_price - min_distance, 2)

    # ✅ GTT Sell Trigger = Current Price + Min Distance
    gtt_sell = round(current_price + min_distance, 2)

    # 🔁 Return both triggers
    return gtt_buy, gtt_sell


# ---------------- RUN BELOW -------------------

# 🧾 Ask user for current market price
price = float(input("Enter Current Stock Price (₹): "))

# 🧮 Calculate triggers
buy_trigger, sell_trigger = calculate_gtt_prices(price)

# 📤 Display result
print(f"\n📌 Based on Zerodha GTT rules:")
print(f"✅ GTT Buy Trigger  : ₹{buy_trigger} (Min allowed below LTP)")
print(f"✅ GTT Sell Trigger : ₹{sell_trigger} (Min allowed above LTP)")
