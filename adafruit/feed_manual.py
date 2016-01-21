#Be sure to create a file called credentials.py with variables for the Adafruit feed key and a feed name to use
import credentials
from Adafruit_IO import Client, Feed, Data

print "Using AIO key " + credentials.aio_key + " to write data to feed " + credentials.feed_name
aio = Client(credentials.aio_key)

while True:
    try:
        in_data = raw_input("Enter data to feed to Adafruit or quit: ")
        if in_data == "quit":
            break
        data = Data(value=int(in_data))
        print "Writing " + in_data + " to feed"
        aio.create_data(credentials.feed_name, data)
    except:
        print "caught exception"

print "Quitting"
