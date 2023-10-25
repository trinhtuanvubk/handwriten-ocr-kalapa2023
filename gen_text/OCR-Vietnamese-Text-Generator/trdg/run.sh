python3 run.py \
--count 50000 \
--language vi \
--format 48 \
--name_format 2 \
--current_idx 0 \
--output_dir ./out/images_hw_test/ \
--label_dir ./out/labels_hw_test/ \
--font_dir ./fonts/HWT/ \
--input_file ./texts/special_domain/eval_address.txt \
--background 3 \
--image_dir ./images/ \
--margins "3,10,3,3" \
--thread_count 16 \
# --text_color  "#153387" \
# --case capwords
# --text_color  "#FF3333" \
# --text_color  "#153387" \
# --case upper \
# --text_color  "#153387" \
# --case upper
# --text_color  "#FF3333" \
# --case upper
# --text_color  "#153387" \

# --output_bboxes 1 


# color: , FF3333, 153387