import abc
from texts import spa

class SiteBase():
  basic_info: []
  community_info: []
  places_of_interest_info: []
  additional_intrigue_info: []
  others_info: []

  def basic_information():
    pass
  
  @abc.abstractclassmethod
  def community():
    pass

  @abc.abstractclassmethod
  def places_of_interest():
    pass

  @abc.abstractclassmethod
  def additional_intrigues():
    pass
  
  @abc.abstractclassmethod
  def others():
    pass

  pass


class ComercialHub(SiteBase):
  def basic_information():
    self._origin()
    self._speciality()
    self._antiquity()
    self._status()
    self._number_of_visitors()
    self.size()
    self.environment()
  
  def _origin():
    values = {1: spa.ORIGEN_1_PUESTO_COMERCIAL,
              2: spa.ORIGEN_2_PUESTO_COMERCIAL,
              3: spa.ORIGEN_3_PUESTO_COMERCIAL,
              4: spa.ORIGEN_4_PUESTO_COMERCIAL,
              5: spa.ORIGEN_5_PUESTO_COMERCIAL,
              6: spa.ORIGEN_6_PUESTO_COMERCIAL,
              7: spa.ORIGEN_7_PUESTO_COMERCIAL,
              8: spa.ORIGEN_8_PUESTO_COMERCIAL,
              }
    
    value = rand(1,8)
    self.basic_info.append(values[value]['text'])
    if 'suboption' in values[value].keys():
      pass #another random value to get suboption.


  def community():
    pass

  def places_of_interest():
    pass

  def additional_intrigues():
    pass

  def others(): 
      pass


class City(SiteBase):
  pass


class Town(SiteBase):
  pass