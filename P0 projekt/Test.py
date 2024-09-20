import importlib

# List of packages to check
packages = [
    'sklearn',        # scikit-learn
    'cv2',            # opencv-python
    'pandas',         
    'numpy', 
    'matplotlib', 
    'seaborn'
]

# Function to check if a package is installed
def check_package(package):
    try:
        importlib.import_module(package)
        return True
    except ImportError:
        return False

# Checking each package
for package in packages:
    if check_package(package):
        print(f"{package} is installed.")
    else:
        print(f"{package} is NOT installed.")
