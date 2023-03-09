from shiphelm.helmdocker import helmdocker

hd = helmdocker() # create an instance of helmdocker
container_list = hd.get_running_containers() # call the method on the instance
print(container_list)