print("doan van quyen")
print("235752021610047")
def find_longest_words(text):
   
    words = text.split()
    
    max_length = max(len(word) for word in words)
    
    longest_words = [word for word in words if len(word) == max_length]
    return longest_words

def main():
   
    text = input("Nhập văn bản: ")
    
    
    longest_words = find_longest_words(text)
    print("Những từ dài nhất trong văn bản là:", longest_words)


if __name__ == "__main__":
    main()
