## Managing ML-lifecycle with MLflow


### Installation 

0. Clone this repository using git or download using Github interface

1. Install miniconda distribution for python 3.7 -> [link](https://docs.conda.io/en/latest/miniconda.html#installing) 

2. Open Anaconda Prompt (Miniconda 3) navigate **to the tutorial folder** and install requirements: 
    
    - **Optional**: you can create separate conda environment for this tutorial from environment file: 
        ```
        conda env create -f conda.yaml
        ```
        ```
        conda activate mlflow-tutorial
        ```
    - Installing requirements from requirements.txt file:
        ```
        pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html
        ```
3. Launch Jupyter Lab from **from the tutorial directory**:
    ```
    jupyter lab
    ```
    
4. Launch MLflow server:
    ```
    mlflow server --backend-store-uri="sqlite:///C:\\path\\to\\project_folder\\backend\\mlflow_data.db" 
                  --default-artifact-root="file:///C:\\path\\to\\project_folder\\artifact_store\\"
    ```
    - Parameters:
        - backend-store-uri - URI to which to persist experiment and run data (sqlite database in our case).
        - default-artifact-root - Local or S3 URI to store artifacts, for new experiments (local folder in our case). 
    
    - **Hint**: you can launch MLflow server also from terminal inside Jupyter Lab interface. 
    
5. Make sure that you can access mlflow server and jupyter notebook from your browser :
    - mlflow server   : http://localhost:5000/
    - jupyter notebook: http://localhost:8888/ 

**Note**: There could be some minor changes in the dependencies and files, thus make sure to double-check prior to the event.
**Note**: Tutorial functionality was tested on Windows 10.
    
### Congrats! You are ready good to go! 