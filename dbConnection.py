import os
import json
import asyncio

from azure.cosmos.aio import CosmosClient
from azure.identity.aio import DefaultAzureCredential


endpoint = os.environ["COSMOS_ENDPOINT"]