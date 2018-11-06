from datetime import datetime, date, timedelta

class DeliveryWindow:
    def __init__(self, starts_at=datetime.now(), ends_at=datetime.now()+timedelta(hours=2)):
        self.starts_at = starts_at
        self.ends_at = ends_at
        
    @classmethod
    def generate(cls):
        windows = []
        today = date.today()
        days = [0, 1, 2, 3, 4, 5, 6]
        hours = [8, 10, 12, 14, 16, 18, 20]
        for d in days:
          day = today + timedelta(days=d)
          for h in hours:
              start = datetime(day.year, day.month, day.day, h)
              end = start+timedelta(hours=2)
              windows.append(DeliveryWindow(starts_at=start, ends_at=end))
        return windows
    
    def __str__(self):
        return "(Starts: {}, Ends: {})".format(self.starts_at, self.ends_at)
    
    def __repr__(self):
        return self.__str__()
        
class Address:
    def __init__(self, zip_code='10001', is_reception=False):
        self.zip_code = zip_code
        self.is_reception = is_reception
    
    @classmethod
    def available_zip_codes(self):
        return ["10001", "10002", "10003"]

class Medication:
    def __init__(self, drug='Lipitor', in_stock_date=date.today()):
        self.drug = drug
        self.in_stock_date = in_stock_date
    

class Order:
    def __init__(self, address=Address(), medications=[Medication()]):
        self.address = address
        self.medications = medications

    def available_windows(self):
        available_zips = Address.available_zip_codes()
        all_windows = DeliveryWindow.generate()
        
        if not self.address.zip_code in available_zips:
            print "Not available"
            return False
        else:
            windows = []
            
            for medication in self.medications:
                for window in all_windows:
                    start_date = window.starts_at
                    
                    if medication.in_stock_date <= start_date.date() and start_date > datetime.now():
                        windows.append(window)
                        
            return windows
                        

        return all_windows

print Order().available_windows()

