def get_img_id(response_json_dic):
    # 输入一个字典，获取其中的task_id这一数据
    if len(response_json_dic['result']) == 0:
        return 0
    task_id = response_json_dic['result']['task_id']
    # print(task_id)
    return task_id