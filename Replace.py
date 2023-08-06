from ast import Name
import os
from token import NAME
os.system('adb devices')
print("请输入你得到序列号就是xxxx devices中xxxxx\n如果有多个请任选其一如果发现反和谐失败请输入另一个")
devices = input()
address = '/storage/emulated/0/Android/data/com.RoamingStar.BlueArchive/files/AssetBundls/'
Name = ["assets-_mx-spinecharacters-asuna_spr-_mxdependency-2023-05-30_assets_all_a3463cbb70598abab36189264165fdda.bundle", "assets-_mx-spinecharacters-eimi_spr-_mxdependency-2023-05-30_assets_all_58e8761e4dff1a7e599ae33a28362e80.bundle", "assets-_mx-spinecharacters-hibiki_spr-_mxdependency-2023-05-30_assets_all_cc942ac0a6e9ad60b92514e07764096d.bundle", "assets-_mx-spinecharacters-hina_spr-_mxdependency-2023-05-30_assets_all_406495c040bdefe4a8fa31df35501f47.bundle", "assets-_mx-spinecharacters-kotori_spr-_mxdependency-2023-05-30_assets_all_313788f05ebe6d09ab1a6b4434a53f5f.bundle", "assets-_mx-spinecharacters-shimiko_spr-_mxdependency-2023-05-30_assets_all_bc785424493fb9fd31a9ef8292995175.bundle", "assets-_mx-spinecharacters-shiroko_spr-_mxdependency-2023-05-30_assets_all_83004927ab3f8e7843ee72f26887dc36.bundle", "assets-_mx-spinecharacters-shun_spr-_mxdependency-2023-05-30_assets_all_8204ae231ade61c1df00f305eefb42f8.bundle", "assets-_mx-spinecharacters-tsubaki_spr-_mxdependency-2023-05-30_assets_all_b7fe865c46d111737524e451b5d2ac11.bundle", "assets-_mx-spinelobbies-eimi_home-_mxdependency-2023-05-30_assets_all_858cd925d9c85b1ece17b8fdf1380a18.bundle", "assets-_mx-spinelobbies-shun_home-_mxdependency-2023-05-30_assets_all_fd1451e4fc242ef36e47dcfab6fc25e4.bundle", "prologdepengroup-assets-_mx-spinecharacters-hasumi_spr-_mxprolog-2023-05-30_assets_all_b4f65f56b4a98b1bcb7f11b5d37cf786.bundle"]
os.chdir('AssetBundls')
for i in range(0, len(Name)):
    os.system(f'adb -s {devices} push {Name[i]} {address}')
print("替换成功")
#by Ayin/李某人
#change by 360NENZ
