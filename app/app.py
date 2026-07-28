import streamlit as st
import pandas as pd
import requests
import plotly.express as px


# -----------------------------
# Configuration
# -----------------------------

API_URL = "http://127.0.0.1:8000/predict"


st.set_page_config(
    page_title="Mining Quality Prediction",
    page_icon="⛏️",
    layout="wide"
)


# -----------------------------
# Custom CSS
# -----------------------------

st.markdown(
    """
    <style>

    .main-title {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    color: white;
    font-size: 80px;
    font-weight: 800;
    text-align: center;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
    margin-bottom: 10px;
    }
    
    .subtitle {
        color: #b8c6ff;
        font-size: 20px;
        text-align: center;
        margin-top: -25px;
        margin-bottom: 30px;
    }


    .card {

        background-color:#f8f9fa;
        padding:20px;
        border-radius:15px;
        box-shadow:0px 4px 10px rgba(0,0,0,0.1);

    }


    .prediction {

        background-color:#e8f5e9;
        padding:25px;
        border-radius:15px;
        text-align:center;

    }


    .prediction h1 {

        color:#2e7d32;
        font-size:45px;

    }


    </style>

    """,
    unsafe_allow_html=True
)



# -----------------------------
# Header
# -----------------------------


st.markdown(
    '<p class="main-title">⛏️ Mining Quality Prediction Dashboard</p>',
    unsafe_allow_html=True
)


st.markdown(
    '<p class="subtitle">'
    'Predict % Silica Concentrate using Optimized CatBoost Regression Model'
    '</p>',
    unsafe_allow_html=True
)


st.divider()



# -----------------------------
# Upload Dataset
# -----------------------------


uploaded_file = st.file_uploader(
    "📂 Upload Mining Sensor CSV",
    type=["csv"]
)



if uploaded_file:


    df = pd.read_csv(uploaded_file)



    # -----------------------------
    # Dataset Information
    # -----------------------------


    st.subheader("📊 Dataset Overview")


    c1,c2,c3 = st.columns(3)


    with c1:

        st.metric(
            "Total Records",
            f"{df.shape[0]:,}"
        )


    with c2:

        st.metric(
            "Features",
            df.shape[1]
        )


    with c3:

        st.metric(
            "Missing Values",
            df.isnull().sum().sum()
        )



    st.divider()



    # Preview

    with st.expander(
        "View Raw Data"
    ):

        st.dataframe(
            df.head(20),
            use_container_width=True
        )



    # -----------------------------
    # Prediction
    # -----------------------------


    if st.button(
        "🔮 Predict Silica Concentrate",
        use_container_width=True
    ):


        with st.spinner(
            "Running CatBoost Prediction..."
        ):


            try:


                data = df.to_dict(
                    orient="records"
                )


                response = requests.post(
                    API_URL,
                    json=data,
                    timeout=120
                )



                if response.status_code == 200:


                    result = response.json()


                    prediction = result["prediction"]



                    st.success(
                        "Prediction Completed Successfully"
                    )


                    st.divider()



                    # Prediction Card


                    st.markdown(
                    f"""

                    <div class="prediction">

                    <h3>
                    Predicted Silica Concentrate
                    </h3>

                    <h1>
                    {prediction:.3f} %
                    </h1>

                    <p>
                    Target: % Silica Concentrate
                    </p>

                    <p>
                    Model:
                    Optimized CatBoost + Time Features
                    </p>


                    </div>

                    """,
                    unsafe_allow_html=True
                    )



                    st.divider()



                    # -----------------------------
                    # Charts
                    # -----------------------------


                    st.header(
                        "📈 Data Visualization"
                    )



                    # Date conversion

                    if "date" in df.columns:

                        df["date"] = pd.to_datetime(
                            df["date"]
                        )



                    # Silica Trend


                    if "% Silica Concentrate" in df.columns:


                        st.subheader(
                            "Silica Concentrate Trend"
                        )


                        fig = px.line(
                            df,
                            x="date",
                            y="% Silica Concentrate",
                            title="Historical Silica Concentrate"
                        )


                        st.plotly_chart(
                            fig,
                            use_container_width=True
                        )




                    # Process Parameters


                    st.subheader(
                        "⚙️ Mining Process Parameters"
                    )


                    parameters = [

                        "% Iron Feed",
                        "% Silica Feed",
                        "Starch Flow",
                        "Amina Flow",
                        "Ore Pulp pH",
                        "Ore Pulp Density"

                    ]



                    available = [

                        x for x in parameters
                        if x in df.columns

                    ]



                    selected = st.multiselect(

                        "Select Parameters",
                        available,
                        default=available[:2]

                    )



                    if selected:


                        fig2 = px.line(

                            df,
                            y=selected,
                            title="Process Parameter Changes"

                        )


                        st.plotly_chart(

                            fig2,
                            use_container_width=True

                        )



                    # Actual vs Prediction


                    if "% Silica Concentrate" in df.columns:


                        st.subheader(
                            "Actual vs Predicted"
                        )


                        comparison = pd.DataFrame({

                            "Type":[
                                "Actual",
                                "Predicted"
                            ],

                            "Silica":[

                                df[
                                "% Silica Concentrate"
                                ].iloc[-1],

                                prediction

                            ]

                        })



                        fig3 = px.bar(

                            comparison,
                            x="Type",
                            y="Silica",
                            text="Silica",
                            title="Comparison"

                        )


                        st.plotly_chart(

                            fig3,
                            use_container_width=True

                        )



                    # Statistics


                    st.subheader(
                        "📌 Statistical Summary"
                    )


                    st.dataframe(

                        df.describe(),

                        use_container_width=True

                    )



                else:


                    st.error(
                        response.text
                    )



            except requests.exceptions.Timeout:


                st.error(
                    "API took too long to respond"
                )



            except Exception as e:


                st.error(
                    f"Error: {e}"
                )



else:


    st.info(
        "Upload mining sensor CSV file to start prediction"
    )