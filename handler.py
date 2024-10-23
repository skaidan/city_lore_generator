URL_BASE = "https://watabou.github.io/city-generator/?"

class PlaceHandler():
  size:int
  seed:int
  citadel:bool
  urban_castle:bool
  plaza:bool
  temple:bool
  walls:bool
  shantytown:bool
  coast:bool
  river:bool
  greens:bool
  gates:bool
  hub:bool
  
  def __init__(self, url:str):
    errors = []
    parameters = {"size": self.size, "seed": self.seed}

    url_without_base = url.removeprefix(URL_BASE)
    if url == url_without_base:
      errors.append(f"La url no contiene la base {URL_BASE}")

    for parameter in parameters.keys:
      if parameter in url_without_base:
        parameter_url = (url_without_base+'.')[1]
        value = parameter_url.split(parameters[parameter])[1].split('&')[0]
        if value is '1':
          parameters[parameter] = True
        else:
          parameters[parameter] = False
  
  
    
