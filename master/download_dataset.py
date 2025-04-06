from .utils import *
from kaggle.api.kaggle_api_extended import KaggleApi


custom_dir, force_update = "C:\\Users\\MesterComputer\\Desktop\\dataset\\Venv\\datasets", False


@dataset_decorator(custom_dir)
def dataset_downloader(force_update: bool, version_path: str) -> str:

    dataset_name = "suvroo/ai-for-elderly-care-and-support"

    json_creator()
    
    api = KaggleApi()
    api.authenticate() 
    if force_update:
        print(f"📥 Dar hal download dataset {version_path}")
        api.dataset_download_files(dataset_name, path=version_path, unzip=True)
        os.remove(rf"{version_path}\daily_reminder.csv")
        os.remove(rf"{version_path}\safety_monitoring.csv")
        print("✅ Dataset ba movafaghiyat nasb shod!")

    return version_path