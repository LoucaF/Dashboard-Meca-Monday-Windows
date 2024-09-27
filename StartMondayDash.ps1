# Check if python is installed on the windows machine
# Python 3.12 is fine
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed. Please install Python and try again."
    exit
}

# Update the project 
git pull origin master

# Check if the venv already exist and if not, create it
$venvPath = "venv"
if(-not (Test-Path $venvPath)) {
    # Create a virtual environment
    python -m venv venv
    Write-Host "Virtual environment created."
}

# Activate the virtual environment
. .\venv\Scripts\Activate.ps1

# Install the dependencies
pip install -r requirements.txt
Write-Host "Dependencies installed"

$env:PLAYWRIGHT_BROWSERS_PATH="0"
playwright install chromium

# To just run it
python .\main.py

Read-Host -Prompt "Press Enter to exit"

