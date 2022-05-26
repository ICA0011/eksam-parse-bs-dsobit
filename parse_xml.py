from bs4 import BeautifulSoup
import requests
import lxml


def parse_xml():
    """Method for xml parsing."""

    url = "http://upload.itcollege.ee/~aleksei/test.xml"
    xml_content = requests.get(url).content
    soup = BeautifulSoup(xml_content, 'xml')
    result = soup.find("data").contents
    return str(result[0]).strip()