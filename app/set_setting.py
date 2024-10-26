import json

setting = {
    'folders': {
        'folder1': './folder1',
        'Icon': 'Icon',
        'phone': r'C:\TuongLC\Other\Picture'
    }
}


with open("setting.json", "wt", encoding='utf-8') as fin:
    json.dump(setting, fin, ensure_ascii=False, indent=4)
