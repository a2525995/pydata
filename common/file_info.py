# -*- coding: utf-8 -*-

import codecs
import csv
import hashlib
import json
import os
import time

from common import InitCommon
itc = InitCommon()

_FILE_SLIM = (100 * 1024 * 1024)  # 100MB
root_path = os.getcwd() + "/data_output/"
host_url = itc.download_url


def file_info(file_path):
    global file_mime, file_extension
    call_times = 0
    hmd5 = hashlib.md5()
    fp = open(file_path, "rb")
    f_size = os.stat(file_path).st_size
    if f_size > _FILE_SLIM:
        while f_size > _FILE_SLIM:
            if (f_size > 0) and (f_size <= _FILE_SLIM):
                hmd5.update(fp.read())
    else:
        hmd5.update(fp.read())
    md5 = hmd5.hexdigest()
    file_size = os.path.getsize(file_path)
    file_name = os.path.basename(file_path)
    if os.path.splitext(file_path)[1] == ".csv":
        file_mime = "text/csv"
        file_extension = "csv"
    file_infos = {"filename": file_name, "md5": md5, "filesize": file_size, "mime": file_mime,
                  "extension": file_extension, "structfile": file_path}
    return json.dumps(file_infos)


def get_file_contents(file_paths):
    file_inf = []
    for i in file_paths:
        file_data = []
        file_name = i['filename']
        file_path = i['structfile']
        with open(file_path, 'r+', encoding='UTF-8') as file:
            for line in file:
                if len(file_data) <= 21:
                    file_data.append(line)
                else:
                    break
        data = {'filename': file_name, 'file_content': file_data}
        file_inf.append(data)
    return file_inf


def get_file_info(file_path_list):
    file_data = []
    for file_path in file_path_list:
        importfile_info = file_info(file_path)
        file_data.append(json.loads(importfile_info))
    data_pack = {"structfile": file_data, "unstructfile": []}
    return data_pack


def make_tar(csv_dict, time_str):
    file_list = set()
    with_header = set()
    file_path_list = []
    for key in csv_dict:
        path = root_path + time_str + "_" + key + ".csv"
        path_prefix = time_str + "_" + key
        event_file = path_prefix + ".csv"
        events_file = key + ".csv"
        if not os.path.exists(root_path):
            mkdir = "mkdir data_output;"
            os.system(mkdir)
        file_path_list.append(root_path + time_str + "_" + events_file)
        file_list.add(event_file)

        f = codecs.open(path, "a", "utf-8")
        cont_wirter = csv.writer(f)
        col_list = csv_dict[key]
        if key not in with_header:
            cont_wirter.writerow(col_list[0])
            with_header.add(key)
        for i in range(1, len(col_list)):
            cont_wirter.writerow(col_list[i])
        f.close()
        # spilt file
        # splitFile(path, path_prefix)
        files = " ".join(file_list)
        command = "cd data_output; tar -cvf " + time_str + ".tar " + files
        os.system(command)
    file_url = host_url + '/tool/download/' + time_str + ".tar"
    file_data = {"file_url": file_url, "file_path_list": file_path_list}
    return file_data
