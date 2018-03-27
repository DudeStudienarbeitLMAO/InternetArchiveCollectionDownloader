import getpass
import internetarchive
from internetarchive import ArchiveSession
from internetarchive import config
from tqdm import tqdm

if __name__ == '__main__':
    username = input('Email: ')
    password = getpass.getpass()
    config = config.get_auth_config(username, password)
    session = ArchiveSession(config)
    wanted_collection = input('Enter collection key to download: ')
    collection = internetarchive.Search(session, 'collection:{0}'.format(wanted_collection))
    print('Enter File Types seperated by ,  -- no spaces')
    print('Leave blank for all')
    print('Examples: MPEG4,Archive BitTorrent,Metadata,Thumbnail')
    filetypes = input('Decide now: ').split(',')
    print(filetypes)
    print("Found {0} items in collection. Downloading.".format(str(len(collection))))
    for item in tqdm(collection.iter_as_items()):
        for file in item.get_files():
            if filetypes[0] == '' or file.format in filetypes:
                file.download(file_path='{0}/{1}'.format(item.identifier, file.name), ignore_existing=False,
                              checksum=True, retries=3)
            else:
                continue