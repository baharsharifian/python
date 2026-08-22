servers =["cp1","cp2","cp3","cp2-new"]
server_name = input("server name:").lower()
if server_name in  servers :
        print ("Server Found")
else:
        print ("server not found")