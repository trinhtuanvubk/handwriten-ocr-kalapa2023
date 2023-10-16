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
        # f.close()



if __name__=="__main__":
    path = "./address_list.xls"
    outpath = "./gen_address.txt"
    read_excel(path, outpath)