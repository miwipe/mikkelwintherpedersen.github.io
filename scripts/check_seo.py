"""Validate generated search metadata and structured identity references."""
from html.parser import HTMLParser
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
class Metadata(HTMLParser):
 def __init__(self):
  super().__init__(); self.meta={}; self.alternates={}; self.canonical=''; self.ld=''; self.in_ld=False; self.title=''; self.in_title=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='meta': self.meta[a.get('name',a.get('property'))]=a.get('content')
  if tag=='link' and a.get('rel')=='canonical': self.canonical=a['href']
  if tag=='link' and a.get('rel')=='alternate': self.alternates[a['hreflang']]=a['href']
  if tag=='script' and a.get('type')=='application/ld+json':self.in_ld=True
  if tag=='title':self.in_title=True
 def handle_data(self,data):
  if self.in_ld:self.ld+=data
  if self.in_title:self.title+=data
 def handle_endtag(self,tag):
  if tag=='script':self.in_ld=False
  if tag=='title':self.in_title=False

titles=set(); count=0
for lang in ['da','en']:
 for filename in ['index.html','about.html','group.html','talks.html','press.html']:
  path=root/filename if lang=='da' else root/'en'/filename
  data=Metadata();data.feed(path.read_text(encoding='utf-8'))
  assert data.title and data.title not in titles; titles.add(data.title)
  assert data.meta['description'] and data.meta['og:title']==data.title
  assert data.meta['og:description']==data.meta['description']
  assert data.canonical==data.meta['og:url']==data.alternates[lang]
  assert set(data.alternates)=={'da','en','x-default'}
  graph=json.loads(data.ld)['@graph'];person,page=graph
  assert page['url']==data.canonical and page['inLanguage']==lang
  assert page['about']['@id']==person['@id']
  assert len(person['sameAs'])==4 and all(u.startswith('https://') for u in person['sameAs'])
  if filename=='about.html':assert page['@type']=='ProfilePage' and page['mainEntity']['@id']==person['@id']
  count+=1
print(f'SEO checks passed for {count} pages: unique titles, descriptions, canonical/language URLs and valid JSON-LD references.')
