import os
import asyncio
import patoolib

async def extract_files(folder_path):
    file_list = os.listdir(folder_path)
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        
        if patoolib.is_archive(file_path):
            patoolib.extract_archive(file_path, outdir=folder_path)

def read_file(file_path) -> str:
    with open(file_path, 'r', encoding="utf-8") as file:
        file_content = file.read()
    return file_content

def write_file(file_path, content) -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(content)

# Test
async def test():
    test_dir = './logs/homework/Python - S1'
    await extract_files(test_dir)
    py_files = []
    for root, dirs, files in os.walk(test_dir):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))
    for file in py_files:
        print(read_file(file))
if __name__ == "__main__":
    asyncio.run(test())