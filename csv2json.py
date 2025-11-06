import csv
import json

## 读取csv文件，转换为json格式
def csv_to_list(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        return [[float(x) for x in row] for row in reader]

filename = '害怕.csv'  # 替换为你的CSV文件路径
data = csv_to_list(filename)
print(data)

def save_to_file(data, filename):
    expression = filename.split(".")[0]
    expression_data = {
    expression: data
}
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            # 方法1：使用自定义格式化
            f.write('{\n')
            f.write(f'  "{expression}": [\n')
            
            for i, row in enumerate(data):
                # 每个子数组写在一行
                row_json = json.dumps(row, ensure_ascii=False, separators=(',', ':'))
                print(row_json)
                if i < len(data) - 1:
                    f.write(f'    {row_json},\n')
                else:
                    f.write(f'    {row_json}\n')
            
            f.write('  ]\n')
            f.write('}\n')
        
        print(f"数据已保存到: {filename}")
    except Exception as e:
        print(f"保存文件时出错: {e}")

save_to_file(data, filename='害怕.json')  # 替换为你想要保存的JSON文件名

