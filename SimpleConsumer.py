import json
from kafka import KafkaConsumer

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('cassie',
                         group_id='basis',
                         bootstrap_servers=['localhost:9092'])
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    #print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
     #                                     message.offset, message.key,
      #                                    message.value))
    print (message.value)
    #print (type(message.value))
    appendme=message.value + "\n"
    appendFile=open('doc.csv','a')
    appendFile.write(appendme)
    appendFile.close()

# consume earliest available messages, don't commit offsets
KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)

# consume json messages
KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii')))


# StopIteration if no message after 1sec
KafkaConsumer(consumer_timeout_ms=1000)


