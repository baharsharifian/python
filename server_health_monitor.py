servers=[
{
    "hostname": "cp1",
    "ip": "10.0.0.1",
    "cpu": 45,
    "ram": 60
},
{
    "hostname": "cp2",
    "ip": "10.0.0.2",
    "cpu": 80,
    "ram": 50
},
{
    "hostname": "cp3",
    "ip": "10.0.0.3",
    "cpu": 30,
    "ram": 45
},
{
    "hostname": "cp4",
    "ip": "10.0.0.4",
    "cpu": 80,
    "ram": 90
},
]

def check_server(server):
    cpu= server["cpu"]
    ram= server["ram"]

    if cpu >=90 or ram>=90:
         return "critical"
    elif cpu>=70 or ram >=70:
       return "warning"
    else:
       return "healthy"


warning_count=0
critical_count=0
problem_servers=[]

for server in servers:
    hostname = server["hostname"]
    ip=server["ip"]
    cpu = server["cpu"]
    ram = server["ram"]
    status=check_server(server)

    if status == "critical":
        critical_count+=1
        problem_servers.append(server)
    elif status == "warning":
        warning_count +=1
        problem_servers.append(server)

    print("=============")
    print("server report")
    print("==============")
    print("hostname:", hostname)
    print("ip:", ip)
    print("cpu:", cpu)
    print("ram:", ram)
    print("status:",status)

print("========== Summary ==========")
print("Warning count:", warning_count)
print("Critical count:", critical_count)
print("Problem servers:")
for server in problem_servers:
    print(f"- {server['hostname']} (CPU: {server['cpu']}, RAM: {server['ram']})")