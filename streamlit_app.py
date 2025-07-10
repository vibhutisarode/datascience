import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os
import sys

# Add the project root to Python path to ensure imports work correctly
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

# Define paths relative to the project root
MODEL_PATH = os.path.join(ROOT_DIR, 'artifacts', 'model.pkl')
PREPROCESSOR_PATH = os.path.join(ROOT_DIR, 'artifacts', 'preprocessor.pkl')

# Utility functions
def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

def predict(features):
    try:
        # Load model and preprocessor
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
        if not os.path.exists(PREPROCESSOR_PATH):
            raise FileNotFoundError(f"Preprocessor file not found at {PREPROCESSOR_PATH}")
        
        model = load_pickle(MODEL_PATH)
        preprocessor = load_pickle(PREPROCESSOR_PATH)
        
        # Process features and get prediction
        features_processed = preprocessor.transform(features)
        prediction = model.predict(features_processed)
        
        return prediction
    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")
        st.info("Please ensure all model artifacts are properly set up in the artifacts directory.")
        raise e

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
    st.markdown("""
        <div style='text-align: center; padding: 1em;'>
            <h1 style='color: #00cc66; margin-bottom: 0.5em;'>📊 Soil Analysis Dashboard</h1>
            <p style='color: #cccccc; font-size: 1.1em;'>Comprehensive analysis of soil samples and fertility patterns</p>
        </div>
    """, unsafe_allow_html=True)

    # Load and prepare data
    try:
        csv_path = os.path.join(ROOT_DIR, 'artifacts', 'raw.csv')
        if not os.path.exists(csv_path):
            st.warning("Analysis data file not found. Some visualizations may not be available.")
            return
            
        df = pd.read_csv(csv_path)
        df.fillna(df.mean(numeric_only=True), inplace=True)
        
        # Display key metrics with custom styling
        st.markdown("""
            <div style='background: rgba(0, 204, 102, 0.05); padding: 20px; border-radius: 15px; margin-bottom: 30px;'>
                <h3 style='color: #00cc66; margin-bottom: 20px; text-align: center;'>Key Metrics Overview</h3>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        # Custom metric display
        total_samples = len(df)
        avg_ph = df['pH Level'].mean()
        avg_organic = df['Organic Matter (%)'].mean()
        fertility_counts = df['Fertility Status'].value_counts()
        high_fertility = int(fertility_counts.get(2, 0))
        
        metrics_data = [
            {"title": "Total Samples", "value": f"{total_samples:,}", "icon": "📊", "delta": f"{total_samples/1000:.1f}k samples"},
            {"title": "Average pH", "value": f"{avg_ph:.2f}", "icon": "🧪", "delta": "Neutral" if 6.5 <= avg_ph <= 7.5 else "Acidic" if avg_ph < 6.5 else "Alkaline"},
            {"title": "Organic Matter", "value": f"{avg_organic:.1f}%", "icon": "🍃", "delta": "Good" if avg_organic > 2 else "Needs Improvement"},
            {"title": "High Fertility", "value": f"{high_fertility:,}", "icon": "⭐", "delta": f"{(high_fertility/total_samples)*100:.1f}% of total"}
        ]
        
        cols = [col1, col2, col3, col4]
        for col, metric in zip(cols, metrics_data):
            col.markdown(f"""
                <div style='background: rgba(0, 204, 102, 0.1); padding: 15px; border-radius: 10px; text-align: center;'>
                    <div style='font-size: 24px; margin-bottom: 5px;'>{metric['icon']}</div>
                    <div style='color: #cccccc; font-size: 0.9em;'>{metric['title']}</div>
                    <div style='color: #00cc66; font-size: 1.8em; font-weight: bold; margin: 10px 0;'>{metric['value']}</div>
                    <div style='color: #888888; font-size: 0.8em;'>{metric['delta']}</div>
                </div>
            """, unsafe_allow_html=True)
        
        # Correlation Analysis
        st.markdown("""
            <div style='background: rgba(0, 204, 102, 0.05); padding: 20px; border-radius: 15px; margin: 30px 0;'>
                <h3 style='color: #00cc66; margin-bottom: 20px;'>� Parameter Correlations</h3>
                <p style='color: #cccccc;'>Discover relationships between different soil parameters</p>
            </div>
        """, unsafe_allow_html=True)
        
        corr_cols = ['pH Level', 'Organic Matter (%)', 'Nitrogen Content (kg/ha)',
                    'Phosphorus Content (kg/ha)', 'Potassium Content (kg/ha)']
        corr = df[corr_cols].corr()
        
        # Create an enhanced heatmap using plotly
        import plotly.express as px
        import plotly.graph_objects as go
        
        fig = go.Figure(data=go.Heatmap(
            z=corr,
            x=corr_cols,
            y=corr_cols,
            colorscale='RdBu',
            zmin=-1, zmax=1,
            text=np.round(corr, 2),
            texttemplate='%{text}',
            textfont={"size": 10},
            hoverongaps=False))
        
        fig.update_layout(
            title={
                'text': 'Soil Parameter Correlations',
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'font': dict(size=20, color='#00cc66')
            },
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#cccccc'),
            height=600
        )
        st.plotly_chart(fig, use_container_width=True)

        # Soil Parameters Distribution
        st.markdown("""
            <div style='background: rgba(0, 204, 102, 0.05); padding: 20px; border-radius: 15px; margin: 30px 0;'>
                <h3 style='color: #00cc66; margin-bottom: 20px;'>📊 Parameter Distributions</h3>
                <p style='color: #cccccc;'>Analysis of key soil parameters across different samples</p>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Enhanced pH Level Distribution
            fig_ph = go.Figure()
            fig_ph.add_trace(go.Histogram(
                x=df['pH Level'],
                nbinsx=30,
                marker_color='rgba(0, 204, 102, 0.6)',
                name='pH Distribution'
            ))
            fig_ph.add_vline(x=7, line_dash="dash", line_color="#cccccc",
                           annotation_text="Neutral pH (7.0)", 
                           annotation_font_color="#cccccc")
            
            fig_ph.update_layout(
                title={
                    'text': 'pH Level Distribution',
                    'y':0.95,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top',
                    'font': dict(size=16, color='#00cc66')
                },
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#cccccc'),
                xaxis_title="pH Level",
                yaxis_title="Number of Samples",
                hoverlabel=dict(bgcolor='#1a1a1a'),
                bargap=0.1
            )
            st.plotly_chart(fig_ph, use_container_width=True)
            
            # Enhanced Soil Type Distribution
            soil_type_counts = df['Soil Type'].value_counts()
            colors = px.colors.qualitative.Set3
            fig_soil = go.Figure(data=[go.Pie(
                labels=soil_type_counts.index,
                values=soil_type_counts.values,
                hole=.3,
                marker=dict(colors=colors),
                textinfo='label+percent',
                hovertemplate="<b>%{label}</b><br>" +
                            "Samples: %{value}<br>" +
                            "Percentage: %{percent}<extra></extra>"
            )])
            
            fig_soil.update_layout(
                title={
                    'text': 'Soil Type Distribution',
                    'y':0.95,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top',
                    'font': dict(size=16, color='#00cc66')
                },
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#cccccc'),
                showlegend=False
            )
            st.plotly_chart(fig_soil, use_container_width=True)

        with col2:
            # Enhanced Organic Matter Distribution
            fig_om = go.Figure()
            fig_om.add_trace(go.Histogram(
                x=df['Organic Matter (%)'],
                nbinsx=30,
                marker_color='rgba(220, 57, 18, 0.6)',
                name='Organic Matter'
            ))
            
            # Add reference line for good organic matter content
            fig_om.add_vline(x=2, line_dash="dash", line_color="#cccccc",
                           annotation_text="Target Level (2%)", 
                           annotation_font_color="#cccccc")
            
            fig_om.update_layout(
                title={
                    'text': 'Organic Matter Distribution',
                    'y':0.95,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top',
                    'font': dict(size=16, color='#00cc66')
                },
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#cccccc'),
                xaxis_title="Organic Matter (%)",
                yaxis_title="Number of Samples",
                hoverlabel=dict(bgcolor='#1a1a1a'),
                bargap=0.1
            )
            st.plotly_chart(fig_om, use_container_width=True)
            
            # Enhanced Fertility Status Distribution
            fertility_map = {0: "Can Be Improved", 1: "Non-Fertile", 2: "Fertile"}
            df['Fertility Label'] = df['Fertility Status'].map(fertility_map)
            fertility_counts = df['Fertility Label'].value_counts()
            
            custom_colors = ['#FFA07A', '#FA8072', '#90EE90']  # Light colors for each category
            fig_fertility = go.Figure(data=[go.Pie(
                labels=fertility_counts.index,
                values=fertility_counts.values,
                hole=.3,
                marker=dict(colors=custom_colors),
                textinfo='label+percent',
                hovertemplate="<b>%{label}</b><br>" +
                            "Samples: %{value}<br>" +
                            "Percentage: %{percent}<extra></extra>"
            )])
            
            fig_fertility.update_layout(
                title={
                    'text': 'Fertility Status Distribution',
                    'y':0.95,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top',
                    'font': dict(size=16, color='#00cc66')
                },
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#cccccc'),
                showlegend=False
            )
            st.plotly_chart(fig_fertility, use_container_width=True)

        # Nutrient Content Analysis
        st.markdown("### 🌱 Nutrient Content Analysis")
        nutrients = ['Nitrogen Content (kg/ha)', 'Phosphorus Content (kg/ha)', 'Potassium Content (kg/ha)']
        
        # Create box plots for nutrients by soil type
        fig_nutrients = px.box(df, x='Soil Type', y=nutrients,
                             title='Nutrient Distribution by Soil Type',
                             points="all")
        st.plotly_chart(fig_nutrients)

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
    
    # Input summary with custom styling
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
