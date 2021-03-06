# Azure Durable Functions Demo - Async HTTP APIs

This is a demo of an HTTP trigger based Azure Durable Function, written in Python. This function app contains three functions and demonstrates a pattern for creating <a href="https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview?tabs=csharp#async-http">Async HTTP APIs</a>. An HTTP trigger based orchestration client function, an orchestrator function, and an activity function.

</br>
To run this demo locally, please use the following steps:
<ol> 
<li>Create a virtual environment in this folder named .venv
<li>Activate this virtual environment or, if using VS Code to run this demo, <a href="https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment">set the Python interpretor</a> to the interpretor created in this virtual environment
<li>Run pip install to ensure all dependencies from requirements.txt are installed
<li>Start the functions run time. This can either be done from the command line using the Azure Functions Core Tools, command <b>func host start</b>, or, if using VS Code to run this demo, by <a href="https://code.visualstudio.com/docs/editor/debugging">starting the debugger</a> using the <b>Attach to Python Functions</b> launch configuration
</ol>