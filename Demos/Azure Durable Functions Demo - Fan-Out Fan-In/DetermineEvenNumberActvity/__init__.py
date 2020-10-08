# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging

def main(total: int) -> str:

    even_number_result = total % 2 

    return "Total is an even number" if even_number_result == 0 else "Total is an NOT even number"

