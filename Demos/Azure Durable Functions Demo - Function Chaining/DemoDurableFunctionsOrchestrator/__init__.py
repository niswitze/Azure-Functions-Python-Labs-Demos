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

    input = context.get_input()
    activity_one_result = yield context.call_activity('DemoHelloActivity1', input.get('name'))

    activity_two_result = yield context.call_activity("DemoHelloActivity2", activity_one_result)

    activity_three_result = yield context.call_activity("DemoHelloActivity3", activity_two_result)

    return activity_three_result

main = df.Orchestrator.create(orchestrator_function)