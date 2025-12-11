import streamlit as st

st.set_page_config(page_title="Box Calculator", layout="wide")

st.title("Box Calculator")
st.write("Input the box high and low to calculate extension targets, stops, and P&L.")
st.caption("Stops scale down: 12.5% for 25% targets, 25% for 50% targets, 50% for 100% targets.")

show_help = st.toggle("Show how it works", value=False)

one_hour_high = st.number_input("Box High", value=0.0, step=0.25, format="%.2f")
one_hour_low = st.number_input("Box Low", value=0.0, step=0.25, format="%.2f")
contracts = st.number_input("MNQ Contracts", min_value=1, value=1)

if one_hour_high <= one_hour_low:
    st.error("The box high must be greater than the box low.")
    st.stop()

if show_help:
    st.info(
        "Enter box high/low and contracts. Targets extend the box (25/50/100%). "
        "Stops shrink relative to targets (12.5/25/50%). P&L uses $2 per MNQ point per contract. "
        "If the box range exceeds 100, consider the 25% or 50% targets for conservative moves."
    )

DOLLARS_PER_POINT = 2

box_range = one_hour_high - one_hour_low
quarter_range = box_range * 0.25
half_range = box_range * 0.5
eighth_range = box_range * 0.125

bullish_tp_100 = one_hour_high + box_range
bearish_tp_100 = one_hour_low - box_range

bullish_tp_25 = one_hour_high + quarter_range
bearish_tp_25 = one_hour_low - quarter_range
bullish_tp_50 = one_hour_high + half_range
bearish_tp_50 = one_hour_low - half_range

# Stops shrink relative to targets: 12.5% for 25% targets, 25% for 50% targets, 50% for 100% targets.
bullish_sl_25 = one_hour_high - eighth_range
bearish_sl_25 = one_hour_low + eighth_range

bullish_sl_50 = one_hour_high - quarter_range
bearish_sl_50 = one_hour_low + quarter_range

bullish_sl_100 = one_hour_high - half_range
bearish_sl_100 = one_hour_low + half_range

bullish_profit_25 = quarter_range * DOLLARS_PER_POINT * contracts
bullish_profit_50 = half_range * DOLLARS_PER_POINT * contracts
bullish_profit_100 = box_range * DOLLARS_PER_POINT * contracts
bullish_loss_25 = -eighth_range * DOLLARS_PER_POINT * contracts
bullish_loss_50 = -quarter_range * DOLLARS_PER_POINT * contracts
bullish_loss_100 = -half_range * DOLLARS_PER_POINT * contracts

# P&L distances are symmetric for bullish and bearish.
bearish_profit_25 = bullish_profit_25
bearish_profit_50 = bullish_profit_50
bearish_profit_100 = bullish_profit_100
bearish_loss_25 = bullish_loss_25
bearish_loss_50 = bullish_loss_50
bearish_loss_100 = bullish_loss_100

st.markdown(
    """
    <style>
    div.block-container {max-width: 1100px;}
    .section-card {
        border: 1px solid #1f2937;
        background: linear-gradient(135deg, #0f172a 0%, #0b1224 100%);
        padding: 16px 18px;
        border-radius: 14px;
        margin-bottom: 12px;
    }
    .section-title {margin: 0 0 6px 0; font-size: 18px;}
    .section-note {margin: 0 0 10px 0; color: #94a3b8; font-size: 13px;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-card"><p class="section-title">Range Snapshot</p><p class="section-note">Key inputs and box size at a glance.</p></div>', unsafe_allow_html=True)
snap_cols = st.columns(4)
snap_cols[0].metric("Box High", f"{one_hour_high:.2f}")
snap_cols[1].metric("Box Low", f"{one_hour_low:.2f}")
snap_cols[2].metric("Box Range", f"{box_range:.2f}")
snap_cols[3].metric("Contracts (MNQ)", f"{contracts}")

price_tab, pl_tab = st.tabs(["Price Levels", "P&L (USD)"])

with price_tab:
    st.markdown('<div class="section-card"><p class="section-title">100% Extension</p><p class="section-note">Full-box targets with 50% stop of the box.</p></div>', unsafe_allow_html=True)
    bull_col, bear_col = st.columns(2)
    with bull_col:
        st.metric("Bullish TP 100%", f"{bullish_tp_100:.2f}")
        st.metric("Bullish SL for 100% TP", f"{bullish_sl_100:.2f}")
    with bear_col:
        st.metric("Bearish TP 100%", f"{bearish_tp_100:.2f}")
        st.metric("Bearish SL for 100% TP", f"{bearish_sl_100:.2f}")

    st.markdown('<div class="section-card"><p class="section-title">50% Levels</p><p class="section-note">Half-box targets with 25% stop of the box.</p></div>', unsafe_allow_html=True)
    bull_col, bear_col = st.columns(2)
    with bull_col:
        st.metric("Bullish TP 50%", f"{bullish_tp_50:.2f}")
        st.metric("Bullish SL for 50% TP", f"{bullish_sl_50:.2f}")
    with bear_col:
        st.metric("Bearish TP 50%", f"{bearish_tp_50:.2f}")
        st.metric("Bearish SL for 50% TP", f"{bearish_sl_50:.2f}")

    st.markdown('<div class="section-card"><p class="section-title">25% Levels</p><p class="section-note">Quarter-box targets with 12.5% stop of the box.</p></div>', unsafe_allow_html=True)
    bull_col, bear_col = st.columns(2)
    with bull_col:
        st.metric("Bullish TP 25%", f"{bullish_tp_25:.2f}")
        st.metric("Bullish SL for 25% TP", f"{bullish_sl_25:.2f}")
    with bear_col:
        st.metric("Bearish TP 25%", f"{bearish_tp_25:.2f}")
        st.metric("Bearish SL for 25% TP", f"{bearish_sl_25:.2f}")

with pl_tab:
    st.markdown('<div class="section-card"><p class="section-title">Bullish P&L</p><p class="section-note">Profit and stop loss per target.</p></div>', unsafe_allow_html=True)
    bull_rows = st.columns(3)
    with bull_rows[0]:
        st.metric("Profit @ 25% TP", f"${bullish_profit_25:.2f}")
        st.metric("Loss @ SL for 25% TP", f"${bullish_loss_25:.2f}")
    with bull_rows[1]:
        st.metric("Profit @ 50% TP", f"${bullish_profit_50:.2f}")
        st.metric("Loss @ SL for 50% TP", f"${bullish_loss_50:.2f}")
    with bull_rows[2]:
        st.metric("Profit @ 100% TP", f"${bullish_profit_100:.2f}")
        st.metric("Loss @ SL for 100% TP", f"${bullish_loss_100:.2f}")

    st.markdown('<div class="section-card"><p class="section-title">Bearish P&L</p><p class="section-note">Same distances apply for shorts.</p></div>', unsafe_allow_html=True)
    bear_rows = st.columns(3)
    with bear_rows[0]:
        st.metric("Profit @ 25% TP", f"${bearish_profit_25:.2f}")
        st.metric("Loss @ SL for 25% TP", f"${bearish_loss_25:.2f}")
    with bear_rows[1]:
        st.metric("Profit @ 50% TP", f"${bearish_profit_50:.2f}")
        st.metric("Loss @ SL for 50% TP", f"${bearish_loss_50:.2f}")
    with bear_rows[2]:
        st.metric("Profit @ 100% TP", f"${bearish_profit_100:.2f}")
        st.metric("Loss @ SL for 100% TP", f"${bearish_loss_100:.2f}")

if box_range > 100:
    st.warning("Box range is over 100; consider using 25% or 50% levels for more conservative targets.")
else:
    st.info("For larger ranges, consider using the 25% or 50% levels as conservative targets.")
