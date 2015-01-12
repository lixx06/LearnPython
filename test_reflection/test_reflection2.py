
module = __import__("person")
theObj = getattr(module, "Person")()
print theObj.getName()