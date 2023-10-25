import pandas as pd
import random
def read_excel(filepath, outpath):
    data = pd.read_excel(filepath)
    print(data)
    cols = ["Tỉnh Thành Phố", "Quận Huyện", "Phường Xã"]
    number = "12345678"
    alphabet = "abcdeg"
    old_val = ""
    with open(outpath, "a+") as f:
        # try:
        #     for col in cols:
        #         old_val = ""
        #         # print(col)
        #         print(data[col])
        #         for val in data[col]:
        #             print(val)
        #             if val!=old_val:
        #                 f.write(val+"\n")
        #                 old_val = val
        # except:
        #     print("ignore")

        
        for idx, row in data.iterrows():
            try:
                pre = random.choice(["Ngõ", "Đường", "Số", "Tổ", "Ngách", "Khu", "Thôn", "Ấp", "Xóm"])
                # pre = random.choice(["số", "ngách", "ngõ", "hẻm", "thôn", "ấp", "tổ", "xóm", "khu"])
                all_pre = random.choice(["Ngõ", "Đường", "Số", "Tổ", "Ngách", "Khu", "Thôn", "Ấp", "Xóm", "số", "ngách", "ngõ", "hẻm", "thôn", "ấp", "tổ", "xóm", "khu"])
                ran_num = random.randint(1, 999)
                ran_num2 = random.randint(1, 999)
                ran_num3 = random.randint(1, 999)
                ran_alphabet = random.choice(["A", "B", "C", "D", "E", "G", "", "", "", ""])
                
                # ran_alphabet = random.choice(alphabet).upper()
                # city = row["Tỉnh Thành Phố"]
                # district = row["Quận Huyện"]
                # vilage = row["Phường Xã"]

                # city = row["Tỉnh Thành Phố"].replace("Thành phố ", "TP ").replace("Tỉnh ", "")
                # district = row["Quận Huyện"].replace("Huyện ", "").replace("Quận ", "")
                # vilage = row["Phường Xã"].replace("Phường ", "").replace("Xã ", "").replace("Thị trấn ", "")

                city = row["Tỉnh Thành Phố"].replace("Thành phố ", "thành phố  ").replace("Tỉnh ", "tỉnh ")
                district = row["Quận Huyện"].replace("Huyện ", "huyện ").replace("Quận ", "quận ")
                vilage = row["Phường Xã"].replace("Phường ", "phường ").replace("Xã ", "xã ").replace("Thị Trấn ", "thị trấn ").replace("Thị trấn ", "thị trấn ")
                ran_address = f"{all_pre} {ran_num}/{ran_num2}/{ran_num3} {vilage}, {district}, {city}"
                print(ran_address)
                random_write = random.randint(0,2)
                # if random_write:
                #     f.write(ran_address + "\n")
                f.write(ran_address + '\n')
            except:
                print("ignore")
            
        # f.close()

def check_length(path):
    with open('checked_address50.txt', 'a+') as f: 
        with open(path, 'r') as f1:
            data = f1.readlines()
            for line in data:
            #     if len(i) < 55:
            #         f.write(i)
            #     else:
            #         print(i)
                if (len(line[:-2]) > 50) and (len(line[:-2]) < 60):
                    print(line)
                    line = " ".join(line[:50].split(" ")[:-1])
                    line += "\n"
                    print(line)
                f.write(line)

def random_test(path):
    with open('eval_address.txt', "a+") as f:
        with open(path, 'r') as f1:
            data = f1.readlines()
            choice  = random.sample(data, 15000)
            for i in choice:
                f.write(i)


if __name__=="__main__":
    path = "./address_list.xls"
    outpath = "./normal_address.txt"
    read_excel(path, outpath)
    # check_length(outpath)
    # random_test(outpath)