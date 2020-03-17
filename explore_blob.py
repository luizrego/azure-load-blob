from azure.storage import CloudStorageAccount
from azure.storage.blob import BlockBlobService, PageBlobService, AppendBlobService
import os
import config

'''
Further reference:
    # 1. connect to the current blob
    https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python-legacy
    2. advanced properties
    https://github.com/Azure-Samples/storage-blob-python-getting-started/blob/master/blob_advanced_samples.py
    3. create metadata and etc
    https://github.com/Azure/azure-storage-python/blob/master/samples/blob/block_blob_usage.py
    4. Quickstart with blobs
    https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python
'''

# 0. Setup account
if config.IS_EMULATED:
    account = CloudStorageAccount(is_emulated=True)
else:
    account_name = config.STORAGE_ACCOUNT_NAME
    account_key = config.STORAGE_ACCOUNT_KEY
    account = CloudStorageAccount(account_name, account_key)


# 1. Create the BlockBlockService that the system uses to call the Blob service for the storage account.
block_blob_service = account.create_block_blob_service()

# 2. List the blobs in the container.
print("\nList blobs in the container")
generator = block_blob_service.list_blobs('test01')
for blob in generator:
    print("\t Blob name: " + blob.name)

# 3. Set metadata to blob
metadata = {'val1': 'foo', 'val2':'blah'}
block_blob_service.set_blob_metadata('test01', 'a dopo.txt', metadata)

# 4. Explore the metadata of the blobs and properties
print('1. get blob properties')
blob = block_blob_service.get_blob_properties('test01', 'a dopo.txt')
print(blob.name)
print(blob.properties.last_modified)
print(blob.metadata['val2'])

'''
for key in blob.metadata:
    print(blob.metadata['val2'])
'''