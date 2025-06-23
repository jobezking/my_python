os.path.getsize("spider.txt")
#This code will provide the file size

os.path.getmtime("spider.txt")
#This code will provide a unix timestamp for the file

import datetime
timestamp = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp)
#This code will provide the date and time for the file in an 
#easy-to-understand format

os.path.abspath("spider.txt")
#This code takes the file name and turns it into an absolute path
