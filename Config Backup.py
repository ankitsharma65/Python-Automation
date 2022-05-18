

from netmiko import ConnectHandler
from getpass import getpass
from datetime import date
import os


#### Global variables
new_dir = ''
file_path = 'C:\\Users\\asharma\\Downloads\\Python Code\\deviceip.txt'
output_dir = 'C:\\Users\\asharma\\Desktop\\Configs\\Automated Backup'

username = input('Enter your username: ')
password = getpass()

# Reading a file of ip addresses
try:
	with open(file_path) as f:
		coredevices = f.read().splitlines()

	# Iterating through list of devices

		for devices in coredevices:
			print('Connecting to device:' + str(devices))
			ip_addr = devices

			core = {
			'device_type': 'cisco_ios',
			'ip': ip_addr,
			'username':username,
			'password':password
			}



			#### Establish an SSH connection to the device by passing in the device dictionary.

			net_connect = ConnectHandler(**core)


			#### Get hostname of the device
			hostname = net_connect.find_prompt()
			hostname = hostname.replace('#','')

			#### Getting date
			getdate = date.today()

			#### Putting date in right format
			date1 = getdate.strftime("%d%m%y")

			#### Execute show commands.
			output = net_connect.send_command('show run')

			#### Changing the output directory
			os.chdir(output_dir)

			#### Create a new folder with date

			if new_dir == '':
				new_dir = date.today().strftime("%d%m%y")
				os.mkdir(new_dir)
				os.chdir(new_dir)
			else:
				os.chdir(new_dir)

			####open file to write command output	
			file = open(str(hostname) + '_' + str(date1) + '.txt' , 'w')

			#### Write output to file above
			file.write(output)
			file.close()

except scerror as error:
	print('Exception occured', error.value)

else:
	print('Script executed Successfully')



