#!/bin/bash
PYTHON_VERSION="3.12"
NODE_VERSION="20"

echo "This project uses python $PYTHON_VERSION. Make sure to have the correct version of Python on your environment."

echo ""
echo "======================== DEACTIVATE ENVIRONMENT ========================"
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Virtual environment is already deactivated"
else
    deactivate
    echo "Virtual environment deactivated"
fi

echo ""
echo "======================= REMOVING OLD ENVIRONMENT ======================="
echo ""
echo "rm -rf venv"
rm -rf venv
echo "rm -rf env"
rm -rf env
echo "Old virtual environment removed."

echo ""
echo "======================= CREATING NEW ENVIRONMENT ======================="
echo ""
echo "python$PYTHON_VERSION -m venv venv"
python$PYTHON_VERSION -m venv venv

echo ""
echo "========================= ACTIVATE ENVIRONMENT ========================="
echo ""
echo "source venv/bin/activate"
source venv/bin/activate

echo ""
echo "================================ UPGRADE PIP ============================"
echo ""
echo "python -m pip install -U pip>=21.1"
python -m pip install -U 'pip>=21.1'

echo ""
echo "=========================== INSTALL DEPENDENCIES =========================="
echo ""
echo "pip install -r requirements.txt"
pip install -r requirements.txt

echo ""
echo "=========================== FRONTEND NODE SETUP ================================"
echo "nvm install & use $NODE_VERSION"
nvm install $NODE_VERSION
nvm use $NODE_VERSION

echo ""
echo "=========================== INSTALL FRONTEND DEPENDENCIES ========================"
echo "cd frontend"
cd frontend
echo "npm install & npm install three"
npm install
npm install three

echo ""
echo "========================= VENV SETUP COMPLETE ========================"
echo ""
