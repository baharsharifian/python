class Server:
    def __init__(self, hostname, ip, cpu,ram):
        self.hostname = hostname
        self.ip = ip
        self.cpu = cpu
        self.ram = ram
    def check_server(self):
        if self.cpu >=90 or self.ram>=90:
             return "critical"
        elif self.cpu>=70 or self.ram >=70:
             return "warning"
        else:
             return "healthy"
    def report(self):

        status = self.check_server()
        print("=============")
        print("server report")
        print("==============")
        print("hostname:", self.hostname)
        print("ip:", self.ip)
        print("cpu:", self.cpu)
        print("ram:", self.ram)
        print("status:", status)


warning_count=0
critical_count=0
problem_servers=[]

cp1 = Server("cp1","10.0.0.1",50,65)
cp2 = Server("cp2","10.0.0.2",80,90)
servers=[cp1,cp2]

for server in servers:
    status = server.check_server()

    if status == "critical":
        critical_count += 1
        problem_servers.append(server)
    elif status == "warning":
        warning_count += 1
        problem_servers.append(server)

    server.report()

print("========== Summary ==========")
print("Warning count:", warning_count)
print("Critical count:", critical_count)
print("Problem servers:")
for server in problem_servers:
    print(f"- hostname:{server.hostname} (CPU: {server.cpu}, RAM: {server.ram})")






