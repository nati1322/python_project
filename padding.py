def padding(width, direction):
    text = input("enter the text: ")
    text_length = len(text)
    padding_length = width - text_length
    if direction == 0:
        print("#"*padding_length, end="")
        print(text)
    elif direction == 1:
        print(text, end="")
        print("#"*padding_length, end="")


if __name__ == "__main__":
    padding(10, 1)