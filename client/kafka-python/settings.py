import yaml

with open("../config.yml", 'r') as ymlfile:
    try:
        cfg = yaml.load(ymlfile)
    except yaml.YAMLError as exc:
        print(exc)

BOOTSTRAP_SERVERS = cfg['KAFKA']['BOOTSTRAP_SERVERS']
TOPICS = cfg['TOPICS']['TOPICS']
MSG = (cfg['TOPICS']['MSG'])

print(BOOTSTRAP_SERVERS)