import requests
import json
import csv

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

def get_full_name(UniProt_accession):
    return (get_data_from_api(UniProt_accession)['protein']['recommendedName']['fullName']['value']).lower()

def get_sequence(UniProt_accession):
    return get_data_from_api(UniProt_accession)['sequence']['sequence']

def write_info_to_csv(UniProt_accession):
    name = get_full_name(UniProt_accession)
    sequence = get_sequence(UniProt_accession)
    if name and sequence is not None:
        with open('csv_file.csv', mode='a') as file:
            fieldnames = ['Accession', 'Name', 'Sequence']
            write = csv.DictWriter(file, fieldnames=fieldnames)

            write.writerow({
                'Accession': UniProt_accession,
                'Name': name,
                'Sequence': sequence
            })

def loop_through_accession(data_list):
    with open(data_list, 'rt') as list_file:
        for accession in list_file:
            accession = accession.strip()
            yield accession


    return accession, sequence

if __name__ == '__main__' :
    access = 'P16627'
    write_info_to_csv(access)
