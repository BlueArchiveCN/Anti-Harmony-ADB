import subprocess
from pathlib import Path

# 检查资源文件夹是否存在
assets_path = 'AssetBundls'
assert Path(assets_path).is_dir(), FileNotFoundError(f'资源文件夹{assets_path}不存在，请考虑重新获取本项目')

# 检查adb是否存在且可用
# 首先检查是否有已经开放的adb端口
cmd = ['adb', 'devices']
devices_list = []
subproc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, encoding='utf8')
out = subproc.stdout.readlines()
for line in out:
    if line.endswith('\tdevice'):
        devices_list.append(line.split('\t')[0])

# 如果是空的(常见于模拟器), 尝试planb: 让用户自己输入端口, 然后用adb connect直接连接
if not devices_list:
    print('没有已经开放的adb端口, 请手动输入端口. 请注意, 手动输入的. \n'
          '如果是真机请检查是否已经开启了adb调试, 直接按回车将退出程序.')
    print('如果是本地模拟器请输入端口号, 例如16543(常见于mumu模拟器12)')
    print('如果是远程adb设备请输入ip:端口号, 例如192.168.123.123:7555')
    _input = input()
    if not _input:
        exit()
    if ':' in _input:
        ip, port = _input.split(':')
    else:
        port = _input
    if int(port) > 65535 or int(port) < 0:
        raise ValueError('端口号不合规')
    try:
        ip = ip
    except:
        ip = '127.0.0.1'
    cmd = ['adb', 'connect', f'{ip}:{port}']
    subproc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, encoding='utf8')
    assert 'connected' not in subproc.stdout.readlines(), RuntimeError(f'连接失败, 请检查设备是否开启了adb调试')
    devices_list.append(f'{ip}:{port}')
print(f'已经开放的adb端口有{devices_list}')

# 长度大于1, 说明有多个设备, 让用户选择
if len(devices_list) > 1:
    print('有多个设备, 请选择其中一个, 输入序号即可, 例如输入1')
    for i, d in enumerate(devices_list):
        print(f'{i + 1}. {d}')
    device = [devices_list[int(input()) - 1]]
else:
    device = devices_list.pop()

# 获得文件列表
address = '/storage/emulated/0/Android/data/com.RoamingStar.BlueArchive/files/AssetBundls/'
bundle_list = Path(assets_path).glob('*.bundle')

# 执行替换
for f in bundle_list:
    cmd = ['adb', '-s', device, 'push', f, address]
    subproc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, encoding='utf8')
    # 如果返回中没有‘pushed’则说明传输失败
    assert 'not found' in subproc.stdout.readlines(), RuntimeError(f'文件{f}传输失败, 设备可能不存在')
    assert 'pushed' not in subproc.stdout.readlines(), RuntimeError(f'文件{f}传输失败')
    print(f"文件{f}替换成功")
print("替换成功")
# by Ayin/李某人
# change by 360NENZ
# 2023-8-17 17:22:23 change by lucosin
