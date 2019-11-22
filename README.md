## Managing ML lifecycle with MLflow


### Installation 

1. Install miniconda distribution for python 3.7 -> [link](https://docs.conda.io/en/latest/miniconda.html#installing) 

2. Open Anaconda Prompt (Miniconda 3) and create a working environment for the tutorial: 

```
conda env create -f conda_env.yaml 
```

3. Activate mlflow-tutorial environment (in two separate terminals):

```
conda activate mlflow-tutorial 
```

4. Launch mlflow web-server (in the first terminal) from your project folder :

    ```
    mlflow ui
    ```

Note: for mlflow production-ready tracking server you need to create sqlite database which will be used as backend-store:
    
    - Start python in your shell and create sqlite database inside your project directory: 

    ```
    import sqlite3
    connection = sqlite3.connect('mlflow_data.db')
    connection.close()
    ```

    - Start server 

    ```
    mlflow server  --backend-store-uri="sqlite:///C:\\mlflow_data.db"  --default-artifact-root="file:///C:\\artifact_store\\"
    ```

5. Launch jupyter notebook (in the second terminal) from your project folder :

```
jupyter notebook 
```

6. Now you can access mlflow server and jupyter notebook from your browser :
    - mlflow server   : http://localhost:5000/
    - jupyter notebook: http://localhost:8888/ 

7. Congrats! You are ready good to go! 


### 