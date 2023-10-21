python3 run.py \
--count 30000 \
--language vi \
--format 48 \
--name_format 2 \
--current_idx 0 \
--output_dir ./out/images_hw_kalapa/ \
--label_dir ./out/labels_hw_kalapa/ \
--font_dir ./fonts/HWT \
--input_file ./texts/special_domain/kalapa_checked.txt \
--background 3 \
--image_dir ./images/ \
--margins "2,10,2,2" \
--skew_angle 1 \
--random_skew \
--thread_count 8 \
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