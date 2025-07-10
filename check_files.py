import os
from pathlib import Path

def check_required_files():
    """Check if all required files are present"""
    base_dir = Path(__file__).parent.absolute()
    required_files = [
        os.path.join('artifacts', 'model.pkl'),
        os.path.join('artifacts', 'preprocessor.pkl'),
        os.path.join('artifacts', 'raw.csv')
    ]
    
    missing_files = []
    for file_path in required_files:
        full_path = os.path.join(base_dir, file_path)
        if not os.path.exists(full_path):
            missing_files.append(file_path)
    
    if missing_files:
        print("Missing required files:")
        for file_path in missing_files:
            print(f"- {file_path}")
        return False
    return True

if __name__ == "__main__":
    check_required_files()
