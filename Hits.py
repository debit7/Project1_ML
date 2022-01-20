class Hits(object):
    def __init__(self,hour,no_of_hits):
        if isinstance(hour,int) is False:
            raise TypeError("Invalid Hour")
        if no_of_hits.lower()=='nan':
            self.no_of_hits=0
        elif isinstance(no_of_hits,int) is False:
            self.no_of_hits=no_of_hits
        
        self.hour=hour
    

    