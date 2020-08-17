from kafka import KafkaConsumer

consumer=KafkaConsumer('Sample_Msgs',bootstrap_servers='otusdphdp3:6667')
f = open("demofile6.json", "a")
for message in consumer:
   print(message.value)
   f.write(message.value+"\r \n")
f.close()
