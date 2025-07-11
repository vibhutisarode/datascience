import pandas as pd

def get_sample_data():
    # Sample data dictionary with typical soil parameters
    data = {
        'District': ['Ahmednagar', 'Pune', 'Nashik', 'Nagpur'] * 250,  # 1000 samples
        'Soil Type': ['Alluvial', 'Red', 'Black', 'Clayey', 'Sandy'] * 200,
        'pH Level': [7.5 + pd.np.random.normal(0, 0.5) for _ in range(1000)],
        'Organic Matter (%)': [2.0 + pd.np.random.normal(0, 0.3) for _ in range(1000)],
        'Nitrogen Content (kg/ha)': [100 + pd.np.random.normal(0, 20) for _ in range(1000)],
        'Phosphorus Content (kg/ha)': [50 + pd.np.random.normal(0, 10) for _ in range(1000)],
        'Potassium Content (kg/ha)': [150 + pd.np.random.normal(0, 30) for _ in range(1000)],
        'Fertility Status': [pd.np.random.choice([0, 1, 2], p=[0.3, 0.4, 0.3]) for _ in range(1000)]
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Ensure values are within realistic ranges
    df['pH Level'] = df['pH Level'].clip(6.0, 9.0)
    df['Organic Matter (%)'] = df['Organic Matter (%)'].clip(0.5, 5.0)
    df['Nitrogen Content (kg/ha)'] = df['Nitrogen Content (kg/ha)'].clip(50, 200)
    df['Phosphorus Content (kg/ha)'] = df['Phosphorus Content (kg/ha)'].clip(20, 100)
    df['Potassium Content (kg/ha)'] = df['Potassium Content (kg/ha)'].clip(50, 300)
    
    return df
