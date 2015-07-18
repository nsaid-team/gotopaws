#!/usr/bin/env python
import elasticsearch

es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
es.index(index='gtp_index', doc_type='city', id=1, body={
    'title': 'Austin, Texas',
    'subtitle': 'Music Capitol of the World',
    'url': 'City_Austin.html',
    'shelters_text': 'Shelters in Austin... It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using \'Content here, content here\', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for \'lorem ipsum\' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)',
    'pets_text': 'Pets in Austin... It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using \'Content here, content here\', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for \'lorem ipsum\' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)',
    'vets_text': 'Vets in Austin... You are dumb if you don\'t take your pet to the corner vet'
})

import elasticsearch

es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
es.index(index='gtp_index', doc_type='city', id=2, body={
    'title': 'San Francisco, California',
    'subtitle': 'Gold in peace, iron in war',
    'url': 'City_SF.html',
    'shelters_text': 'Shelters in San Francisco... It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using \'Content here, content here\', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for \'lorem ipsum\' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)',
    'pets_text': 'Pets in San Francisco... It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using \'Content here, content here\', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for \'lorem ipsum\' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)',
    'vets_text': 'Vets in San Francisco... \"5 stars for SF Pet hospital isn\'t enough!\nMy 14 year old cat, Titan got sick from a digestion issue. I brought him to SF Pet Hospital. The staff and vets...\"'
})

import elasticsearch

es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
es.index(index='gtp_index', doc_type='city', id=3, body={
    'title': 'Houston, Texas',
    'subtitle': 'Space City',
    'url': 'City_Houston.html',
    'shelters_text': 'Shelters in Houston... It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using \'Content here, content here\', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for \'lorem ipsum\' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)',
    'pets_text': 'Pets in Houston... It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using \'Content here, content here\', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for \'lorem ipsum\' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)',
    'vets_text': 'Vets in Houston... \"5 stars for SF Pet hospital isn\'t enough!\nMy 14 year old cat, Titan got sick from a digestion issue. I brought him to SF Pet Hospital. The staff and vets...\"'
})