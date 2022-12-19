#!/usr/env python
from schemas.venue import Venue
from schemas.country import Country
from schemas.state import State
from schemas.city import City

import json
from helpers import json_read

schemas = {
  "venue" : json.loads(Venue.schema_json()),
  "country" : json.loads(Country.schema_json()),
  "state" : json.loads(State.schema_json()),
  "city" : json.loads(City.schema_json())
}

database = {
  "venue" : json_read("../data/venue.json"),
  "country" : json_read("../data/country.json"),
  "state" : json_read("../data/state.json"),
  "city" : json_read("../data/city.json"),
  "person" : json_read("../data/person.json"),
}

#print(json.dumps(venue_schema, indent=4))



