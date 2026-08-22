servers = [
    {
        "hostname": "cp1",
        "ip": "10.0.0.1",
        "cpu": 45,
        "ram": 60
    },
    {
        "hostname": "cp2",
        "ip": "10.0.0.2",
        "cpu": 95,
        "ram": 80
    },
    {
        "hostname": "cp3",
        "ip": "10.0.0.3",
        "cpu": 55,
        "ram": 85
    }
]

for server in servers:
    hostname = server["hostname"]
    cpu =server["cpu"]
    ram = server["ram"]
    if cpu >=90 or ram>=90:
        status="critical"
    elif cpu>=70 or ram >=70:
        status ="warning"
    else:
        status= "healthy"
    print(f"{hostname} - {status}")