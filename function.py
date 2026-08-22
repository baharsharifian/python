while True:
    try:
        cpu=int(input("cpu:"))
        ram=int(input("ram:"))

        if (cpu <0 or cpu > 100) or (ram<0 or ram >100):
            print("cpu or ram must be between 0 and 100")
        else:
            break
    except ValueError:
        print("cpu or ram not correct")

hostname=input("hostname:")
def check_server(cpu,ram):

    if cpu >=90 or ram>=90:
        status="critical"
    elif cpu>=70 or ram >=70:
        status ="warning"
    else:
        status= "healthy"

    return status

status=check_server(cpu,ram)
print("=============")
print("server report")
print("==============")
print("hostname:", hostname)
print("cpu:", cpu)
print("ram:", ram)

print("status:",status)