import requests
import os
import random
import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
from datetime import datetime
from datetime import date
time=datetime.now().strftime("%H:%M:%S%p")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
lam = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#đánh dấu bản quyền
import os, sys, requests
from time import sleep
from pystyle import *
from time import strftime
from datetime import datetime, timedelta
import pywifi
now=datetime.now()
os.system("cls" if os.name == "nt" else "clear")
def check_internet_connection():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Kiểm tra kết nối internet
if check_internet_connection():
    print(f"{luc}Vui Lòng Chờ!!!")
    sleep(0.001)
else:
    print(f"{do}Vui Lòng Kiểm Tra Kết NốI!!!")
    sys.exit()
def get_location_by_ip():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()

        city = data.get("city")
        region = data.get("region")
        country = data.get("country")
        loc = data.get("loc").split(",")
        latitude, longitude = loc if len(loc) == 2 else (None, None)

        return city, region, country, latitude, longitude
    except Exception as e:
        print(f"Lỗi: {e}")
        return None, None, None, None, None
city, region, country, latitude, longitude = get_location_by_ip()
def get_weather():
    try:
        # Lấy thông tin vị trí từ dịch vụ ipinfo.io
        response = requests.get("https://ipinfo.io")
        data = response.json()
        location = data.get("loc").split(",")
        latitude, longitude = location
        # Lấy thông tin thời tiết từ trang web công cộng
        base_url = f"https://wttr.in/{latitude},{longitude}?format=%t"
        response = requests.get(base_url)
        weather_description = response.text.strip()
        return weather_description
    except Exception as e:
        print(f"Lỗi: {e}")
        return None
weather_description = get_weather()
System.Clear()
banner=f"""
\033[1;31m┌═════════════════════════════════════════════════════════════════════════════┐
\033[1;31m██████╗ ███╗  ██╗ █████╗ ███╗   ███╗      ██╗  ██╗███╗  ██╗ █████╗ ███╗   ███╗
\033[1;32m██╔══██╗████╗ ██║██╔══██╗████╗ ████║      ██║  ██║████╗ ██║██╔══██╗████╗ ████║
\033[1;33m██████╦╝██╔██╗██║███████║██╔████╔██║█████╗███████║██╔██╗██║███████║██╔████╔██║
\033[1;34m██╔══██╗██║╚████║██╔══██║██║╚██╔╝██║╚════╝██╔══██║██║╚████║██╔══██║██║╚██╔╝██║
\033[1;36m██████╦╝██║ ╚███║██║  ██║██║ ╚═╝ ██║      ██║  ██║██║ ╚███║██║  ██║██║ ╚═╝ ██║
\033[1;35m╚═════╝ ╚═╝  ╚══╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚═╝╚═╝     ╚═╝  
\033[1;34m┠═════════════════════════════════════════════════════════════════════════════┨
\033[1;34m ➯ Cre : \033[1;31mBảo Nam x Hoàng Nam
\033[1;34m ➯ Nhóm Zalo : \033[1;37mhttps://zalo.me/g/pdsvkf650
\033[1;34m ➯ Facebook Bảo Nam : \033[1;37mhttps://facebook.com/100093509571156
\033[1;34m ➯ Facebook Hoàng Nam : \033[1;37mhttps://facebook.com/nam.nhn131                              
\033[1;34m└═════════════════════════════════════════════════════════════════════════════┘
\033[1;34m ➯ Loại Tool: \033[1;37mGộp Python
\033[1;34m└═════════════════════════════════════════════════════════════════════════════┘
{do} ➩ {trang}Ngày{trang} : {vang}{ngay_hom_nay}{lam} |{trang} Tháng{trang}: {vang}{thang_nay} {lam}| {trang}Năm{trang}: {vang}{nam_}{lam} | {trang}Thời Gian: {vang}{time}
{do} ➩ {trang}Thành Phố : {vang}{city} {lam}|{trang} Khu Vực: {vang}{region} {lam}| {trang} Quốc gia: {vang}{country} {lam}| {trang} Tọa độ: {vang}{latitude}, {longitude} {lam}| {trang} Nhiệt độ: {vang}{weather_description}
"""
for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0)

import requests
from datetime import datetime, timedelta
import os
import random
import string

# Bổ sung: Thiết lập giá trị cho key2
key2 = 'NguyenNam131'
key2_creation_date = datetime.now().strftime("%Y-%m-%d")

def create_or_load_key_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = file.read().strip().split('\n')
            key = data[0]
            key_creation_date = data[1] if len(data) > 1 else datetime.now().strftime("%Y-%m-%d")
    else:
        key = 'namnguyen' + str(int(datetime.now().strftime("%y%m%d%H%M%S")))
        with open(file_path, 'w') as file:
            file.write(f"{key}\n{key_creation_date}")
    return key, key_creation_date

def update_key_file(file_path, new_key, new_key_creation_date):
    with open(file_path, 'w') as file:
        file.write(f"{new_key}\n{new_key_creation_date}")

def check_key_expiry(file_path, days):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = file.read().strip().split('\n')
            key_date_str = data[1] if len(data) > 1 else datetime.now().strftime("%Y-%m-%d")
            key_date = datetime.strptime(key_date_str, "%Y-%m-%d")
            expiration_date = key_date + timedelta(days=days)
            current_date = datetime.now()
            return current_date > expiration_date
    return True

def print_link_message(link):
    print(f'-----------------------------------------------------------------')
    print(f"Link Lấy Key Của Tool !!")
    print(f'Truy Cập Vào Link: {link}')
    print(f'-----------------------------------------------------------------')

def admin_menu():
    print("Menu Admin:")
    print("1. Xem Key")
    print("2. Đổi Key Free")
    print("3. Vào Tool")
    admin_choice = input("Vui Lòng Nhập Số: ")
    return admin_choice

def main():
    # Bước 1: Tạo File
    key_free_file = "Key_Free.txt"
    key_vip_file = "Key_Vip.txt"
    
    # Bước 2: Lấy hoặc tạo key
    key, key_creation_date = create_or_load_key_file(key_free_file)
    
    # Bước 3: Kiểm tra hết hạn key và cập nhật nếu cần
    if check_key_expiry(key_free_file, 3):
        key = 'namnguyen' + str(int(datetime.now().strftime("%y%m%d%H%M%S")))
        update_key_file(key_free_file, key, key_creation_date)
        print("Key Free đã hết hạn, đã cập nhật key mới.")
    
    # Bước 4: In thông báo với link (chỉ khi người dùng chọn Key Free)
    long_url = f"https://keytool.namdev131.repl.co/?key={key}"
    api_token = '3fd7f06f-7545-4a1b-81a3-69d89df0d303'
    url = requests.get(f'https://web1s.com/api?token={api_token}&url={long_url}').json()
    status = url['status']
    link = url['shortenedUrl']

    print("Chọn người dùng:")
    print("1. Người Dùng")
    print("2. Admin")

    choice = input("Nhập số chọn: ")

    if choice == "1":
        print("Đã chọn Người Dùng")
        print("Vui Lòng Chọn Key:")
        print("1. Key Free")
        print("2. Key Vip")
        key_choice = input("Nhập số chọn Key: ")

        if key_choice == "1":
            print_link_message(link)
            api_key = input("Nhập API Key: ")
            if api_key == key:
                print("API Key Đúng!")
                print("Chào Mừng Bạn Đến Với Tool!!")
                update_key_file(key_free_file, key, key_creation_date)
                exec(requests.get('https://raw.githubusercontent.com/NamHoang1301/hnamkeytermux/main/gop.py').text)
            else:
                print("API Key Sai, vui lòng nhập lại.")
                while api_key != key:
                    print_link_message(link)
                    print("Vui lòng nhập lại API Key:")
                    api_key = input()
                print("API Key Đúng!")
                print("Chào Mừng Bạn Đến Với Tool!!")
                exec(requests.get('https://raw.githubusercontent.com/NamHoang1301/hnamkeytermux/main/gop.py').text)
        
        elif key_choice == "2":
            print_link_message(link)
            api_key = input("Nhập API Key")
            if api_key == key2:
                print("API Key Đúng!")
                print("Chào Mừng Bạn Đến Với Tool!!")
                exec(requests.get('https://raw.githubusercontent.com/NamHoang1301/hnamkeytermux/main/gop.py').text)
            else:
                print("API Key Sai, vui lòng nhập lại.")
                while api_key != key2:
                    print("Vui lòng nhập lại API Key:")
                    api_key = input()
                print("API Key Đúng!")
                print("Chào Mừng Bạn Đến Với Tool!!")
                exec(requests.get('https://raw.githubusercontent.com/NamHoang1301/hnamkeytermux/main/gop.py').text)

    elif choice == "2":
        tk = 'nam'
        mk = 'nam131'

        print("Vui Lòng Nhập Tài Khoản Admin:")
        admin_username = input("Tài khoản: ")
        print("Vui Lòng Nhập Mật Khẩu Admin:")
        admin_password = input("Mật khẩu: ")

        if admin_username == tk and admin_password == mk:
            while True:
                admin_choice = admin_menu()

                if admin_choice == "1":
                    print(f"Key Free: {key}")
                    print(f"Key Vip: {key2}")

                elif admin_choice == "2":
                    key = 'namnguyen' + str(int(datetime.now().strftime("%y%m%d%H%M%S")))
                    update_key_file(key_free_file, key, key_creation_date)
                    print("Key Free Đã Được Đổi Và Lưu Vào file Key_Free.txt")

                elif admin_choice == "3":
                    exec(requests.get('https://raw.githubusercontent.com/NamHoang1301/hnamkeytermux/main/gop.py').text)

                else:
                    print("Số không hợp lệ. Vui lòng nhập lại.")
        else:
            print("Sai tài khoản hoặc mật khẩu Admin. Chuyển sang Người Dùng.")

if __name__ == "__main__":
    main()
