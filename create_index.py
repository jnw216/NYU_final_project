from elasticsearch import Elasticsearch
import lxml.html
import requests
import json

es = Elasticsearch("http://localhost:9200")
r = json.loads(requests.get("http://localhost:5000/site_index").text)

def html_to_text(url):
    if url.startswith("/"):
        url = url.replace("/grab_entry","http://localhost:5000/grab_entry")
    r = requests.get(url)
    html = lxml.html.fromstring(r.text)
    string = html.xpath("//html")[0].text_content()
    return string.encode("ascii","ignore")

def to_index(route,text):
    data = {}
    data["route"] = route
    data["body"] = text
    es.index(index="search",doc_type="text",body=data)

index_text = html_to_text(r["/index"])
about_me_text = html_to_text(r["/about_me"])
rec = requests.get(r["/blog"])
blog_text = html_to_text(r["/blog"])
html = lxml.html.fromstring(rec.text)
links_to_grab = [elem for elem in html.xpath("//a/@href") if "grab_entry" in elem]
text_for_blog = [html_to_text(elem) for elem in links_to_grab]
routes_for_blog = [elem.replace("http://localhost:5000","") for elem in links_to_grab]
to_index("/index",index_text)
to_index("/about_me",about_me_text)
to_index("/blog",blog_text)
[to_index(routes_for_blog[i],text_for_blog[i]) for i in range(len(routes_for_blog))]
