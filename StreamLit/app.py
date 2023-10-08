import inspect
import textwrap

import datetime

import streamlit as st
from PIL import Image

dataPath = "../data/final_df"

def main():
    st.title("Delfos: a geomagnetic storm prediction tool")

    with st.sidebar:
        #logo = Image.open("delfos-logo.png")
        #logo = logo.resize((70,70))
        #st.image(logo)
        
        st.title("Configuration")
        st.header("Start date for the model")
        st.write("The start date will determine from which moment the model starts learning, starting from January 2016.")
        
        start_date = st.date_input("Start date", value = None)

        st.header("End date for the model")
        st.write("The maximum date available is December 30th 2022")
        end_date = st.date_input("End date", value = None)

        st.header("Prediction time")
        st.write("The prediction will be made in the following 3 hours after the imputed date")

        prediction_time = st.time_input("Prediction time", value=None, step=11800)

        return start_date, end_date, prediction_time


if __name__ == "__main__":
    st.set_page_config(
        page_title="Streamlit ECharts Demo", page_icon=":chart_with_upwards_trend:"
    )
    start_date, end_date, prediction_time = main()

    if start_date is not None and end_date is not None and prediction_time is not None:

        start_date_str = start_date.strftime("%Y-%m-%d")
        end_date_str = end_date.strftime("%Y-%m-%d")

        # Valida que las fechas sean válidas
        start_date_obj = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date_obj = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
        st.write(str(type(end_date_obj.year)))

        # Valida que las fechas estén entre el 1 de enero de 2016 y el 30 de diciembre de 2022
        if start_date_obj >= datetime.datetime(2016, 1, 1) and end_date_obj <= datetime.datetime(2022, 12, 30):
            st.markdown("---")
            st.markdown("### Data Visualization")
            st.markdown("---")
            st.markdown("### The model itself")




    with st.sidebar:
        st.markdown("---")
        st.title("Delfos")

