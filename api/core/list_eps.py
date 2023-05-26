import requests
from requests.exceptions import HTTPError

def getListAllEps():
    try:
        response = requests.get('https://www.datos.gov.co/api/id/tq4m-hmg2.json?$query=select%20*%2C%20%3Aid%20search%20%27meta%27&$$query_timeout_seconds=30')
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        listEps = response.json()

        nameEpsUnics = set()
        listEpsNotRep = []
        for eps in listEps:
            name = eps["ent_nombre"]
            if name not in nameEpsUnics:
                nameEpsUnics.add(name)
                listEpsNotRep.append(eps)

        return [(eps["ent_id"], eps["ent_nombre"]) for eps in listEpsNotRep]
    