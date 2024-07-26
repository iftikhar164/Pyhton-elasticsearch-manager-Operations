from elasticsearch import Elasticsearch


class ElasticsearchManager(object):
    def __init__(self, username=None, password=None, esaddress=None):
        self.username = username
        self.password = password
        self.esaddress = esaddress
        self.elastic_object = None

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

    def store_record(self, index_name, record, type="_doc"):
        try:
            outcome = self.elastic_object.index(index=index_name, doc_type=type, body=record)
            return True, outcome
        except Exception as ex:
            print('Error in indexing data error: {}'.format(str(ex)))
            return False, str(ex)

    def update_record(self, index_name, doc_id, record, type="_doc"):
        try:
            outcome = self.elastic_object.index(index=index_name, id=doc_id, doc_type=type, body=record)
            return True, outcome
        except Exception as ex:
            print('Error in updating of error {0}, doc_id: {1}.'.format(str(ex), doc_id))
            print(str(ex))
            return False, str(ex)

    def get_document_by_id(self, index_name, document_id):
        try:
            result = self.elastic_object.get(index=index_name, id=document_id)
            return True, result
        except Exception as ex:
            print('Error in get_document_by_id, index: {0}, error: {1}'.format(index_name, str(ex)))
            return False, str(ex)

    def search_documents(self, index_name, body=None):
        try:
            result = self.elastic_object.search(index=index_name, body=body)
            return True, result
        except Exception as ex:
            print('Error in search_documents, index: {0}, body: {1}, error: {2}'.format(index_name, body, str(ex)))
            return False, str(ex)

    def count_documents(self, index_name, body=None, type="_doc"):
        try:
            result = self.elastic_object.count(index=index_name, doc_type=type, body=body)
            return True, result
        except Exception as ex:
            print('Error in counting documents of index name: {0}, error: {1}'.format(index_name, str(ex)))
            return False, str(ex)
