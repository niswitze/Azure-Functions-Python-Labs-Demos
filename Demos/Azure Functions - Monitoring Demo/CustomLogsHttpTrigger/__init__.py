import logging

import azure.functions as func

#ensure the package opencensus-ext-azure has been added to the requirements.txt file for this function app
from opencensus.ext.azure.log_exporter import AzureLogHandler

logger = logging.getLogger(__name__)

logger.addHandler(AzureLogHandler())


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        logger.warning(f"Hello, {name}. This HTTP triggered function executed successfully and this log is coming directly from code.")
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        logger.warning("This HTTP triggered function executed successfully and this log is coming directly from code. Pass a name in the query string or in the request body for a personalized response.")
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
