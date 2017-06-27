
import os, ssl
from os.path import expanduser

ca   = expanduser("~/.ssh/cloud_kafka/ca_cert.pem")
cert = expanduser("~/.ssh/cloud_kafka/signed_cert.pem") 
pkey = expanduser("~/.ssh/cloud_kafka/private_key.pem") 

brokers = ##"xxxx.cloudkafka.com:9093"
topic_prefix = 'oko9-'#'oko9-', topic prefix 

with open(ca, 'r') as myfile:
    CLOUDKARAFKA_CA=myfile.read()

with open(cert, 'r') as myfile:
    CLOUDKARAFKA_CERT=myfile.read()

with open(pkey, 'r') as myfile:
    CLOUDKARAFKA_PRIVATE_KEY=myfile.read()

# Write the client cert from the environment variables
# to files on disk and then load them into the context
with open("/tmp/client.pem", "w") as f:
    f.write(CLOUDKARAFKA_CERT)
with open("/tmp/client.key", "w") as f:
    f.write(CLOUDKARAFKA_PRIVATE_KEY)

# Create a SSL context
ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH,
                                         cadata=CLOUDKARAFKA_CA)
ssl_context.load_cert_chain('/tmp/client.pem', '/tmp/client.key')