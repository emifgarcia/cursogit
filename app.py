import pandas as pd
import numpy as np
import streamlit as st
from src.extraction import load_data
import src.answers as asw

st.set_page_config(layout="wide")

def create_dataframe_section(df):
    st.title("Database Section")

    col_1, col_2 = st.columns(2)

    col_1.header("Database")
    col_1.dataframe(df, height=530)

    col_2.header("Data Description")

    data_description = """"
                        | coluna | Descrição |
                        | :----- | --------: |
                        | ID | Identificador da linha/registro |
                        | name | Fabricante e modelo da moto |
    """
    col_2.markdown(data_description)
    return None

def create_answers_section(df):
    st.title("Main Questions Answers")
    st.header("First Round")

    st.subheader("How many bikes are being sold by their owners and how many bikes are being sold by distributors")

    return None

def load_data():
    return pd.read_csv('data/processed/bikes_completed.csv')

def main():
    df_raw = load_data()

    st.dataframe(df_raw)

    df = load_data()

    create_dataframe_section(df)

    create_answers_section(df)

    return None

if __name__ == '__main__':
    main()
    
