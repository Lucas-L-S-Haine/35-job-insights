import csv
from functools import lru_cache


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    file = open(path, mode="r")
    jobs_csv = csv.DictReader(file)
    jobs_list = []
    for job in jobs_csv:
        jobs_list.append(job)
    return jobs_list
    file.close()
