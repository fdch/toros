#!/usr/env python
import schemas
import config
import json
import readline
from helpers import json_read
print(config.tables)
quit()


database = {
  "venue" : json_read("../data/venue.json"),
  "country" : json_read("../data/country.json"),
  "state" : json_read("../data/state.json"),
  "city" : json_read("../data/city.json"),
  "person" : json_read("../data/person.json"),
}

#print(json.dumps(venue_schema, indent=4))


def input_with_prefill(prompt, text):
  def hook():
    readline.insert_text(text)
    readline.redisplay()
  readline.set_pre_input_hook(hook)
  result = input(prompt)
  readline.set_pre_input_hook()
  return result

def input_new_venue(obj):
  print("Input Venue")
  for prop, types in schemas['venue']['properties'].items():
    
    required = prop in schemas['venue']['required']
    req = "(required)" if required else ""
    prefill = obj[prop] if prop in obj else ""
    if prop.endswith("Ref"):
      print(prop, "can be one of", '/'.join(database[prop.replace('Ref','')].keys()))
    elif prop.endswith("Refs"):
      print("A list of references", prop)
    while 1:
      obj[prop] = input_with_prefill(f"{prop} {req} ({types['type']}): ", prefill)
      if required and obj[prop] in database['venue']:
        print(f"{obj[prop]} already in the database:")
        print(obj[prop]+":", json.dumps(database['venue'][obj[prop]], indent=4));
        print("Please enter a new key.")
      else:
        break
  return obj







obj = {}

while 1:
  obj = input_new_venue(obj)
  print(json.dumps(obj,indent=4))
  veredict = input("Is this correct? [Y]/n: ")

  if veredict in ("Y","","y"):
    print("FINISHED")
    try:
      new_venue = Venue(**obj)
    except Exception as e:
      print("Error creating object")
      raise(e)
    obj_noid = { k : obj[k] for k in obj if k != 'id' } 
    database['venue'].update({obj['id']:obj_noid})
    #print(database['venue'])

    with open("../data/event.json", "w") as f:
      json.dump(database['venue'], f, indent=4)
   
   # find keys that end with "Ref"
    # and update tables with new key if it does not exist
    for key in obj:
      if key.endswith("Ref"):
        if obj[key] not in database[key.replace('Ref','')]:
          print("Input Country")
    
    break

  else:

    next_step = input("Do you want to try again? [Y]/n: ")

    if next_step not in ("Y","y",""):
      print("Venue not created.")
      break




