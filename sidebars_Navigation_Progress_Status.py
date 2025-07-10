import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-darkgrid")  # more modern style

# Original data
data = {
    "num": [x for x in range(1, 11)],
    "Square": [x ** 2 for x in range(1, 11)],
    "Twice": [x * 2 for x in range(1, 11)],
    "Thrice": [x * 3 for x in range(1, 11)]
}

# Create dataframe
df = pd.DataFrame(data)

# Friendly display names
display_names = {
    "num": "Number",
    "Square": "Squared",
    "Twice": "Double",
    "Thrice": "Triple"
}

# Let user pick multiple columns
selected_cols = st.sidebar.multiselect(
    "Select columns to plot:", df.columns, default=["num"]
)

# If nothing selected, show message
if not selected_cols:
    st.warning("Please select at least one column to display the graph.")
else:
    fig, ax = plt.subplots(figsize=(8, 5))

    x = df.index + 1  # X-axis: index 1–10

    colors = plt.cm.tab10.colors  # get nice colors

    for idx, col in enumerate(selected_cols):
        y = df[col]
        label = display_names.get(col, col)  # use friendly name
        ax.plot(
            x, y,
            marker='o',
            linestyle='-',
            linewidth=2,
            markersize=6,
            color=colors[idx % len(colors)],
            label=label
        )

    ax.set_xlabel("Index", fontsize=12)
    ax.set_ylabel("Value", fontsize=12)
    ax.set_title("Selected Data Plots", fontsize=14, weight='bold')
    ax.legend(title="Lines", fontsize=10)
    ax.grid(True)

    st.pyplot(fig)