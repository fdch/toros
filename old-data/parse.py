#!/usr/bin/env python

import json
import datetime
j = {
    0: "Sonic Arts Ensemble",
    1: "Jacob Kopcienski",
    3: "Gustavo Obligado"
}
v = {
    0: "Columbus, OH",
    1: "New York City, NY",
    2: "Online",
    3: "Cordoba, ARG",
    4: "Bariloche, ARG",
    5: "Berlin, DE"
}
y = {
    0: "The Ohio State University",
    1: "The Jacktrip Foundation",
    2: "Earth Day Art Model",
    3: "Horse Bar"
}
g = {
    0: "Wexner Center for the Arts",
    1: "Advanced Computing Center for the Arts and Design",
    2: "Deck10",
    3: "Live Performance"
}
kind = {
    0: "Live Performance",
    1: "Livestream",
    2: "Software Release"
}
def opener(f):
    data=[]
    with open(f+'.json', encoding="utf-8") as fp:
        data = json.load(fp)
    return data

event = opener('events')
new_event = []
for e in event:
    ne = {}
    ne['date'] = datetime.datetime(year=e['year'], month=e['month'],
                                   day=e['day']).isoformat()
    for k in e.keys():
        if k in ('year', 'month', 'day'): continue
        if k == 'location':
            ne[k] = v.get(e[k])
        elif k == 'venue':
            ne[k] = y.get(e[k])
        elif k == 'employer':
            ne[k] = j.get(e[k])
        elif k == 'institution':
            ne[k] = g.get(e[k])
        elif k == 'kind':
            ne['category'] = kind.get(e[k])
        else:
            ne[k] = e[k]
    new_event.append(ne)

with open("new_event.json", "w", encoding="utf8") as fp:
    json.dump(new_event, fp, indent=4)
