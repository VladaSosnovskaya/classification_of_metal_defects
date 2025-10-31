import os
import shutil
import random

root_dir = "NEU2/peeling_origs"
classes = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d)) and d not in ["train", "val", "test"]]

splits = ["train", "val", "test"]
for split in splits:
    split_path = os.path.join(root_dir, split)
    os.makedirs(split_path, exist_ok=True)
    for class_name in classes:
        os.makedirs(os.path.join(split_path, class_name), exist_ok=True)

for class_name in classes:
    class_path = os.path.join(root_dir, class_name)
    files = [f for f in os.listdir(class_path) if os.path.isfile(os.path.join(class_path, f))]

    random.shuffle(files)
    
    total = len(files)
    train_end = int(0.8 * total)
    val_end = train_end + int(0.1 * total)
    
    train_files = files[:train_end]
    val_files = files[train_end:val_end]
    test_files = files[val_end:]
    
    print(f"Класс: {class_name}. Train: {len(train_files)}, Val: {len(val_files)}, Test: {len(test_files)}")
    
    def move_files(file_list, target_split):
        target_dir = os.path.join(root_dir, target_split, class_name)
        for f in file_list:
            src = os.path.join(class_path, f)
            dst = os.path.join(target_dir, f)
            shutil.move(src, dst)
    
    move_files(train_files, "train")
    move_files(val_files, "val")
    move_files(test_files, "test")


for class_name in classes:
    class_path = os.path.join(root_dir, class_name)
    if os.path.exists(class_path) and len(os.listdir(class_path)) == 0:
        os.rmdir(class_path)

print("Готово! Данные разделены и структура восстановлена: 80% train, 10% val, 10% test")