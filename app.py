import streamlit as st

st.set_page_config(page_title="One-Hour Box Calculator", layout="wide")

st.title("One-Hour Box Calculator")
st.write("Input the one-hour high and low to calculate extension targets and stop losses.")

one_hour_high = st.number_input("One-Hour High", value=0.0, step=0.25, format="%.2f")
one_hour_low = st.number_input("One-Hour Low", value=0.0, step=0.25, format="%.2f")

if one_hour_high <= one_hour_low:
    st.error("The one-hour high must be greater than the one-hour low.")
    st.stop()

box_range = one_hour_high - one_hour_low
quarter_range = box_range * 0.25
half_range = box_range * 0.5

bullish_tp_100 = one_hour_high + box_range
bearish_tp_100 = one_hour_low - box_range

bullish_sl_50 = one_hour_high - half_range
bearish_sl_50 = one_hour_low + half_range

bullish_tp_25 = one_hour_high + quarter_range
bearish_tp_25 = one_hour_low - quarter_range
bullish_sl_25 = one_hour_high - quarter_range
bearish_sl_25 = one_hour_low + quarter_range

bullish_tp_50 = one_hour_high + half_range
bearish_tp_50 = one_hour_low - half_range

st.metric("Box Range", f"{box_range:.2f}")

st.subheader("100% Extension")
bull_col, bear_col = st.columns(2)
with bull_col:
    st.metric("Bullish TP 100%", f"{bullish_tp_100:.2f}")
    st.metric("Bullish SL 50%", f"{bullish_sl_50:.2f}")
with bear_col:
    st.metric("Bearish TP 100%", f"{bearish_tp_100:.2f}")
    st.metric("Bearish SL 50%", f"{bearish_sl_50:.2f}")

st.subheader("25% Levels")
bull_col, bear_col = st.columns(2)
with bull_col:
    st.metric("Bullish TP 25%", f"{bullish_tp_25:.2f}")
    st.metric("Bullish SL 25%", f"{bullish_sl_25:.2f}")
with bear_col:
    st.metric("Bearish TP 25%", f"{bearish_tp_25:.2f}")
    st.metric("Bearish SL 25%", f"{bearish_sl_25:.2f}")

st.subheader("50% Levels")
bull_col, bear_col = st.columns(2)
with bull_col:
    st.metric("Bullish TP 50%", f"{bullish_tp_50:.2f}")
    st.metric("Bullish SL 50%", f"{bullish_sl_50:.2f}")
with bear_col:
    st.metric("Bearish TP 50%", f"{bearish_tp_50:.2f}")
    st.metric("Bearish SL 50%", f"{bearish_sl_50:.2f}")

if box_range > 100:
    st.warning("Box range is over 100; consider using 25% or 50% levels for more conservative targets.")
else:
    st.info("For larger ranges, consider using the 25% or 50% levels as conservative targets.")
