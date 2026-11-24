import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(
    page_title="Excel Cleaner Pro",
    page_icon="📊"
)

st.title("📊 Excel Cleaner Pro")
st.write("Clean your Excel data in seconds.")

uploaded = st.file_uploader(
    "Upload your Excel file",
    type=["xlsx"]
)

if uploaded is not None:
    df = pd.read_excel(uploaded)
    original = len(df)

    st.subheader("Original Data")
    st.dataframe(df)

    if st.button("Clean Data"):
        df.columns = df.columns.str.strip()

        for col in df.select_dtypes(include="object"):
            df[col] = df[col].map(
                lambda x: x.strip() if isinstance(x, str) else x
            )

        df = df.replace(r"^\s*$", pd.NA, regex=True)

        df = df.dropna(how="all")
        df = df.drop_duplicates()

        st.success("Cleaning completed!")

        st.metric("Original rows", original)
        st.metric("Cleaned rows", len(df))
        st.metric("Removed rows", original - len(df))

        st.subheader("Cleaned Data")
        st.dataframe(df)

        output = BytesIO()
        df.to_excel(output, index=False)

        st.download_button(
            "Download Cleaned Excel",
            data=output.getvalue(),
            file_name="cleaned_data.xlsx"
        )
