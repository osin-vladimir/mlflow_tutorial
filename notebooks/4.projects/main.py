import click
import os

import mlflow
from mlflow.utils import mlflow_tags
from mlflow.entities import RunStatus
from mlflow.utils.logging_utils import eprint

@click.command()
@click.option("--param_one", default=10, type=int)
@click.option("--param_two", default=20, type=int)
@click.option("--param_three", default=100000, type=int)
def main(param_one, param_two, param_three):
  print("PyCon - MLFlow Projects")
  print("Parameters {}, {}, {} ".format(param_one, param_two, param_three))
  


if __name__== "__main__":
  main()