import datetime
import time

def isInt(s):
  #Check if a number is an integer
  try: 
      int(s)
      return True
  except ValueError:
      return False


class PicoPlaca:
  '''
  Class that allows knowing if a vehicle with a certain license plate is 
  allowed to transit on a certain day and time according to the restrictions 
  in the city of Quito-Ecuador.
  
  Parameters
  ----------
  plateNumber: It has to finish with a number.
  date: In format d/m/Y.
  time: In format H:M.

  Example
  --------
  Checking if a vehicle is allowed.
   >>> a = PicoPlaca('ABC211','31/05/2021','7:00')
   >>> a.message()
   The vehicle is NOT allowed to road

  '''
  def __init__(self, plateNumber, date, time):
    self.plateNumber = plateNumber
    self.date = date
    self.time = time
    self.formatDate = "%d/%m/%Y"
    self.formatHour = '%H:%M'

    #{Week days : [ plate numbers, hours]}. Monday starts with 0.
    '''
    #New restrictions (hoy no circula)
    self.infoPicoPlaca = {0:[[0,1,2,3], [[6,20]]],
                          1:[[2,3,4,5], [[6,20]]],
                          2:[[4,5,6,7], [[6,20]]],
                          3:[[6,7,8,9], [[6,20]]],
                          4:[[0,1,8,9], [[6,23]]],
                          5:[[-1],[[-1,-1]]],
                          6:[[-1],[[-1,-1]]]}
    '''
    #Old restrictions (pico y placa)
    self.infoPicoPlaca = {0:[[0, 1], [[7, 9.5], [16, 19.5]]],
                          1:[[2, 3], [[7, 9.5], [16, 19.5]]],
                          2:[[4, 5], [[7, 9.5], [16, 19.5]]],
                          3:[[6, 7], [[7, 9.5], [16, 19.5]]],
                          4:[[8, 9], [[7, 9.5], [16, 19.5]]],
                          5:[[-1],[[-1,-1]]],
                          6:[[-1],[[-1,-1]]]}


  def validPlate(self):
    #Check if the plate number has an integer as the last element.
    if len(self.plateNumber) > 0:
      return isInt(self.plateNumber[-1])
    else:
      return False


  def validDate(self):
    #Check if the date is in a valid format (d,m,Y).
    try:
      datetime.datetime.strptime(self.date,self.formatDate)
      return True
    except ValueError:
      return False


  def validTime(self):
    #Check if the hour is in a valid format(H:M).
    try:
      time.strptime(self.time,self.formatHour)
      return True
    except:
      return False


  def isAllowed(self):
    result = True


    #Check if the data is valid.
    if self.validPlate() and  self.validDate() and self.validTime():
      
      #Computing the last digit of the plate.
      lastDigitPlate = int(self.plateNumber[-1])
      
      #Computing the week day of a date.
      day, month, year = (int(x) for x in self.date.split('/')) 
      weekDay = datetime.date(year, month, day).weekday()      
      
      #Converting the time to hours. 
      hours, minutes = (int(x) for x in self.time.split(':')) 
      hour = hours + minutes/60

      #Check the plate and weekday restriction.
      if lastDigitPlate in self.infoPicoPlaca.get(weekDay)[0]:
        #Chek if the hour is in the restriction
        for horas in self.infoPicoPlaca.get(weekDay)[1]:
          if horas[0]<= hour <= horas[1]:
            result = False
            break

    else:
      #The data is not in the proper format.
      return 'formato'

    return result

  def message(self):
    
    result = self.isAllowed()
    #print the message according to the result
    if result == True:
      print('The vehicle is allowed to road')
    elif result == False:
      print('The vehicle is NOT allowed to road')
    else:
      #Validating (or not) the atributes.
      conditions = {'plate number': self.validPlate(), 
                    'date': self.validDate(), 
                    'time': self.validTime() }

      #Detailing what data is not in the proper format.
      for cond in conditions.keys():
        if conditions[cond] == False:
          print(f'The element {cond} is not in a valid format')
      

