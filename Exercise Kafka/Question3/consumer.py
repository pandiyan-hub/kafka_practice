from kafka import KafkaConsumer

consumer = KafkaConsumer('ksrawat_test1',
                         bootstrap_servers='otusdphdp3:6667')
f = open('demofile3.txt', 'a')
f1 = open('demofile4.txt', 'a')
for message in consumer:
    if message.offset % 2 == 0:
        print('even',message.offset)
        f.write(message.value + 'Partition' + str(message.partition)
                + 'Offset' + str(message.offset) + '\n')
    else:
        print('odd',message.offset)
        f1.write(message.value + 'Partition' + str(message.partition)
                + 'Offset' + str(message.offset) + '\n')
f.close()
f1.close()