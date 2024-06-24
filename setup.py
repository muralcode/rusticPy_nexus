#Data Ingestion: http://localhost:5000
#Processing Core: http://localhost:5001
#Visualization: http://localhost:5002
#AI Model Creation: http://localhost:5003

#build and start services
#docker-compose up --build


# process data
# curl -X POST http://localhost:5001/process -d '{"data": [1, 2, 3, 4]}'

#train model
# curl -X POST http://localhost:5003/train -d '{"data": [1, 2, 3, 4], "target": [0, 1, 0, 1]}'
from setuptools import setup, find_packages

setup(
    name="rusticPy_nexus",
    version="0.1.0",
    packages=find_packages(where="services"),
    package_dir={"": "services"},
    install_requires=[
        "Flask==2.0.1",
        "requests==2.26.0",
        "scikit-learn==0.24.2",
        "gunicorn==20.1.0",
        "numpy==1.20.3",
    ],
)
