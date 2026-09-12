import streamlit as st
import pandas as pd
from data_analysis import load_data, basic_eda
from llm import create_llm, analyze_data


# -------------------------
# Page Configuration
# -------------------------

st.set_page_config(
    page_title="AI Data Analyst",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Data Analyst")
st.caption(
    "Upload your dataset and ask questions in natural language."
)


# -------------------------
# File Upload
# -------------------------

uploaded_file = st.file_uploader(
    "Upload CSV or Excel file",
    type=["csv", "xlsx"]
)


if uploaded_file:

    try:

        # -------------------------
        # Load Data
        # -------------------------

        df = load_data(uploaded_file)

        st.success(
            f"Dataset loaded: {df.shape[0]:,} rows × "
            f"{df.shape[1]} columns"
        )


        # -------------------------
        # Data Preview
        # -------------------------

        with st.expander("📋 Data Preview"):

            st.dataframe(
                df,
                use_container_width=True
            )


        # -------------------------
        # Dataset Information
        # -------------------------

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Rows",
            f"{df.shape[0]:,}"
        )

        col2.metric(
            "Columns",
            df.shape[1]
        )

        col3.metric(
            "Missing Values",
            int(df.isna().sum().sum())
        )

        col4.metric(
            "Duplicates",
            int(df.duplicated().sum())
        )


        # -------------------------
        # Basic EDA
        # -------------------------

        eda_result = basic_eda(df)

        with st.expander("🔎 Basic EDA"):

            st.write("### Numerical Columns")

            st.write(
                eda_result["numerical_columns"]
            )


            st.write("### Categorical Columns")

            st.write(
                eda_result["categorical_columns"]
            )


            # Missing values

            if eda_result["missing_values"]:

                st.write("### Missing Values")

                st.dataframe(
                    pd.DataFrame(
                        eda_result["missing_values"].items(),
                        columns=["Column", "Missing Values"]
                    )
                )


            # Statistics

            if eda_result["statistics"]:

                st.write("### Descriptive Statistics")

                st.dataframe(
                    df[
                        eda_result["numerical_columns"]
                    ].describe()
                )


            # Correlation

            if eda_result["correlation"]:

                st.write("### Correlation")

                st.dataframe(
                    df[
                        eda_result["numerical_columns"]
                    ].corr()
                )


        # -------------------------
        # Create LLM
        # -------------------------

        llm = create_llm()


        # -------------------------
        # User Question
        # -------------------------

        question = st.text_area(
            "Ask a question about your data",
            placeholder=(
                "Example: What are the major patterns "
                "and problems in this dataset?"
            )
        )


        # -------------------------
        # Analyze
        # -------------------------

        if st.button(
            "Analyze",
            type="primary"
        ):

            if not question.strip():

                st.warning(
                    "Please enter a question."
                )

            else:

                with st.spinner(
                    "Analyzing your data..."
                ):

                    answer = analyze_data(
                        llm,
                        question,
                        eda_result
                    )


                # -------------------------
                # Display Answer
                # -------------------------

                st.subheader("🤖 Analysis")

                st.markdown(answer)


    except Exception as e:

        st.error(
            f"Error: {e}"
        )