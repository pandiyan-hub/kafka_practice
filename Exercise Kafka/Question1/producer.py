from kafka import KafkaConsumer,KafkaProducer
from datetime import datetime
import time
producer = KafkaProducer(bootstrap_servers='otusdphdp3:6667')
f = open("demofile.txt", "r")

for x in f:
  message="Message {}".format(str(x))
  producer.send('ksrawat_test1',message.encode('utf-8'))
  time.sleep(2)
  print("Message Sent ",x)

producer.close()
