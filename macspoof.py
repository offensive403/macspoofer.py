import subprocess

interface = input("Enter the name of the interface you want to change the MAC address of: ")
new_mac = input("Enter the new MAC address: ")

# Bring the interface down
subprocess.run(["ifconfig", interface, "down"])

# Change the MAC address
subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])

# Bring the interface back up
subprocess.run(["ifconfig", interface, "up"])
subprocess.run("ifconfig")
print("Your MAC is spoofed")
