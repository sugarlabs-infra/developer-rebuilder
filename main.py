import os
import json
from pykafka import KafkaClient

client = KafkaClient(hosts='freedom.sugarlabs.org:9092')
topic = client.topics['org.sugarlabs.hook']
consumer = topic.get_simple_consumer()

for msg in consumer:
    try:
        value = json.loads(msg.value)
    except ValueError:
        print 'Error decoding message', msg.offset, msg.value
        continue

    if value['clone_url'] == 'https://github.com/sugarlabs/sugar-docs':
        os.system('git pull')
        os.system('rm -rf doc')
        os.system('/docker/docker -I -c default --extras addHeader,noFiles'
                  ' -x node_modules')
        os.system('cp -r images doc')
