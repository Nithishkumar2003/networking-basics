import ipaddress

print("================================")
print("      IP ADDRESS CHECKER")
print("================================")

ip = input("Enter an IP address: ")

try:
    address = ipaddress.ip_address(ip)

    print("\nIP Address:", address)
    print("IP Version: IPv" + str(address.version))

    if address.is_private:
        print("IP Type: Private IP")
    else:
        print("IP Type: Public IP")

    print("Status: Valid IP Address")

except ValueError:
    print("Status: Invalid IP Address")