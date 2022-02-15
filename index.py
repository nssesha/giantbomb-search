from giantbomb import GiantBomb
from corpus import transform


class Index:
    def __init__(self):
        self.index = {}
        self.documents = {}

    def create_index(self, document: GiantBomb):
        """
        Create an Index of words in the aliases and name fields using the ids of the documents as the set
        :param document: Game data from GiantBomb
        :return: dictionary of list of words indexed and id of the document
        """
        if document.id not in self.documents:
            self.documents[document.id] = document

        for word in transform(document.fulltext, False):
            if word not in self.index:
                self.index[word] = set()
            self.index[word].add(document.id)

    def _indexed_results(self, transformed_query: str) -> list[set]:
        return [self.index.get(word, set()) for word in transformed_query]

    def search_index(self, query: str) -> list:
        """
        Search will return documents that contain words from the query
        """

        transformed_query = transform(query, True)
        results = self._indexed_results(transformed_query)
        # AND operation
        documents = [self.documents[doc_id] for doc_id in set.intersection(*results)]

        return documents
