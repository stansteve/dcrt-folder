import os
from pathlib import Path


def get_dirs(path: str) -> list:
    """
    Extract names of all folders inside the local directory
    param p: path to loacal directory
    return: A list containing names
    """
    return [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]


def create_path_name(pri_path: str, yr: list, sec_path: str) -> list:
    """
    Create a list of file paths by joining local directories with year.
    param yr: A list of years
    param pri_path: Local parent path
    param sec_path: Secondary parent path
    return: A path list containing names of directories
    """
    dir_path = []
    for d in get_dirs(pri_path):
        for y in yr:
            full_path = f"{sec_path}/{d}/{y}"
            dir_path.append(full_path)
    return dir_path


def create_dirs(mons: list, p_path: str, yr: list, s_path: str) -> None:
    """
    Create the folders in the remote directory.
    param mons: A list of month
    param yr: A list of years
    param p_path: Local parent path
    param s_path: Secondary parent path
    """
    # TODO: handle where only one month is given
    paths = create_path_name(pri_path=p_path, yr=yr, sec_path=s_path)
    for p in paths:
        for month in mons:
            # dir_path= os.path.join(p, month)
            dir_path = f"{p}/{month}"
            Path(dir_path).mkdir(parents=True, exist_ok=True)


def main():
    local_path = "/home/fiend/Downloads/Work/DCRT/INPUT/TEMPLATE 3"
    secondary_path = "/home/fiend/Downloads/Work/DCRT/INPUT/TEMPLATE 4"
    years = ['2022', '2023']
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

    print(f"Creating folders")
    create_dirs(mons=months, yr=years, p_path=local_path, s_path=secondary_path)
    print("Process has finished!")


if __name__ == '__main__':
    main()
