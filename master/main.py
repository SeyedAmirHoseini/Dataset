from .download_dataset import dataset_downloader

def main():

    force_update = input("mikhay version jadid besazi az dataset hat? (Y/n): ").strip().lower() == 'y'

    dataset_downloader(force_update)



if __name__ == "__main__":
    main()