import os
import markdown

root_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../.."))
src_path = os.path.join(root_path, "src")
doc_path = os.path.join(root_path, "doc")
tmp_path = os.path.join(root_path, "tmp")

if(os.path.isdir(tmp_path)):
    os.system(f"rm -r {tmp_path}")
if(os.path.isdir(doc_path)):
    os.system(f"rm -r {doc_path}")
os.system(f"cp -r {src_path}/ {tmp_path}/")

for path, subdirs, files in os.walk(tmp_path):
    for name in files:
        if(name.endswith(".md")):
            md_content = open(os.path.join(path, name), "r").read()
            os.remove(os.path.join(path, name))
            pre, ext = os.path.splitext(name)
            file = open(f"{os.path.join(path, pre)}.html", "w")
            file.write(markdown.markdown(md_content))
            file.close()

os.system(f"cp -r {tmp_path}/ {doc_path}/")

os.system(f"rm -r {tmp_path}")
