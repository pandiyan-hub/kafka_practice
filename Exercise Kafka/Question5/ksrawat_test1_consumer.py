from kafka import KafkaConsumer

consumer=KafkaConsumer('ksrawat_test1',bootstrap_servers='otusdphdp3:6667')
f = open("demofile7.json", "a")
for message in consumer:
   print(message.value)
   f.write(message.value+"\r \n")
f.close()
