from tabula import convert_into
import csv
from requests_html import HTMLSession
import requests
from clint.textui import progress

session = HTMLSession()
# def parse_pdf(input_file, output_file):
#     convert_into(input_file, output_file, output_format='csv',
#                   pages='all', lattice=True)
#     return output_file


# parse_pdf('list.pdf', 'output.csv')

def main(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        next(reader)
        for row in reader:
            if "neuroanatomy" in str.lower(row[1]):
                link = get_download_link(row)
                print(f'Downloading - {row[1]}')
                download_file(row, link)
                print(f'Downloading - {row[1]}')

def get_download_link(csv_row):
    URL = csv_row[-1]
    r = session.get(URL)
    link_element = r.html.find('a.test-bookpdf-link', first=True)
    link = list(link_element.absolute_links)[0]
    return link

def download_file(csv_row, url):
    path = csv_row[1].replace(' ', '_')+ '.pdf'
    response = requests.get(url, stream= True)
    with open(path, 'wb') as f:
        total_length = int(response.headers.get('content-length'))
        for chunk in progress.bar(response.iter_content(chunk_size=1024), \
                                  expected_size=(total_length/1024)+1):
            if chunk:
                f.write(chunk)
                f.flush()
                
main("output.csv")