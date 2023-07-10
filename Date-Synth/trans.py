import json

# Đọc file COCO JSON
with open('annotations.json', 'r') as f:
    data = json.load(f)

# Lặp qua từng hình ảnh trong file
for image_name, image_data in data.items():
    # Tạo tên file txt tương ứng
    txt_file_name = image_name.replace('.jpg', '.txt')
    
    # Mở file txt để ghi
    with open(txt_file_name, 'w') as txt_file:
        string = ''
        # Lặp qua từng annotation trong hình ảnh
        for annotation in image_data['ann']:
            string += annotation['transcription']
            string += '/'        
        n = len(string)
        txt_file.write(string[:n-1])