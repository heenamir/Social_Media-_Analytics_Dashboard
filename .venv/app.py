if __name__ == "__main__":
    import streamlit as st
    import pandas as pd

    # Load data
    df = pd.read_excel("your_youtube_data.xlsx")

    # Streamlit app layout
    st.title("YouTube Dataset Dashboard")

    # Display data
    st.write("## YouTube Dataset Overview")
    st.write(df)

    # Add interactive components
    st.sidebar.header("Filters")
    selected_category = st.sidebar.selectbox("Select Category", df["Category"].unique())

    # Filter data based on user selection
    filtered_df = df[df["Category"] == selected_category]

    # Display filtered data
    st.write("## Filtered YouTube Dataset")
    st.write(filtered_df)
