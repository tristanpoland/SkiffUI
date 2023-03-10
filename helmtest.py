from shiphelm.helmdocker import helmdocker

hd = helmdocker() # create an instance of helmdocker
container_list = hd.get_running_containers() # call the method on the instance
print(container_list)
w=0

print("Preparing new server...")
while w<49:
    hd.run_container(image="docker/getting-started", detach=1)
    w=w+1

print("Your server is up and ready of connection!")