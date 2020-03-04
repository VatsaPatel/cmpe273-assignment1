CHUNK_SIZE = 6550

image_file = 'upload.txt'
new_file_loc = 'myfile.jpg'

# new_file = open(new_file_loc, 'wb+')

chunk_lookup = {
}
i=0
with open(image_file, 'rb+') as ifile:
    while True:
        chunk = ifile.read(CHUNK_SIZE)
        if not chunk: break
        i+=1
        chunk_lookup[i] = chunk

        # printing chunk here will show each line correctly

# Note: myfile.txt has all the data. 30 lines of weird symbols.

# with open('myfile.jpg', 'rb') as f:
#     data = f.read()
#     print(data)
# new_file.write(chunk)
print(list(chunk_lookup.keys())[-1])