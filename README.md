# Azure Functions - Labs & Demos

This repository contains examples of Azure Functions and Durable Functions written in Python. These demos and labs are all based off Microsoft's public Azure documentation on <a href="https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python">Azure Functions</a>, <a href="https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview?tabs=python">Durable Functions</a>, and <a href="https://docs.microsoft.com/en-us/azure/developer/python/">Azure Python Development</a>.


If there are any problems found with these examples or requests for specific examples to be added, please raise an issue in this repository describing your problem or request.


</br>

# Prerequisites 

Please use the below steps to configure your machine for running & debugging Python based Azure Functions locally in Visual Studio Code:

<ol>
    <li>Install the initial set of prerequisites found <a href="https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-vs-code?pivots=programming-language-python#configure-your-environment">here</a>
    <ul>
        <li><b>NOTE</b> - An active Azure subscription is not needed for running these demos and labs locally
    </ul>
    <li>Download and install the <a href="https://docs.microsoft.com/en-us/azure/storage/common/storage-use-emulator">Azure Storage Emulator</a>
        <ul>
        <li><b>NOTE</b> - The Azure Storage Emulator is currently being replaced by <a href="https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azurite">Azurite</a>, which will be the future solution for emulating Azure Storage locally. However, it does not currently support some major features of Azure Storage which is why the Azure Storage Emulator is the recommended solution for the demos and labs in this repository for now
        </ul>
    <li>Download and install <a href="https://docs.microsoft.com/en-us/azure/vs-azure-tools-storage-manage-with-storage-explorer?tabs=windows#download-and-install">Azure Storage Explorer</a>
    <li> <a href="https://docs.microsoft.com/en-us/azure/storage/common/storage-use-emulator#start-and-initialize-the-storage-emulator">Start and initialize</a> the Azure Storage Emulator
        <ul>
            <li>If the Azure Storage Emulator has not already been initiliazed on install, please search for the executable <b>AzureStorageEmulator.exe</b> and execute the commands <b>AzureStorageEmulator.exe init</b> and <b>AzureStorageEmulator.exe start</b> in the directory where this executable exists
            <li><b>NOTE</b> - For windows users, this directory should be something similar to <b>C:\Program Files (x86)\Microsoft SDKs\Azure\Storage Emulator</b>
        </ul>
    <li>Ensure Azure Storage Explorer can connect to the Local & Attached Storage Account named <b>Emulator</b>
    </br>
    </br>
        <img src=".\Assets\StorageExplorerLocalEmulator.PNG">
    </ol>
</br>
</br>

# Troubleshooting

If any issues occur with installing or configuring the above prerequisites, please review the following troubleshoot links or raise an issue in this repository:
<ul>
    <li><a href="https://docs.microsoft.com/en-us/azure/azure-functions/recover-python-functions?tabs=vscode">https://docs.microsoft.com/en-us/azure/azure-functions/recover-python-functions?tabs=vscode</a>
    <li><a href="https://docs.microsoft.com/en-us/azure/azure-functions/functions-recover-storage-account">https://docs.microsoft.com/en-us/azure/azure-functions/functions-recover-storage-account</a>
</ul>