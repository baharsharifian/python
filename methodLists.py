servers=[]
count =int(input("count of servers:"))

for i in range((count)):
    servers.append(input("server name:"))

print ("=======MENU=======")

for i in range(len(servers)) :
 ##print (f"{}servername i.{servers[i]})
 print(f"{i + 1}. {servers[i]}")
