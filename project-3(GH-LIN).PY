#===========================================
# ===== FIREWALL ACCESS CONTROL SYSTEM =====
#===========================================

firewall_rules = {
    "192.168.1.1": [80, 443, 22],
    "10.0.0.5": [3306, 8080]
}

ip = input("Enter your IP address: ")
port = int(input("Enter your port number: "))

if ip in firewall_rules:
    if port in firewall_rules[ip]:
        print("Access Granted")
    else:
        print("Access Denied")
else:
    print("Unknown IP Address")