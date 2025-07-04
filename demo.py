import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@st.cache_data
def generate_data():
    return pd.DataFrame(
        data = np.random.randint(3, 100, size=(40, 3)),
        columns = ["a", "b", "c"]
    )

data = generate_data()

fig, ax = plt.subplots()
ax.scatter(data["a"], data["b"])
ax.set_xlabel("Time")
ax.set_ylabel("Velocity")
ax.set_title("Acceleration Chart")
st.pyplot(fig)

st.line_chart(data=data)
st.area_chart(data=data)
st.bar_chart(data=data)
st.dataframe(data)



# Lets create a map using streamlib and mark 4 points in it which is delhi, Rajasthan, goa and bengal

locations = pd.DataFrame({
    'lat': [28.6139, 26.9124, 15.2993, 22.5726],
    'lon': [77.2090, 75.7873, 74.1240, 88.3639],
    'place': ['Delhi', 'Rajasthan', 'Goa', 'Bengal']
})

st.title("Indian Locations Map")
# Simple map with points
st.map(locations)

# Show the DataFrame too
st.write("Plotted Points:")
st.dataframe(locations)