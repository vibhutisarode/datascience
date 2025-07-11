#!/usr/bin/env python3
"""
Test script for soil fertility prediction
"""

from src.ENDTOENDDSPROJECT.pipelines.prediction_pipeline import CustomData, PredictPipeline

def test_prediction():
    """Test the prediction pipeline with sample data"""
    try:
        # Sample data for testing
        data = CustomData(
            district="Jaipur",
            soil_type="Clay",
            ph_level=7.5,
            organic_matter=2.0,
            nitrogen_content=30.0,
            phosphorus_content=20.0,
            potassium_content=40.0
        )
        
        # Convert to DataFrame
        pred_df = data.get_data_as_data_frame()
        print("Input data:")
        print(pred_df)
        
        # Make prediction
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        
        # Map results
        fertility_mapping = {0: "Low Fertility", 1: "Medium Fertility", 2: "High Fertility"}
        fertility_status = fertility_mapping.get(results[0], "Unknown")
        
        print(f"\nPrediction Result: {fertility_status}")
        print(f"Raw prediction value: {results[0]}")
        
        return True
        
    except Exception as e:
        print(f"Error during prediction: {e}")
        return False

if __name__ == "__main__":
    print("Testing Soil Fertility Prediction Pipeline...")
    success = test_prediction()
    if success:
        print("\n✅ Test completed successfully!")
    else:
        print("\n❌ Test failed!")
