import requests
import json

access = 'P01889'


def get_data_from_api(UniProt_accession):
    link = 'https://www.ebi.ac.uk/proteins/api/proteins/{}'.format(UniProt_accession)
    result = requests.get(link, headers={'Accept':'application/json'})

    if result.ok:
        data = result.text
        data_json = json.loads(data)
    else:
        data_json = None
        print('Not found')
    return data_json

# if you don't know access number

def get_data_from_api_proteinname(protein_name):
    protein_name = protein_name.replace(" ", "%20")
    link = 'https://www.ebi.ac.uk/proteins/api/proteins?protein={}'.format(protein_name)
    result = requests.get(link, headers={'Accept':'application/json'})

    if result.ok:
        data = result.text
        data_json = json.loads(data)
    else:
        data_json = None
        print("Not found")
    return data_json


def check_full_name(UniProt_accession):
    return get_data_from_api(UniProt_accession)['protein']['recommendedName']['fullName']['value']

def get_sequence(UniProt_accession):
    return get_data_from_api(UniProt_accession)['sequence']['sequence']

