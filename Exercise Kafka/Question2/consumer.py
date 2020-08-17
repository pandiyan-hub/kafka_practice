from kafka import KafkaConsumer

consumer=KafkaConsumer('Sample_Msgs',bootstrap_servers='otusdphdp3:6667')
f = open("demofile2.txt", "a")
for message in consumer:
   print(message.value)
   print(message.partition)
   print(message.offset)
   f.write(message.value+"Partition"+str(message.partition)+"Offset"+str(message.offset)+"\n")
f.close()
