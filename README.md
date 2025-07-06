# Zerodha GTT Price Calculator

A simple Python script to calculate the minimum allowed Good Till Triggered (GTT) buy and sell trigger prices based on Zerodha’s rules.

It helps set valid GTT orders avoiding “trigger price out of range” errors

## Why this?

Zerodha requires GTT trigger prices to be set a minimum distance away from the current market price to avoid errors like "trigger price out of range."

- For stocks priced **₹50 or above**, the trigger must be at least **0.25%** away from the last traded price (LTP).
- For stocks priced **below ₹50**, the trigger must be at least **₹0.09** away from LTP.

This script helps you quickly calculate valid buy and sell trigger prices.

## How to Use

1. Clone or download this repo.
2. Run the Python script:

```bash
python gtt_calculator.py
````

3. When prompted, enter the current stock price (positive number).
4. The script will display the recommended GTT buy and sell trigger prices.

## Example

```
Enter Current Stock Price (₹): 120

📌 Based on Zerodha GTT rules:
✅ GTT Buy Trigger  : ₹119.7
✅ GTT Sell Trigger : ₹120.3
```

## License

MIT License
