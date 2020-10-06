from zipfile import ZipFile
from pathlib import Path
import requests


def download(url: str, save_path: Path, save_name=None, chunk_size=1024) -> Path:
    if save_name is None:
        save_name = Path(url.split('/')[-1]).resolve()
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with save_path.open("wb") as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
    return save_name.resolve()


def extract_zip(zip_path: Path, folder_path: Path, members=None, pwd=None) -> Path:
    with ZipFile(zip_path) as zf:
        zf.extractall(folder_path, pwd=pwd, members=members)
    return zip_path.resolve()


def create_zip(folder_path: Path, zip_path: Path) -> Path:
    with ZipFile(zip_path) as zf:
        for child in folder_path.glob("**/*"):
            zf.write(child.relative_to(folder_path))
        return zip_path
