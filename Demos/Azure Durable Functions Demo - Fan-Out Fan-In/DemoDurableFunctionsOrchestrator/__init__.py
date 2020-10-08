# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):

    #code snippet refactored from https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview?tabs=python#fan-in-out

    # Get a list of N work items to process in parallel.
    work_batch = yield context.call_activity("WorkBatchActvity", None)

    parallel_tasks = [ context.call_activity("ProcessorActivity", b) for b in work_batch ]
    
    outputs = yield context.task_all(parallel_tasks)

    # Aggregate all N outputs and send the result to DetermineEvenNumberActvity.
    total = sum(outputs)
    even_number_result = yield context.call_activity("DetermineEvenNumberActvity", total)

    return even_number_result
    

main = df.Orchestrator.create(orchestrator_function)