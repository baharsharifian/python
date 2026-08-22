print ("Enter Hostname: ")
hostname = input()
print ("Enter CPU Usage: ")
cpu = int(input())
print (" Enter RAM Usage: ")
ram = int(input())

if  cpu <=70:
    cpu_status ="healthy"
elif 70 <= cpu <= 90:
    cpu_status = "warning"
elif cpu >=90:
    cpu_status ="critical"

if  ram <=70:
    ram_status ="healthy"
elif 70 <= ram <= 90:
    ram_status = "warning"
elif ram >=90:
    ram_status ="critical"

if cpu_status == "critical" or ram_status == "critical":
    print("============")
    print(" Server Report")
    print("=============")
    print(f" hostname : {hostname}")
    print("server is critical")

elif cpu_status == "warning" or ram_status == "warning":
    print("============")
    print(" Server Report")
    print("=============")
    print(f" hostname : {hostname}")
    print("server is warning")

else:
    print("============")
    print(" Server Report")
    print("=============")
    print(f" hostname : {hostname}")
    print("server is ok")



