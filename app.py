import streamlit as st 
from functions import add_sidebar, get_radar_chart, add_predictions


def main():
    st.set_page_config(
        page_title="Breast Cancer Predictor",
        page_icon=":male-doctor:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    with open("assests/style.css") as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

    input_data = add_sidebar()
    with st.container():
        st.title("Breast Cancer Predictor")
        st.write("Please connect this app to your cytology lab to help diagnose breast cancer form your tissue sample. This app predicts using a machine learning model whether a breast mass is benign or malignant based on the measurements it receives from your cytosis lab. You can also update the measurements by hand using the sliders in the sidebar.")
    

    col1, col2 = st.columns([4,1])

    with col1:
        radar_chart = get_radar_chart(input_data)
        st.plotly_chart(radar_chart)

    with col2:
        add_predictions(input_data)


if __name__ == '__main__':
    main()