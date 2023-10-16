import pandas as pd
import random
def read_excel(filepath, outpath):
    data = pd.read_excel(filepath)
    print(data)
    alphabet = "abcdeg"
    with open(outpath, "a+") as f:
        for idx, row in data.iterrows():
            try:
                pre = random.choice(["Ngõ", "Đường", "Số", "Tổ", "Ngách", "Khu"])
                ran_num = random.randint(1, 99)
                ran_alphabet = random.choice(alphabet).upper()
                city = row["Tỉnh Thành Phố"].replace("Thành phố ", "TP").replace("Tỉnh ", "")
                district = row["Quận Huyện"].replace("Huyện ", "").replace("Quận ", "")
                vilage = row["Phường Xã"].replace("Phường ", "").replace("Xã ", "")
                ran_address = f"{pre} {ran_num}{ran_alphabet} {vilage} {district} {city}"
                print(ran_address)
                f.write(ran_address + "\n")
                # print(row["Tỉnh Thành Phố"])
                # print(row["Quận Huyện"])
                # print(row["Phường Xã"])
            except:
                print("ignore")
        f.close()



if __name__=="__main__":
    path = "./address_list.xls"
    outpath = "./gen_address.txt"
    read_excel(path, outpath)