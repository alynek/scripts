import os
import subprocess
import sys

def main():
    path = sys.arg[1] 
    validate_path(path)

    requirements = os.path.join(path, 'requirements.txt')
    create_environment(path)
    install_packages(path, requirements)

def validate_path(path):
    if not os.path.exists(path):
        print("The directory does not exist!")
        return

def create_environment(path):
    venv_path = os.path.join(path, 'venv')

    if os.path.exists(venv_path):
        print(f"The virtual environment already exists")
        return
    
    try:
        subprocess.run(['virtualenv', venv_path], check=True)
        print("Environment sucessfully created")
        
    except subprocess.CalledProcessorError as e:
        print(f"Error trying to create environment, error: {e}") 

def install_packages(path, requirements):
    validate_path(requirements)

    subprocess.run(['pip install', requirements], check=True)