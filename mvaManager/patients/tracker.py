import datetime 

def endofBlock1(accident_date):
  duration = datetime.timedelta(days=28)
  return accident_date + duration

def endofBlock2(accident_date):
  duration = datetime.timedelta(days=56)
  return accident_date + duration

def endofBlock3(accident_date):
  duration = datetime.timedelta(days=84)
  return accident_date + duration