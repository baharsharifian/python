servers=[("cp1" , "running"),
         ("cp2" , "stopped"),
         ("cp3" , "running"),
         ("cp4" , "stopped")]


for hostname,status in servers:
    if status=="running":
        print(hostname);
