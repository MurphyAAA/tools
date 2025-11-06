一些常用工具
## 目录

### 1. concate_csv.py
**文件夹下多个csv拼接为一个csv文件，用于合并数据集**

```python
    concatenate_csv_files(data_path, output_file)
```

### 2. interpolation.py
**直接对list计算插值**

```python
    import json
    from custom_json_format import format_dict
    
    file_name = "xxx.json"
    output_file = 'pxxx.json'
    with open(file_name, 'r', encoding='UTF-8') as f:
        expression = json.load(f)

    res_frames = {}
    exp_list = ['微笑', '跳舞', '开心', '点头同意', '调皮', '享受', '生气', '惊讶', '震惊', '惊喜', '难过']
    # 遍历json所有表情，分别进行插值
    for exp_name in exp_list:
        target_time = 5000 # ms
        flash_time = 30 # ms
        # 根据时间计算要插值多少个
        target_frame_count = target_time // flash_time 
        # 如果当前的帧数已经大于默认总时间5s，则时间*2
        while len(expression[exp_name]) > target_frame_count:
            target_frame_count *= 2
        # 进行插值
        frame = global_bezier_interpolation(expression[exp_name], target_frame_count)
        # 插值结果保存回字典，之后写入json文件
        res_frames[exp_name] = frame.copy()
```

### 3. custom_json_format.py 
**自定义json输出的格式**

```python
    with open(output_file, 'w', encoding='utf-8') as f:
        # json.dump(res_frames, f, ensure_ascii=False, indent=4)
        f.write(format_dict(res_frames))
```

### 4. json2csv.py
**json文件转为csv**


### 5. csv2json.py
**csv文件转为json**

