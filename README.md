## Managing ML lifecycle with MLflow


### Installation 

0. Clone current tutorial repository

1. Install miniconda distribution for python 3.7 -> [link](https://docs.conda.io/en/latest/miniconda.html#installing) 

2. Open Anaconda Prompt (Miniconda 3) navigate **to the tutorial folder** and install requirements: 

    ```
    pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html
    ```

3. In two separate terminals launch mlflow server and jupyter lab server **from the tutorial directory**:
    - Mlflow server:
    
    ```
    mlflow server --backend-store-uri="sqlite:///C:\\path\\to\\project_folder\\backend\\mlflow_data.db"  --default-artifact-root="file:///C:\\artifact_store\\"
    ```

    - Jupyter Lab:  
    ```
    jupyter lab
    ```

4. Make sure that you can access mlflow server and jupyter notebook from your browser :
    - mlflow server   : http://localhost:5000/
    - jupyter notebook: http://localhost:8888/ 

5. Congrats! You are ready good to go! 

**Note**: There could be some minor changes in the dependecies, thus make sure to double check prior to event.  

