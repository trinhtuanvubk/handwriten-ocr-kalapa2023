import os

# TO READ

# for file in os.listdir("./kalapa"):
#     file_path = os.path.join("./kalapa", file)
#     with open('kalapa_text.txt', 'a+') as k:
#         with open(file_path, 'r') as f:
#             line = f.readline()
#             k.write(line + "\n")

# TO CHECK

with open("./kalapa_checked50.txt", "a+") as o:
    with open("./kalapa_text.txt", 'r') as f:
        data = f.readlines()
        for line in data:
            if len(line[:-2]) > 50:
                print(line)
                line = " ".join(line[:50].split(" ")[:-1])
                line += "\n"
                print(line)
            o.write(line)

