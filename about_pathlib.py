from pathlib import Path

# Path("C:\\Program Files\\Microsoft")
# Path(r"C:\Program Files\Microsoft")
# path = Path()/Path("sample")
# print(path)
# print(Path.home())

# path = Path()/Path("sample/__init__.py")
# print(path.exists())
# print(path.is_file())
# print(path.is_dir())
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)
# path = path.with_name("fileee.txt")
# print(path)
# path = Path()/Path("sample").rename('target')
# path = Path('something')
# path.mkdir()
# path.rmdir()
# path = Path('target/azar_17.py')
# for p in path.iterdir():
#     print(p)
# paths = [p for p in path.iterdir() if p.is_dir()]
# print(paths)
# paths = [p for p in path.rglob("*.py")]
# print(paths)
# print(path.read_text())
# print(path.read_bytes())

# path.write_text("....")

# copy files:
# source = Path("target/__init__.py")
# dest = Path()/"some.py"
# dest.write_text(source.read_text())

# import shutil
# source = Path("target/__init__.py")
# dest = Path()/"sw.py"
# shutil.copy(source, dest)

# zip file
from zipfile import ZipFile
# with ZipFile("temp.zip") as zip:
#     files = zip.namelist()
#     for path in files:
#         file = Path(path)
#         print(file.read_bytes())
#         print('--------------------------------------')

with ZipFile("temp.zip") as zip:
    files = zip.namelist()
    print(files)
    info = zip.getinfo('f.txt')
    info = zip.getinfo('file.txt')
    print(info)
    zip.extractall()
