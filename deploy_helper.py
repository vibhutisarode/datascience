#!/usr/bin/env python3
"""
Deployment Helper Script
Automates the deployment process for the Soil Fertility Prediction App
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - Success!")
        if result.stdout:
            print(f"Output: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Failed!")
        print(f"Error: {e.stderr}")
        return False

def check_git_status():
    """Check if there are uncommitted changes"""
    try:
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True, check=True)
        return len(result.stdout.strip()) == 0
    except:
        return False

def deploy_to_git():
    """Deploy changes to GitHub"""
    print("📤 Deploying to GitHub...")
    
    # Check if git is initialized
    if not os.path.exists('.git'):
        print("❌ Git repository not found. Please initialize git first.")
        return False
    
    # Check for uncommitted changes
    if not check_git_status():
        print("📝 Found uncommitted changes. Committing...")
        
        # Add all files
        if not run_command('git add .', 'Adding files to git'):
            return False
        
        # Commit changes
        commit_message = "feat: Complete soil fertility prediction app with deployment config"
        if not run_command(f'git commit -m "{commit_message}"', 'Committing changes'):
            return False
    else:
        print("✅ No uncommitted changes found.")
    
    # Push to GitHub
    if not run_command('git push origin main', 'Pushing to GitHub'):
        return False
    
    return True

def test_local_deployment():
    """Test the application locally"""
    print("\n🧪 Testing Local Deployment...")
    
    # Check if all required files exist
    required_files = [
        'application.py',
        'requirements.txt',
        'templates/index.html',
        'templates/home.html',
        'artifacts/model.pkl',
        'artifacts/preprocessor.pkl'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        return False
    
    print("✅ All required files present")
    
    # Test imports
    try:
        import flask
        from src.ENDTOENDDSPROJECT.pipelines.prediction_pipeline import CustomData, PredictPipeline
        print("✅ All imports successful")
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    
    print("✅ Local deployment test passed!")
    return True

def create_deployment_summary():
    """Create a deployment summary"""
    summary = """
🎉 DEPLOYMENT READY!

Your Soil Fertility Prediction App is ready for deployment:

📁 Files Created:
  ✅ Procfile (Heroku)
  ✅ runtime.txt (Heroku Python version)
  ✅ Dockerfile (Docker deployment)
  ✅ build.sh (Render.com)
  ✅ DEPLOYMENT.md (Complete guide)

🚀 Recommended Deployment Platforms:
  1. Render.com (Free, Easy) - RECOMMENDED
  2. Heroku (Popular, Paid)
  3. Railway (Modern)
  4. Docker + Any Cloud

📤 GitHub Status:
  ✅ All changes committed and pushed

🌐 Next Steps:
  1. Go to render.com and sign up
  2. Connect your GitHub repository
  3. Create a Web Service
  4. Set start command: python application.py
  5. Deploy!

📧 Share with Professor:
  - Live app URL (after deployment)
  - GitHub repo: https://github.com/vibhutisarode/datascience
  - Project documentation in README.md

🎯 Your app will showcase:
  ✅ Complete ML pipeline
  ✅ Professional web interface
  ✅ AI-powered predictions with suggestions
  ✅ Model transparency and performance metrics
  ✅ Production-ready deployment

GOOD LUCK! 🌟
"""
    return summary

def main():
    """Main deployment workflow"""
    print("🚀 SOIL FERTILITY PREDICTION APP - DEPLOYMENT HELPER")
    print("=" * 60)
    
    # Test local deployment
    if not test_local_deployment():
        print("\n❌ Local deployment test failed. Please fix issues before deploying.")
        return
    
    # Deploy to GitHub
    if not deploy_to_git():
        print("\n❌ GitHub deployment failed. Please check git configuration.")
        return
    
    # Show deployment summary
    print(create_deployment_summary())
    
    # Ask user what they want to do next
    print("\n🤔 What would you like to do next?")
    print("1. View deployment guide (DEPLOYMENT.md)")
    print("2. Test app locally (python application.py)")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        print("\n📖 Opening deployment guide...")
        if os.path.exists('DEPLOYMENT.md'):
            print("Please open DEPLOYMENT.md file for detailed deployment instructions.")
        else:
            print("Deployment guide not found.")
    
    elif choice == "2":
        print("\n🧪 Starting local test...")
        print("Run: python application.py")
        print("Then visit: http://localhost:5000")
    
    elif choice == "3":
        print("\n👋 Good luck with your deployment!")
    
    else:
        print("\n❓ Invalid choice. Please run the script again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Deployment helper stopped by user.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please check the error and try again.")
