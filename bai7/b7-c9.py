print("doan van quyen")
print("235752021610047")

def copy_file_content(source_file, destination_file):
    try:
        
        with open(source_file, 'r', encoding='utf-8') as src:
           
            with open(destination_file, 'w', encoding='utf-8') as dest:
                
                content = src.read()
                dest.write(content)
        
        print(f"Nội dung đã được sao chép từ '{source_file}' sang '{destination_file}'.")
    except FileNotFoundError:
        print(f"Không tìm thấy tệp '{source_file}'.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

def main():
    source_file = input("Nhập tên tệp nguồn (bao gồm phần mở rộng, ví dụ: 'source.txt'): ")
    destination_file = input("Nhập tên tệp đích (bao gồm phần mở rộng, ví dụ: 'destination.txt'): ")
    
  
    copy_file_content(source_file, destination_file)


if __name__ == "__main__":
    main()
