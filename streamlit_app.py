import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go

# Import the model utilities
from src.ENDTOENDDSPROJECT.models.model_data import get_model_and_preprocessor, load_model_from_b64

# Get the model and preprocessor data
model_b64, preprocessor_b64 = get_model_and_preprocessor()

@st.cache_resource
def load_model():
    if model_b64 is None or preprocessor_b64 is None:
        st.error("Error: Could not load the model. Please ensure model files are properly saved.")
        return None, None
    return load_model_from_b64(model_b64, preprocessor_b64)

def predict(features):
    model, preprocessor = load_model()
    
    if model is None or preprocessor is None:
        st.error("Error: Model not available. Please check your setup.")
        return None
        
    try:
        # Transform features using the preprocessor
        features_processed = preprocessor.transform(features)
        # Make prediction
        prediction = model.predict(features_processed)
        return prediction
    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")
        return None

def home_page():
    # Hero Section
    st.markdown("""
        <div style='text-align: center; padding: 2em;'>
            <h1 style='font-size: 3em; margin-bottom: 0.5em; color: #00cc66;'>🌱 Soil Fertility Prediction System</h1>
            <p style='font-size: 1.2em; color: #cccccc; margin-bottom: 2em;'>
                Empowering agricultural decisions with AI-driven soil analysis
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Feature Cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class='feature-card'>
                <h3 style='color: #00cc66; margin-bottom: 1em;'>🧪 Smart Analysis</h3>
                <p style='color: #cccccc;'>Advanced machine learning algorithms process multiple soil parameters for accurate fertility assessment.</p>
                <div style='background: rgba(0, 204, 102, 0.1); padding: 10px; border-radius: 5px; margin-top: 1em;'>
                    <small style='color: #00cc66;'>Features: pH, NPK, Organic Matter</small>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class='feature-card'>
                <h3 style='color: #00cc66; margin-bottom: 1em;'>⚡ Instant Results</h3>
                <p style='color: #cccccc;'>Get immediate fertility predictions and actionable recommendations for your soil samples.</p>
                <div style='background: rgba(0, 204, 102, 0.1); padding: 10px; border-radius: 5px; margin-top: 1em;'>
                    <small style='color: #00cc66;'>Real-time processing & insights</small>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class='feature-card'>
                <h3 style='color: #00cc66; margin-bottom: 1em;'>📊 Data-Driven</h3>
                <p style='color: #cccccc;'>Powered by comprehensive soil analysis data and advanced visualization tools.</p>
                <div style='background: rgba(0, 204, 102, 0.1); padding: 10px; border-radius: 5px; margin-top: 1em;'>
                    <small style='color: #00cc66;'>Interactive charts & analytics</small>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # System Overview
    st.markdown("""
        <div style='margin-top: 3em; padding: 2em; background: rgba(0, 204, 102, 0.05); border-radius: 15px;'>
            <h2 style='color: #00cc66; margin-bottom: 1em;'>System Overview</h2>
            <p style='color: #cccccc; margin-bottom: 2em;'>
                Our AI-powered system analyzes multiple soil parameters to provide accurate fertility predictions and recommendations.
            </p>
            <div style='display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;'>
                <div style='background: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 10px;'>
                    <h4 style='color: #00cc66;'>Key Parameters</h4>
                    <ul style='color: #cccccc; list-style-type: none; padding-left: 0;'>
                        <li>🔵 pH Level (Soil acidity/alkalinity)</li>
                        <li>🟢 Organic Matter Content</li>
                        <li>🟡 NPK Levels (Nutrient content)</li>
                        <li>🟣 Geographic Factors</li>
                    </ul>
                </div>
                <div style='background: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 10px;'>
                    <h4 style='color: #00cc66;'>System Benefits</h4>
                    <ul style='color: #cccccc; list-style-type: none; padding-left: 0;'>
                        <li>✨ High Accuracy Predictions</li>
                        <li>📱 User-Friendly Interface</li>
                        <li>🎯 Actionable Insights</li>
                        <li>📊 Detailed Analysis Reports</li>
                    </ul>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Quick Start Guide
    st.markdown("""
        <div style='margin-top: 3em;'>
            <h2 style='color: #00cc66; margin-bottom: 1em;'>Quick Start Guide</h2>
            <div style='display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;'>
                <div class='feature-card'>
                    <h4 style='color: #00cc66;'>1. Input Data</h4>
                    <p style='color: #cccccc;'>Enter your soil sample parameters in the prediction page.</p>
                </div>
                <div class='feature-card'>
                    <h4 style='color: #00cc66;'>2. Get Prediction</h4>
                    <p style='color: #cccccc;'>Receive instant fertility assessment results.</p>
                </div>
                <div class='feature-card'>
                    <h4 style='color: #00cc66;'>3. View Analysis</h4>
                    <p style='color: #cccccc;'>Explore detailed insights and recommendations.</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


def data_analysis_page():
    st.markdown("<h1 style='text-align: center;'>🌱 Soil Fertility Prediction System</h1>", unsafe_allow_html=True)
    st.markdown("<h2>📈 Data Analysis Dashboard</h2>", unsafe_allow_html=True)

    # Load and prepare data
    try:
        # Import and use sample data
        from src.ENDTOENDDSPROJECT.data.sample_data import get_sample_data
        df = get_sample_data()
        st.success("Successfully loaded sample data")
            
        df.fillna(df.mean(numeric_only=True), inplace=True)
        
        # Display key metrics
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Samples", len(df))
        col2.metric("Avg pH Level", f"{df['pH Level'].mean():.2f}")
        col3.metric("Avg Organic Matter", f"{df['Organic Matter (%)'].mean():.1f}%")
        
        # Calculate fertility distribution
        fertility_counts = df['Fertility Status'].value_counts()
        col4.metric("High Fertility Samples", int(fertility_counts.get(2, 0)))
        
        # Correlation Analysis
        st.markdown("### 📊 Feature Correlations")
        corr_cols = ['pH Level', 'Organic Matter (%)', 'Nitrogen Content (kg/ha)',
                    'Phosphorus Content (kg/ha)', 'Potassium Content (kg/ha)']
        corr = df[corr_cols].corr()
        
        # Create a heatmap using plotly
        import plotly.express as px
        fig = px.imshow(corr,
                       labels=dict(color="Correlation"),
                       x=corr_cols,
                       y=corr_cols,
                       color_continuous_scale='RdBu')
        st.plotly_chart(fig)

        # Soil Parameters Distribution
        st.markdown("### 🌍 Soil Parameters Distribution")
        col1, col2 = st.columns(2)
        
        with col1:
            # pH Level Distribution
            fig_ph = px.histogram(df, x='pH Level', 
                                title='pH Level Distribution',
                                color_discrete_sequence=['#3366cc'])
            fig_ph.update_layout(showlegend=False)
            st.plotly_chart(fig_ph)
            
            # Soil Type Distribution
            soil_type_counts = df['Soil Type'].value_counts()
            fig_soil = px.pie(values=soil_type_counts.values, 
                            names=soil_type_counts.index,
                            title='Soil Type Distribution')
            st.plotly_chart(fig_soil)

        with col2:
            # Organic Matter Distribution
            fig_om = px.histogram(df, x='Organic Matter (%)',
                                title='Organic Matter Distribution',
                                color_discrete_sequence=['#dc3912'])
            fig_om.update_layout(showlegend=False)
            st.plotly_chart(fig_om)
            
            # Fertility Status Distribution
            fertility_map = {0: "Can Be Improved", 1: "Non-Fertile", 2: "Fertile"}
            df['Fertility Label'] = df['Fertility Status'].map(fertility_map)
            fertility_counts = df['Fertility Label'].value_counts()
            fig_fertility = px.pie(values=fertility_counts.values,
                                names=fertility_counts.index,
                                title='Fertility Status Distribution',
                                color_discrete_sequence=px.colors.qualitative.Set3)
            st.plotly_chart(fig_fertility)

        # Nutrient Content Analysis
        st.markdown("""
            <div style='background: rgba(0, 204, 102, 0.05); padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
                <h3 style='color: #00cc66;'>🌱 Nutrient Content Analysis</h3>
                <p style='color: #cccccc;'>Comprehensive analysis of NPK (Nitrogen, Phosphorus, Potassium) levels across different soil types</p>
            </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            # NPK Distribution Violin Plot
            nutrients = ['Nitrogen Content (kg/ha)', 'Phosphorus Content (kg/ha)', 'Potassium Content (kg/ha)']
            npk_data = pd.melt(df[nutrients], var_name='Nutrient', value_name='Content')
            
            fig_violin = go.Figure()
            colors = ['rgba(0, 204, 102, 0.6)', 'rgba(51, 102, 204, 0.6)', 'rgba(255, 153, 51, 0.6)']
            
            for nutrient, color in zip(nutrients, colors):
                fig_violin.add_trace(go.Violin(
                    x=[nutrient.split()[0]] * len(df),  # Just use "Nitrogen", "Phosphorus", "Potassium"
                    y=df[nutrient],
                    name=nutrient.split()[0],
                    box_visible=True,
                    meanline_visible=True,
                    fillcolor=color,
                    line_color='rgba(0,0,0,0)',
                    points='all',
                    pointpos=-0.5,
                    jitter=0.3
                ))

            fig_violin.update_layout(
                title={
                    'text': 'NPK Distribution Overview',
                    'y':0.95,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top',
                    'font': dict(size=16, color='#00cc66')
                },
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#cccccc'),
                xaxis_title="Nutrient Type",
                yaxis_title="Content (kg/ha)",
                showlegend=False,
                height=500
            )
            st.plotly_chart(fig_violin, use_container_width=True)

        with col2:
            # Radar Chart for Average Nutrient Content by Soil Type
            soil_types = df['Soil Type'].unique()
            nutrient_means = df.groupby('Soil Type')[nutrients].mean()

            fig_radar = go.Figure()
            colors = px.colors.qualitative.Set3

            for i, soil in enumerate(soil_types):
                fig_radar.add_trace(go.Scatterpolar(
                    r=nutrient_means.loc[soil],
                    theta=['N', 'P', 'K'],
                    name=soil,
                    fillcolor=colors[i],
                    fill='toself',
                    line=dict(color=colors[i])
                ))

            fig_radar.update_layout(
                title={
                    'text': 'Average NPK by Soil Type',
                    'y':0.95,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top',
                    'font': dict(size=16, color='#00cc66')
                },
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        gridcolor='rgba(255,255,255,0.2)'
                    ),
                    angularaxis=dict(
                        gridcolor='rgba(255,255,255,0.2)'
                    ),
                    bgcolor='rgba(0,0,0,0)'
                ),
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#cccccc'),
                showlegend=True,
                legend=dict(
                    yanchor="top",
                    y=0.9,
                    xanchor="left",
                    x=1.1,
                    font=dict(color='#cccccc')
                ),
                height=500
            )
            st.plotly_chart(fig_radar, use_container_width=True)

        # Add NPK Level Summary Table
        st.markdown("""
            <div style='background: rgba(0, 204, 102, 0.05); padding: 20px; border-radius: 10px; margin-top: 20px;'>
                <h4 style='color: #00cc66;'>Nutrient Levels Summary</h4>
            </div>
        """, unsafe_allow_html=True)

        # Calculate summary statistics
        summary_data = {
            'Metric': ['Average (kg/ha)', 'Minimum (kg/ha)', 'Maximum (kg/ha)', 'Std Dev'],
            'Nitrogen': [
                f"{df['Nitrogen Content (kg/ha)'].mean():.1f}",
                f"{df['Nitrogen Content (kg/ha)'].min():.1f}",
                f"{df['Nitrogen Content (kg/ha)'].max():.1f}",
                f"{df['Nitrogen Content (kg/ha)'].std():.1f}"
            ],
            'Phosphorus': [
                f"{df['Phosphorus Content (kg/ha)'].mean():.1f}",
                f"{df['Phosphorus Content (kg/ha)'].min():.1f}",
                f"{df['Phosphorus Content (kg/ha)'].max():.1f}",
                f"{df['Phosphorus Content (kg/ha)'].std():.1f}"
            ],
            'Potassium': [
                f"{df['Potassium Content (kg/ha)'].mean():.1f}",
                f"{df['Potassium Content (kg/ha)'].min():.1f}",
                f"{df['Potassium Content (kg/ha)'].max():.1f}",
                f"{df['Potassium Content (kg/ha)'].std():.1f}"
            ]
        }
        
        summary_df = pd.DataFrame(summary_data)
        st.dataframe(
            summary_df.style.set_properties(**{
                'background-color': 'rgba(0, 204, 102, 0.05)',
                'color': '#cccccc'
            }),
            hide_index=True,
            use_container_width=True
        )

        # Model Performance
        st.markdown("### 🤖 Model Performance")
        model_data = {
            'Model': ['CatBoost', 'Random Forest', 'XGBoost', 'Decision Tree', 'KNN'],
            'Accuracy': [0.89, 0.85, 0.84, 0.82, 0.78]
        }
        model_df = pd.DataFrame(model_data)
        fig_models = px.bar(model_df, x='Model', y='Accuracy',
                          title='Model Performance Comparison',
                          color_discrete_sequence=['#2ecc71'])
        st.plotly_chart(fig_models)

    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        st.info("Please ensure you have the required data files in the artifacts directory.")


def prediction_page():
    st.markdown("""
        <div style='text-align: center; padding: 1em;'>
            <h1 style='color: #00cc66; margin-bottom: 0.5em;'>🔮 Soil Fertility Prediction</h1>
            <p style='color: #cccccc; font-size: 1.1em;'>Enter your soil parameters below to get instant fertility predictions</p>
        </div>
    """, unsafe_allow_html=True)

    # Input fields matching the preprocessor's expected format
    districts = ['Ahmednagar', 'Pune', 'Nashik', 'Nagpur']
    soil_types = ['Alluvial', 'Red', 'Black', 'Clayey', 'Sandy']
    
    # Create tabs for different input methods
    tab1, tab2 = st.tabs(["📝 Manual Input", "📁 Bulk Upload"])
    
    with tab1:
        st.markdown("""
            <div style='background: rgba(0, 204, 102, 0.05); padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
                <h3 style='color: #00cc66;'>Soil Parameters</h3>
                <p style='color: #cccccc;'>Fill in the details below for your soil sample</p>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            district = st.selectbox('🏢 District', districts,
                help='Select the district where the soil sample was collected')
            
            soil_type = st.selectbox('🌍 Soil Type', soil_types,
                help='Select the type of soil being analyzed')
            
            ph = st.number_input('🧪 pH Level', 
                min_value=0.0, max_value=14.0, value=7.0,
                help='Soil pH level (0-14)')
                
            organic = st.number_input('🍃 Organic Matter (%)', 
                min_value=0.0, max_value=10.0, value=2.5,
                help='Percentage of organic matter in soil')
        
        with col2:
            nitrogen = st.number_input('🌿 Nitrogen Content (kg/ha)', 
                min_value=0.0, value=100.0,
                help='Amount of nitrogen in kilograms per hectare')
                
            phosphorus = st.number_input('💠 Phosphorus Content (kg/ha)', 
                min_value=0.0, value=50.0,
                help='Amount of phosphorus in kilograms per hectare')
                
            potassium = st.number_input('🔷 Potassium Content (kg/ha)', 
                min_value=0.0, value=150.0,
                help='Amount of potassium in kilograms per hectare')
    
    with tab2:
        st.markdown("""
            <div style='background: rgba(0, 204, 102, 0.05); padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
                <h3 style='color: #00cc66;'>Bulk Prediction</h3>
                <p style='color: #cccccc;'>Upload a CSV file with multiple soil samples</p>
            </div>
        """, unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file is not None:
            st.info("File uploaded successfully! You can preview the data below.")
            df_upload = pd.read_csv(uploaded_file)
            st.dataframe(df_upload.head())
    
    # Input summary with custom styling
    with tab1:
        st.markdown("""
            <div style='background: rgba(0, 204, 102, 0.05); padding: 20px; border-radius: 10px; margin-top: 20px;'>
                <h3 style='color: #00cc66;'>Input Summary</h3>
                <div style='display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-top: 15px;'>
                    <div>
                        <h4 style='color: #00cc66; margin-bottom: 10px;'>Location & Soil Type</h4>
                        <p style='color: #cccccc;'><strong>District:</strong> {}</p>
                        <p style='color: #cccccc;'><strong>Soil Type:</strong> {}</p>
                    </div>
                    <div>
                        <h4 style='color: #00cc66; margin-bottom: 10px;'>Basic Properties</h4>
                        <p style='color: #cccccc;'><strong>pH Level:</strong> {:.2f}</p>
                        <p style='color: #cccccc;'><strong>Organic Matter:</strong> {:.1f}%</p>
                    </div>
                </div>
                <div style='margin-top: 20px;'>
                    <h4 style='color: #00cc66; margin-bottom: 10px;'>Nutrient Content</h4>
                    <div style='display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;'>
                        <div>
                            <p style='color: #cccccc;'><strong>Nitrogen:</strong></p>
                            <p style='color: #00cc66;'>{:.1f} kg/ha</p>
                        </div>
                        <div>
                            <p style='color: #cccccc;'><strong>Phosphorus:</strong></p>
                            <p style='color: #00cc66;'>{:.1f} kg/ha</p>
                        </div>
                        <div>
                            <p style='color: #cccccc;'><strong>Potassium:</strong></p>
                            <p style='color: #00cc66;'>{:.1f} kg/ha</p>
                        </div>
                    </div>
                </div>
            </div>
        """.format(district, soil_type, ph, organic, nitrogen, phosphorus, potassium), unsafe_allow_html=True)
    
    # Create DataFrame with proper column names to match the preprocessor
    input_df = pd.DataFrame({
        'District': [district],
        'Soil Type': [soil_type],
        'pH Level': [ph],
        'Organic Matter (%)': [organic],
        'Nitrogen Content (kg/ha)': [nitrogen],
        'Phosphorus Content (kg/ha)': [phosphorus],
        'Potassium Content (kg/ha)': [potassium]
    })
    if st.button('Predict'):
        try:
            pred = predict(input_df)
            st.success(f'Predicted Fertility: {pred[0]}')
            
            # Display additional information about the prediction
            fertility_map = {0: "Low", 1: "Medium", 2: "High"}
            if pred[0] in fertility_map:
                st.markdown(f"""
                ### Detailed Result
                Fertility Level: **{fertility_map[pred[0]]}**
                
                Recommendations:
                - {"Consider adding more nutrients" if pred[0] == 0 else "Maintain current practices" if pred[0] == 1 else "Soil is highly fertile"}
                - {"Focus on improving organic matter content" if organic < 2.0 else "Good organic matter content"}
                - {"Monitor pH levels" if ph < 6.0 or ph > 8.0 else "pH levels are optimal"}
                """)
        except Exception as e:
            st.error(f'Error: {e}')
            st.info("Please make sure all input values are within expected ranges.")


def set_custom_style():
    st.markdown("""
        <style>
        .main {
            background-color: #0e1117;
            color: white;
        }
        .stButton>button {
            background-color: #00cc66;
            color: white;
            border-radius: 10px;
            border: none;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            transition-duration: 0.4s;
        }
        .stButton>button:hover {
            background-color: #00994d;
        }
        div[data-testid="stMetricValue"] {
            font-size: 24px;
            color: #00cc66;
        }
        .stPlotlyChart {
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 10px;
        }
        section[data-testid="stSidebar"] > div {
            background-color: #1a1a1a;
            padding: 2rem 1rem;
        }
        section[data-testid="stSidebar"] .stSelectbox label {
            color: white;
        }
        .styled-metric {
            background-color: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        .info-box {
            background-color: rgba(0, 204, 102, 0.1);
            border-left: 5px solid #00cc66;
            padding: 20px;
            border-radius: 0 10px 10px 0;
            margin: 20px 0;
        }
        .feature-card {
            background: linear-gradient(135deg, rgba(0, 204, 102, 0.1) 0%, rgba(0, 153, 77, 0.1) 100%);
            padding: 20px;
            border-radius: 15px;
            margin: 10px 0;
            border: 1px solid rgba(0, 204, 102, 0.2);
        }
        </style>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title='Soil Fertility Prediction System',
        page_icon='🌱',
        layout='wide',
        initial_sidebar_state='expanded'
    )
    
    set_custom_style()
    
    # Custom sidebar styling
    st.sidebar.markdown("""
        <div style='text-align: center; margin-bottom: 20px;'>
            <h1 style='color: #00cc66;'>🌱</h1>
            <h2 style='color: white;'>Navigation</h2>
        </div>
    """, unsafe_allow_html=True)
    
    page = st.sidebar.selectbox(
        'Choose a page',
        ['Home', 'Data Analysis', 'Prediction'],
        format_func=lambda x: f"{'🏠' if x == 'Home' else '📊' if x == 'Data Analysis' else '🔮'} {x}"
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
        <div style='text-align: center; padding: 20px; background-color: rgba(0, 204, 102, 0.1); border-radius: 10px;'>
            <h4 style='color: #00cc66;'>About</h4>
            <p style='color: white; font-size: 0.9em;'>Advanced ML-powered soil analysis system for precise fertility assessment</p>
        </div>
    """, unsafe_allow_html=True)
    
    if page == 'Home':
        home_page()
    elif page == 'Data Analysis':
        data_analysis_page()
    elif page == 'Prediction':
        prediction_page()

if __name__ == '__main__':
    main()
