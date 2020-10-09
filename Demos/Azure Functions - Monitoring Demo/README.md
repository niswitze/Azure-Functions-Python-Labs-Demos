# Azure Functions - Monitoring Demo

This is a demo of an HTTP trigger based Azure Function, written in Python. This function app contains one HTTP trigger based function and demonstrates how to integrate <a href="https://docs.microsoft.com/en-us/azure/azure-monitor/app/opencensus-python">application insights in code</a> using the opencensus-ext-azure package.

</br>
To run this demo locally, please use the following steps:
<ol> 
<li>Create a virtual environment in this folder named .venv
<li>Activate this virtual environment or, if using VS Code to run this demo, <a href="https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment">set the Python interpretor</a> to the interpretor created in this virtual environment
<li>Run pip install to ensure all dependencies from requirements.txt are installed
<li>Start the functions run time. This can either be done from the command line using the Azure Functions Core Tools, command <b>func host start</b>, or, if using VS Code to run this demo, by <a href="https://code.visualstudio.com/docs/editor/debugging">starting the debugger</a> using the <b>Attach to Python Functions</b> launch configuration
</ol>