import os
import shutil

source_dir = 'NEU2/old_train'
output_dir = 'NEU2/train'

os.makedirs(output_dir, exist_ok=True)

classes = ["Crazing", "Inclusion", "Patches", "Pitted", "Rolled", "Scratches"] 
for c in classes:
    source_class_dir = os.path.join(source_dir, c)

    for filename in os.listdir(source_class_dir):
        filepath = os.path.join(source_class_dir, filename)
        output_class_dir = os.path.join(output_dir, c)
        os.makedirs(output_class_dir, exist_ok=True)

        if os.path.isfile(filepath) and filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            if "_augmented" not in filename:
                shutil.copy2(filepath, output_class_dir) # копия оригинала
                print(f"Скопировано: {filename}")