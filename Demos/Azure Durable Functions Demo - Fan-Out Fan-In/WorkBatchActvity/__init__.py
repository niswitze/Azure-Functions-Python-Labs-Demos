# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import numpy as np

def main(binding=None) -> list:

    random_numbers_list = np.random.randint(1,26,10).tolist()
    return random_numbers_list

