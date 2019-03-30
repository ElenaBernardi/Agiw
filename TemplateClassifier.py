import xml.etree.ElementTree as ET
import requests
from collections import defaultdict
from lxml import html, etree
from matplotlib import pyplot as plt

def list_urls(xmlFile):
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    list = root.findall(".//loc")
    urls=[]
    for i in list:
        urls.append(i.text)
    return urls

def count_tags(url):
    page = requests.get(url)
    tree = html.fromstring(page.text)

    tot = tree.xpath('//*')
    div = tree.xpath('//div')
    return (len(tot),len(div),len(div)/len(tot))

def get_number_of_pages_with_number_of_tags(pages, text):
    tags_dict = defaultdict(int)
    divs_dict = defaultdict(int)
    normalize_dict = defaultdict(int)
    vector_tags=[]
    vector_divs=[]
    vector_normalize=[]
    i = len(pages)
    for element in pages:
        print(i)
        i-=1
        elements = count_tags(element)
        text.write(element+"\t"+str(elements[0])+"\t"+str(elements[1])+"\t"+str(elements[2])+"\n")

        tags_dict[elements[0]]+=1
        divs_dict[elements[1]]+=1
        normalize_dict[elements[2]]+=1
    keys_tags = sorted(tags_dict)
    keys_divs = sorted(divs_dict)
    keys_normalize = sorted((normalize_dict))
    for key in keys_tags:
        vector_tags.append(tags_dict[key])
    for key in keys_divs:
        vector_divs.append(divs_dict[key])
    for key in keys_normalize:
        vector_normalize.append(normalize_dict[key])
    return (keys_tags, vector_tags, keys_divs, vector_divs, keys_normalize, vector_normalize)

if __name__=="__main__":

    urls = list_urls("sitemap-.xml")
    print(len(urls))
    text = open("dati.txt","w+")
    vectors = get_number_of_pages_with_number_of_tags(urls, text)
    plt.plot(vectors[0] , vectors[1], 'b', label='Tags Tot')
    plt.show()
    plt.plot(vectors[2], vectors[3], 'b', label='Div Tot')
    plt.show()
    plt.plot(vectors[4], vectors[5], 'b', label='Normalize Tot')
    plt.show()