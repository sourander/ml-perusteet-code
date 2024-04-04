import requests
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Dataset:
    name: str
    remote: str
    local: str


datasets = [
    Dataset(
        name="MongoDB Injection",
        remote="https://raw.githubusercontent.com/capnmav77/No-SQL_Gen/master/No-SqlDataset.json",
        local="data/nosql/nosql.json",
    ),
]


def download_dataset(d: Dataset):
    response = requests.get(d.remote)
    if response.ok:

        # Create the containing directories
        Path(d.local).parent.mkdir(parents=True, exist_ok=True)

        # Write the file
        with open(d.local, "wb") as file:
            file.write(response.content)
            print(f"Dataset downloaded: {d.name}")
    else:
        print(f"Failed to download dataset {d.name} from {d.remote}")
        exit(1)


if __name__ == "__main__":

    for d in datasets:
        download_dataset(d)
