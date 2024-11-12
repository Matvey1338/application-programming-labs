from icrawler.builtin import GoogleImageCrawler

base_dir = 'images'


def download_images(keyword: str, max_num: int = 50, save_dir=base_dir) -> None:
    """
    Func for downloading images

    parameterS:
    - keyword (str): key search for Google Images.
    - max_num (int): max num of downloading images.
    - save_dir (str): directory for saving images.
    """
    google_crawler = GoogleImageCrawler(
        storage={'root_dir': save_dir},
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4
    )
    google_crawler.crawl(keyword=keyword, max_num=max_num)

