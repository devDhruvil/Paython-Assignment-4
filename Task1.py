file = open("sample.txt", "w")
file.write("This is a sample text file.\nIt contains multiple lines.")
file.close()


def read_file(filename):
    try:
        file = open(filename, 'r')
        for i, line in enumerate(file, start=1):
            print(f"Line"+ str(i) +":" + str(line.strip()) + "")

    except FileNotFoundError:
        print(f"Error: The file " + str(filename) + " was not found.")

    except Exception as e:
        print(f"An unexpected error occurred: " + str(e))


read_file('sample.txt')
