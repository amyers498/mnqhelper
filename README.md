# Box Calculator

A Streamlit app to calculate "box" targets, stops, and MNQ P&L from a box high/low.

## Features
- Inputs: Box High, Box Low (validated high > low), MNQ Contracts
- Calculations:
  - Box range, quarter/half/eighth segments
  - Targets: 25%, 50%, 100% extensions up/down
  - Stops: scaled to each target (12.5% for 25% TPs, 25% for 50% TPs, 50% for 100% TPs)
  - P&L: $2 per MNQ point per contract for each target/stop
- UI:
  - Range snapshot
  - Tabs for Price Levels and P&L (bullish/bearish)
  - Toggle for a quick "how it works" helper
  - Warning when box range > 100 suggesting 25%/50% targets

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Notes
- Uses only Streamlit (no extra UI libraries).
- Prices and P&L shown with two-decimal formatting.
- Stops and P&L are symmetric for bullish and bearish setups.
