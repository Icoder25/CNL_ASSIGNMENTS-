import math

# 1. Get user input for Base IP and CIDR prefix
ip = input("Enter base IP address (e.g., 192.168.10.0): ")
cidr = int(input("Enter CIDR prefix (e.g., 26 for /26): "))

# Split IP address into four octets
o1, o2, o3, o4 = map(int, ip.split("."))

# Validate for Class C subnetting range
if cidr < 24 or cidr > 30:
    print("Error: This program currently supports Class C subnetting (CIDR 24 to 30).")
    exit()

# 2. Calculate subnetting details

# Number of host bits
hostBits = 32 - cidr

# Size of each subnet
blockSize = 2 ** hostBits

# Number of subnets
numSubnets = 256 // blockSize

# Usable hosts in each subnet
usableHosts = blockSize - 2

# Last octet of subnet mask
lastOctetMask = 256 - blockSize

# Display general subnet information
print("\n--- General Subnet Information ---")
print("Calculated Subnet Mask :", "255.255.255." + str(lastOctetMask))
print("Total Usable Hosts     :", usableHosts, "per subnet")
print("Total Subnets Created  :", numSubnets)
print()

# 3 & 4. Calculate and display each subnet
for i in range(numSubnets):

    # Network address
    network = i * blockSize

    # First usable host
    firstHost = network + 1

    # Last usable host
    lastHost = network + usableHosts

    # Broadcast address
    broadcast = network + blockSize - 1

    print("=========================================")
    print("Subnet", i + 1)
    print("=========================================")

    print("Network Address   :", f"{o1}.{o2}.{o3}.{network}")
    print("First Host        :", f"{o1}.{o2}.{o3}.{firstHost}")
    print("Last Host         :", f"{o1}.{o2}.{o3}.{lastHost}")
    print("Broadcast Address :", f"{o1}.{o2}.{o3}.{broadcast}")

    # Print all usable IP addresses
    print("\nUsable IP Addresses:")

    for j in range(firstHost, lastHost + 1):
        print(f"  {o1}.{o2}.{o3}.{j}")

    print()