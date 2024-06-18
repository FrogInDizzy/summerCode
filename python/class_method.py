class Employee:
    __class_version = "v1.0"

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def cls_ver_get(cls):
        return cls.__class_version
    
    @classmethod
    def cls_ver_set(cls, new_version):
        cls.__class_version = new_version

print(Employee.cls_ver_get())
Employee.cls_ver_set("v1.1")
print(Employee.cls_ver_get())