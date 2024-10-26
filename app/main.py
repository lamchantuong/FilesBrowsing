from flask import Flask, render_template, send_from_directory, url_for, request
import os
import json

app = Flask(__name__)

ICON_PATH = r'Icon'
DEFAULT_FOLDER_IMAGE = 'folder.webp'
DEFAULT_DOCUMENT_IMAGE = 'document.png'
with open('setting.json', 'r') as f:
    setting = json.load(f)

folders = setting.get('folders')

def get_subdirs_files(directory):
    # Lấy danh sách các tệp trong thư mục
    return os.listdir(directory)

def get_directory_file_image(icon_directory, extensions):
    # Tìm hình ảnh tương ứng với các định dạng tệp
    for ext in extensions:
        image_path = os.path.join(icon_directory, ext)
        if os.path.exists(image_path):
            return image_path
    return os.path.join(icon_directory, DEFAULT_FOLDER_IMAGE)

def get_image_mapping(subdir_files):
    # Tạo từ điển ánh xạ các tệp với hình ảnh tương ứng
    ext_to_image = {}
    for file in subdir_files:
        filename, ext = os.path.splitext(file)
        if not ext:
            ext_to_image[file] = DEFAULT_FOLDER_IMAGE
        else:
            for img_ext in ['.jpg', '.png', '.webp']:
                img_file = f"{ext[1:]}{img_ext}"
                if os.path.exists(os.path.join(os.getcwd(), ICON_PATH, img_file)):
                    ext_to_image[file] = img_file
                    break
            else:
                ext_to_image[file] = DEFAULT_DOCUMENT_IMAGE
    return ext_to_image

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<root_path>')
@app.route('/<root_path>/<path:sub_path>')
def index(root_path, sub_path=''):
    if root_path in folders:
        full_path = os.path.join(folders.get(root_path), sub_path)
        if os.path.isdir(full_path):            
            subdir_files = get_subdirs_files(full_path)
            subdir_files = [sub_path + ('/' if sub_path and file else '') + file for file in subdir_files]
            image_mapping = get_image_mapping(subdir_files)  # Không thay đổi ở đây
            return render_template('index.html', root_path=root_path, subdirectories=subdir_files, images=image_mapping, icon_path=ICON_PATH)
        
        if os.path.isfile(full_path):       
            return send_from_directory(folders.get(root_path), sub_path)
    else:
        return 'Not a registered'
    

if __name__ == '__main__':
    print('Starting server...')
    app.run(host='0.0.0.0', port=80, debug=True)
