from dotenv import load_dotenv
import os, json

load_dotenv()

def dataset_decorator(base_path):
    def decorator(func):
        def wrapper(force_update: bool, *args, **kwargs):
            version = 1
            while True:
                folder_name = f"v{version}"
                version_path = os.path.join(base_path, folder_name)

                if not os.path.exists(version_path):
                    os.makedirs(version_path)  
                    break

                if force_update:
                    version += 1
                else:
                    break

            return func(force_update, version_path, *args, **kwargs)
        return wrapper
    return decorator




def json_creator():
    username = os.getenv("KAGGLE_USERNAME")
    key = os.getenv("KAGGLE_KEY")
    
    # ساخت مسیر پیش‌فرض برای kaggle
    kaggle_dir = os.path.join(os.path.expanduser("~"), ".kaggle")
    os.makedirs(kaggle_dir, exist_ok=True)

    # ساخت فایل kaggle.json به صورت خودکار
    kaggle_json_path = os.path.join(kaggle_dir, "kaggle.json")
    with open(kaggle_json_path, "w") as f:
        json.dump({"username": username, "key": key}, f)