import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

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

# Navigation on Side bar
rad=st.sidebar.radio("Navigation",["Home","About Us","Status Messages","Progress Bar"])

# Multi select on Side bar
if rad=="Home":
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
        
if rad=="About Us":
    st.write("About Page")
    
if rad=="Status Messages":
    st.error("Error Status")
    st.success("Success Status")
    st.info("Information Status")
    st.exception(RuntimeError("Exception: RuntimeError Status"))
    st.warning("Warning Status")

if rad == "Progress Bar":
    st.subheader("Progress Bar Animation")
    st.write("Click the button below to run the loading animation!")

    if st.button("Run Animation"):
        progress = st.progress(0, text="Starting...")
        status_text = st.empty()

        for percent_complete in range(101):
            time.sleep(0.05)  # ~5 seconds total
            progress.progress(percent_complete, text=f"Loading... {percent_complete}%")

            if percent_complete == 25:
                status_text.info("🕹️ Loading Assets...")
                time.sleep(0.2)
            elif percent_complete == 50:
                status_text.info("⚙️ Optimizing...")
                time.sleep(0.2)
            elif percent_complete == 75:
                status_text.info("✨ Almost Ready...")
                time.sleep(0.2)

        status_text.success("✅ Done! Ready to go!")
        st.balloons()

        # Reset progress bar to 0
        time.sleep(1)  # Optional pause before reset
        progress.progress(0, text="Progress reset.")