def dicotomia(self,array,data):
    if len(array)==0:
        return False
    array.sort()
    mid = len(array)//2
    if array[mid]==data:
        return True
    return self.dicotomia(array[mid+1:],data)if data>array[mid]else\
        self.dicotomia(array[:mid],data)