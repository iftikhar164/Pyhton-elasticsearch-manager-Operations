from elasticsearch_op_manager import ElasticsearchManager

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