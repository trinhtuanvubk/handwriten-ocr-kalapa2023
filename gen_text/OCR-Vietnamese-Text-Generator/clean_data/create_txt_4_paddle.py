import os
from tqdm import tqdm

def save_dict2txt(results_dict, out_path):
    with open(out_path, "a", encoding="utf-8") as outfile:  # Use "a" mode for appending
        for key, value in results_dict.items():
            line = f"{key}\t{value}\n"
            outfile.write(line)
    print("=======================================append dict done=====================================================")
    return "append dict done"

forlder_txt = "../trdg/train/labels"

result_image_list = {}

for path in tqdm(os.listdir(forlder_txt)):
    label_path = os.path.join(forlder_txt, path)
    name_file = os.path.join("data_500k_hwt_synthetic", path[:-4] + ".jpg")
    with open(label_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[0]
    result_image_list[name_file] = lines
    # break
save_dict2txt(result_image_list, "data_hwt_500k_syn.txt")

