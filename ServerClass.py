class Server:
    def __init__(self, hostname, ip, cpu,ram):
        self.hostname = hostname
        self.ip = ip
        self.cpu = cpu
        self.ram = ram


def check_server(Server):

    if server.cpu >=90 or ram>=90:
         return "critical"
    elif cpu>=70 or ram >=70:
       return "warning"
    else:
       return "healthy"


warning_count=0
critical_count=0
problem_servers=[]

for server in Server:
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


cp1 = Server("cp1","10.0.0.1",50,65)
cp2 = Server("cp2","10.0.0.2",80,90)

print(cp1.hostname)
print(cp2.hostname)
print(cp1.cpu)
