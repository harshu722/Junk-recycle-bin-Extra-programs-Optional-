name = "Jon Doe"
length = len(name)
if length > 5:
    print(f"Name has{length} charactors")
if (length := len(name)) > 5:
    print(f"Name has {length} charactors")
