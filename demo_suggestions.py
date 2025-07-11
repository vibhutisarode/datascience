#!/usr/bin/env python3
"""
Demo script to show the enhanced soil fertility prediction with suggestions
"""

from src.ENDTOENDDSPROJECT.pipelines.prediction_pipeline import CustomData, PredictPipeline
from application import get_suggestions

def demo_enhanced_prediction():
    """Demo the enhanced prediction with suggestions"""
    
    # Test cases with different fertility levels
    test_cases = [
        {
            "name": "Low Fertility Soil",
            "data": CustomData(
                district="Jodhpur",
                soil_type="Sandy",
                ph_level=5.5,  # Acidic
                organic_matter=0.8,  # Low organic matter
                nitrogen_content=15.0,  # Low nitrogen
                phosphorus_content=8.0,  # Low phosphorus
                potassium_content=20.0   # Low potassium
            )
        },
        {
            "name": "Medium Fertility Soil",
            "data": CustomData(
                district="Jaipur",
                soil_type="Clay",
                ph_level=7.2,
                organic_matter=2.0,
                nitrogen_content=30.0,
                phosphorus_content=18.0,
                potassium_content=38.0
            )
        },
        {
            "name": "High Fertility Soil",
            "data": CustomData(
                district="Udaipur",
                soil_type="Loamy",
                ph_level=6.8,
                organic_matter=3.5,
                nitrogen_content=45.0,
                phosphorus_content=25.0,
                potassium_content=50.0
            )
        }
    ]
    
    predict_pipeline = PredictPipeline()
    fertility_mapping = {0: "Low Fertility", 1: "Medium Fertility", 2: "High Fertility"}
    
    print("🌱 SOIL FERTILITY PREDICTION DEMO WITH SUGGESTIONS")
    print("=" * 60)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{i}. {test_case['name']}:")
        print("-" * 40)
        
        # Get prediction
        pred_df = test_case['data'].get_data_as_data_frame()
        results = predict_pipeline.predict(pred_df)
        fertility_status = fertility_mapping.get(results[0], "Unknown")
        
        # Get suggestions
        suggestions = get_suggestions(results[0], test_case['data'])
        
        print(f"🎯 PREDICTION: {fertility_status}")
        print(f"🤖 MODEL: Decision Tree Classifier (95%+ accuracy)")
        
        print(f"\n💡 RECOMMENDATIONS:")
        for rec in suggestions['recommendations']:
            print(f"   • {rec}")
        
        print(f"\n🚀 ACTION ITEMS:")
        for action in suggestions['actions']:
            print(f"   • {action}")
        
        if suggestions['warnings']:
            print(f"\n⚠️  WARNINGS:")
            for warning in suggestions['warnings']:
                print(f"   • {warning}")
        
        print(f"\n📊 INPUT SUMMARY:")
        print(f"   District: {test_case['data'].district}")
        print(f"   Soil Type: {test_case['data'].soil_type}")
        print(f"   pH: {test_case['data'].ph_level}")
        print(f"   Organic Matter: {test_case['data'].organic_matter}%")
        print(f"   N-P-K: {test_case['data'].nitrogen_content}-{test_case['data'].phosphorus_content}-{test_case['data'].potassium_content} kg/ha")

if __name__ == "__main__":
    try:
        demo_enhanced_prediction()
        print(f"\n✅ Demo completed successfully!")
        print(f"\n🌐 Start the web app with: python application.py")
        print(f"   Then visit: http://localhost:5000")
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")
