import os, requests, xmltodict, json, logging
from  requests.exceptions import HTTPError
from bs4 import BeautifulSoup
from api.helpers.feed_helper import *

class AutoEsporteFeed():

    url = None
    response_xml = None
    list_items = None

    def __init__(self):
        try:
            self.url = os.environ.get('URL_FEED_XML')
            logging.info(self.url)
        except (AttributeError, TypeError) as e:
            logging.error("ENV ERROR : {}".format(str(e)))
            raise Exception("value URL_FEED_XML not founded")


    def __parse_xml(self):
        try:
            tree = xmltodict.parse(self.response_xml.content)
            self.list_items = json.loads(json.dumps(tree['rss']['channel']['item']))
        except ValueError as e:
            logging.error("PARSER XML ERROR : {}".format(str(e)))
            raise Exception("XML error to parser")


    def __call_feed(self):
        self.response_xml = requests.get(self.url)
        logging.info(self.response_xml)


    def __parse_to_serializers(self):
        self.list_items = [ { "item" : self.__parse_content(it) } for it in self.list_items ]


    def __parse_content(self, it):
        try:
            html = BeautifulSoup(it['description'], 'html.parser')
            tag_parser = html.select('img, a, p, ul')
            content = []
            
            for tag in tag_parser:

                if str(tag.name) == 'img' : 
                    content.append({"type":"image", "content" : tag['src']})

                elif str(tag.name) == 'a' : 
                    content.append({"type":"links", "content" : tag['href']})
                    
                elif str(tag.name) == 'p' : 
                    if len(str(tag.get_text()).strip()) > 0 :
                        content.append({"type":"text", "content" : str(tag.get_text()).strip() })
                        
                elif str(tag.name) == 'ul' : 
                    lists = [ li for li in tag.contents if len(str(li).strip()) > 0 ]
                    content.append({"type":"links", "content" : 
                        [ a.select('a')[0]['href'] for a in lists if len(a.select('a')) > 0 ] 
                    })
            
            it['description'] = content

            return it

        except Exception as e:
            logging.error("PARSE CONTENT ITEM {}".format(str(e)))


    def get_feed(self):
        try:
            
            self.__call_feed()
            self.__parse_xml()
            self.__parse_to_serializers()

            return self.list_items

        except HTTPError as e:
            logging.error("FEED HTTP ERROR : {}".format(str(e)))
            raise Exception("Feed http error")
        
        except Exception as e:
            logging.error("GET FEED ERROR : {}".format(str(e)))