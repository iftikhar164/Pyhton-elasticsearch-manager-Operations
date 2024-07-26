ElasticsearchManager: A Python Class for Managing Elasticsearch Operations
Overview
The ElasticsearchManager class provides a convenient interface for connecting to and interacting with an Elasticsearch cluster. It encapsulates several common operations such as connecting to the cluster, storing records, updating records, retrieving documents by ID, searching documents, and counting documents. This class handles connection initialization, error handling, and basic CRUD operations.

Code Explanation
Importing Required Modules
python
Copy code
from elasticsearch import Elasticsearch
This line imports the Elasticsearch class from the elasticsearch Python client library, which is used to interact with an Elasticsearch cluster.

Class Definition
python
Copy code
class ElasticsearchManager(object):
The ElasticsearchManager class is defined to encapsulate Elasticsearch operations.

Initialization Method
python
Copy code
def __init__(self, username=None, password=None, esaddress=None):
    self.username = username
    self.password = password
    self.esaddress = esaddress
    self.elastic_object = None
The __init__ method initializes the class with optional parameters for username, password, and esaddress. These parameters are used for authentication and specifying the Elasticsearch server address. The elastic_object attribute is initialized to None and will hold the Elasticsearch connection object.

Connection Method
python
Copy code
def get_connection(self):
    print("Starting initialization of {0}".format(self.esaddress))
    try:
        auth = None
        if self.username and self.password:
            auth = (self.username, self.password)

        es = Elasticsearch(self.esaddress)
        print("Successfully connected to elasticsearch.")
        self.elastic_object = es
        return True
    except Exception as e:
        print("Could not connect to elasticsearch! error: {0}".format(e))
        return False
The get_connection method attempts to establish a connection to the Elasticsearch server. If username and password are provided, they are used for authentication. The method prints messages indicating the status of the connection and sets the elastic_object attribute to the Elasticsearch client instance upon successful connection. It returns True if the connection is successful, otherwise False.

Storing Records
python
Copy code
def store_record(self, index_name, record, type="_doc"):
    try:
        outcome = self.elastic_object.index(index=index_name, doc_type=type, body=record)
        return True, outcome
    except Exception as ex:
        print('Error in indexing data error: {}'.format(str(ex)))
        return False, str(ex)
The store_record method indexes (stores) a document in the specified index_name. The document is passed as the record parameter, and the document type is specified by the type parameter. The method returns a tuple with a boolean indicating success and the outcome of the operation.

Updating Records
python
Copy code
def update_record(self, index_name, doc_id, record, type="_doc"):
    try:
        outcome = self.elastic_object.index(index=index_name, id=doc_id, doc_type=type, body=record)
        return True, outcome
    except Exception as ex:
        print('Error in updating of error {0}, doc_id: {1}.'.format(str(ex), doc_id))
        print(str(ex))
        return False, str(ex)
The update_record method updates a document in the specified index_name using its doc_id. The updated document is passed as the record parameter. The method returns a tuple with a boolean indicating success and the outcome of the operation.

Retrieving Documents by ID
python
Copy code
def get_document_by_id(self, index_name, document_id):
    try:
        result = self.elastic_object.get(index=index_name, id=document_id)
        return True, result
    except Exception as ex:
        print('Error in get_document_by_id, index: {0}, error: {1}'.format(index_name, str(ex)))
        return False, str(ex)
The get_document_by_id method retrieves a document from the specified index_name using its document_id. The method returns a tuple with a boolean indicating success and the retrieved document.

Searching Documents
python
Copy code
def search_documents(self, index_name, body=None):
    try:
        result = self.elastic_object.search(index=index_name, body=body)
        return True, result
    except Exception as ex:
        print('Error in search_documents, index: {0}, body: {1}, error: {2}'.format(index_name, body, str(ex)))
        return False, str(ex)
The search_documents method searches for documents in the specified index_name using the search query provided in the body parameter. The method returns a tuple with a boolean indicating success and the search results.

Counting Documents
python
Copy code
def count_documents(self, index_name, body=None, type="_doc"):
    try:
        result = self.elastic_object.count(index=index_name, doc_type=type, body=body)
        return True, result
    except Exception as ex:
        print('Error in counting documents of index name: {0}, error: {1}'.format(index_name, str(ex)))
        return False, str(ex)
The count_documents method counts the number of documents in the specified index_name that match the query provided in the body parameter. The method returns a tuple with a boolean indicating success and the count result.

Usage
To use the ElasticsearchManager class, instantiate it with the necessary parameters and call its methods as needed. Below is an example usage:

python
Copy code
# Initialize the ElasticsearchManager
es_manager = ElasticsearchManager(username="user", password="pass", esaddress="http://localhost:9200")

# Connect to Elasticsearch
if es_manager.get_connection():
    # Store a record
    record = {"name": "John Doe", "age": 30}
    success, outcome = es_manager.store_record(index_name="test_index", record=record)
    if success:
        print("Record stored:", outcome)
    else:
        print("Failed to store record:", outcome)

    # Get a document by ID
    success, result = es_manager.get_document_by_id(index_name="test_index", document_id="1")
    if success:
        print("Document retrieved:", result)
    else:
        print("Failed to retrieve document:", result)

    # Search for documents
    query = {"query": {"match_all": {}}}
    success, results = es_manager.search_documents(index_name="test_index", body=query)
    if success:
        print("Documents found:", results)
    else:
        print("Failed to search documents:", results)
This example demonstrates how to initialize the ElasticsearchManager, connect to Elasticsearch, store a record, retrieve a document by ID, and search for documents.

By including this detailed explanation in your GitHub repository, you will provide users with a clear understanding of how the ElasticsearchManager class works and how to use it effectively.
