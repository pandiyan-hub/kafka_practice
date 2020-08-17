from kafka import KafkaConsumer,KafkaProducer
import time


consumer=KafkaConsumer('ksrawat_test1',bootstrap_servers='otusdphdp3:6667')
producer = KafkaProducer(bootstrap_servers='otusdphdp3:6667')


for message in consumer:
   print(message.value)
   newmessage="testing  transformation  -->>"+message.value.upper()
   newmessage2="Message {}".format(str(message.value.upper()))
   producer.send('Sample_Msgs',newmessage2.encode('utf-8'))
   print("Message Sent ",newmessage2)
   time.sleep(2)
producer.close()