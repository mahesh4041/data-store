import data_store as d
d.access.create("mahesh",41)#data successfully stored
d.access.create("yatheesh",66)#data successfully stored
d.access.create("karthik",21)#data successfully stored
d.access.create("vineeth",50,3600)# data stored with time to live property given value is in sec
d.access.create("mahesh",75)#raise error:key already stored
d.access.read("mahesh")#it gives the value in Jasonobject format 'key-value'
d.access.read("vineeth")#it gives the value in Jasonobject format if time to live property is not expired
d.access.delete("karthik")#deleting the key and its value from database
d.access.delete("naresh")#raise error: given key doesn't exist in the database


#output
#data successfully stored
#data successfully stored
#data successfully stored
#data successfully stored
#raise error:key already stored
#mahesh-41
#vineeth-50
#key is successfully deleted
#raise error: given key doesn't exist in the database
