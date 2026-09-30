def main():
    file = input("File name: ").strip().lower()

    if file.endswith(".jpg"):
        print("image/jpeg")
    elif file.endswith(".png"):
        print("image/png")
    elif file.endswith(".pdf"):
        print("application/pdf")


main()
