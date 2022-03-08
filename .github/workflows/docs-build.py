import os
root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..")
print(root_path)
f = open(os.path.join(root_path, "test.txt"), "w")
f.write("This is a test")
f.close
