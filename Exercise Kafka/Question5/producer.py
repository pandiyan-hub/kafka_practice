from kafka import KafkaConsumer,KafkaProducer
from datetime import datetime
import time
import json
producer = KafkaProducer(bootstrap_servers='otusdphdp3:6667')
f = open("demofile5.json", "r")

for x in f:
  message="Message {}".format(x)
  msg = json.loads(x)
  if (int(msg["id"]) > 10):
    producer.send('ksrawat_test1',message.encode('utf-8'))
    time.sleep(2)
    print("send to ksrawat_test1")
  else:
    producer.send('Sample_Msgs',message.encode('utf-8'))
    time.sleep(2)
    print("send to Sample_Msgs")
    

producer.close()