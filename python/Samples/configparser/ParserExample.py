import configparser

#configfile name
file = 'config.ini'

#Setup Parser
config = configparser.ConfigParser()


#Write to config
#Create sections
#Create subsections
#Create enrties


#Read from config
config.read(file)

#list sections in file:
config.sections()

#Check for section:
'Paths' in config

#Get value:"
#opt 1:
home_dir = config['Paths']['home_dir']

#opt 2:
home_dir = config.get('IPs', 'localhost', fallback=None)


#Print all keys in section:
for key in config['Paths']:
    print(key)
    