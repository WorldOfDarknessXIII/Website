import yaml

WEBSITE = yaml.load(open("wod13site/config/website.yml"), Loader=yaml.SafeLoader)
SERVERS = yaml.load(open("wod13site/config/servers.yml"), Loader=yaml.SafeLoader)
