# Python Learn - Programming Practices

This repository contains Python practice scripts focused on logical development and calculation tools.

## Steps to Activate the Virtual Environment and Run the Project

Follow these steps every time you open a new terminal in VS Code inside this project folder:

1. Allow script execution in the current PowerShell session:
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

2. Activate the virtual environment:
   .\.venv\Scripts\Activate.ps1

3. Verify the activation:
   Make sure (.venv) appears at the beginning of your terminal command line.

4. Run the calculator script:
   python practices/example.py

## Steps for Library Installation

If you need to reinstall or add new tools to the virtual environment, run the following commands with the environment already active:

1. Ensure pip is updated inside the virtual environment:
   python -m pip install --upgrade pip

2. Install the SymPy library for derivative calculation:
   pip install sympy

## Installed Libraries
- SymPy: Used for processing and analytical calculation of symbolic derivatives.
