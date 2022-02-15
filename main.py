from giantbomb import GiantBomb
import requests as requests
from index import Index


class GiantBombSearch(object):

    def get_data(self, offset: int) -> list:
        """
        Gets game data from GiantBomb API
        :param offset: Page number
        :return: list of games
        """
        try:
            url = f'http://www.giantbomb.com/api/games/?api_key=6fe6fb576b0c7bef2364938b2248e1628759508d&format=json&offset={str(offset)}&platforms=21'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            dictionary = response.json()

            data_dictionary = dictionary["results"]
        except requests.exceptions.HTTPError as error:
            print(error)
        finally:
            response.close()
        return data_dictionary

    def index_documents(self, data_documents: list[dict]) -> Index:
        """
        Create an Index of words in the aliases and name fields using the ids of the documents as the set
        :param data_documents: game data from GiantBomb
        :return: all the indexed words
        """
        def extract_data(data_list: list[dict]):
            for giantbomb in data_list:
                yield GiantBomb(aliases=giantbomb.get('aliases'), name=giantbomb.get('name'), id=giantbomb.get('id'),
                                site_detail_url=giantbomb.get('site_detail_url'),
                                description=giantbomb.get('description'))

        index = Index()
        for document in extract_data(data_documents):
            index.create_index(document)

        return index

    def search(self):
        """
        Provides the user interface to query the game data and also the call to GiantBomb API and Index methods
        :return: None
        """
        d_list = []
        for offset_iter in range(298, 301):
            d_list.extend(self.get_data(offset_iter))

        index_all = self.index_documents(d_list)
        print(f'Index contains {len(index_all.documents)} words')
        search_key = input("Please enter the game title keyword(s) to search: ")
        documents = index_all.search_index(search_key)

        print('\n' + str(len(documents)) + ' game title(s) found ...\n')
        for x in documents:
            print('\nName = ' + x.name)
            if x.aliases:
                print('aliases = ' + x.aliases)
            if x.description:
                print('description = ' + x.description)
            if x.site_detail_url:
                print('site_detail_url = ' + x.site_detail_url)


def main():
    gb_search = GiantBombSearch()
    gb_search.search()


if __name__ == '__main__':
    main()
