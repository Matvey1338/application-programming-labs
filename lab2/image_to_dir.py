from icrawler.builtin import GoogleImageCrawler

base_dir = "images"


def download_images(keyword: str, max_num: int, save_dir=base_dir) -> str:
    """
    Func for downloading images

    parameterS:
    - keyword (str): key search for Google Images.
    - max_num (int): max num of downloading images.
    - save_dir (str): directory for saving images.
    """
    google_crawler = GoogleImageCrawler(storage={'root_dir': save_dir})
    google_crawler.crawl(keyword=keyword, max_num=max_num)
    return save_dir
