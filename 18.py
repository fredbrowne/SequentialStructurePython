# Create a program that asks the size of a file to download (in MB) and the connection speed (in Mbps), 
# calculate and inform the approximate time to download the file using this link (in minutes).


file_size = int(input('Type the size of the file (in MB) to download: '))
connection_speed = int(input('Type the connection speed (in Mbps): '))

seconds_mb = connection_speed / 8
transfer_calc = file_size / seconds_mb

print(f'It will take { transfer_calc} seconds to download.')