import mysql.connector as sqlcon
import base64
import os


conn = sqlcon.connect(host='aws.connect.psdb.cloud',
                      password='pscale_pw_5N9UzKjFxtGYI1Sal8AxaaOtiefLcuwPuG4wtmzjJdW',
                      user='518qjoru1docwhov7azw',
                      database='birthday_gift_db')

conn_cursor =conn.cursor()
if conn.is_connected() == True:
    print('Connection Successful.')

# def convertToBinary(filename):
#     with open(filename, mode='rb') as file:
#         binaryData = file.read()
#     return binaryData
def convertToBinary(filename):
    with open(filename, mode='rb') as file:
        bin_data = base64.b64encode(file.read())
    
    img_bin_data = bin_data.decode('utf-8')
    
    return img_bin_data


def binaryToImage(data, filename):
    with open(filename, mode='wb') as file:
        file.write(data)


def insertBLOB(img_no, img_path):
    print("Inserting BLOB into MySQL database...")
    
    try:
        bin_img = convertToBinary(img_path)
        insert_query = f"INSERT INTO IMAGES VALUES(%s, %s);"

        conn_cursor.execute(insert_query, (img_no, bin_img))
        conn.commit()

        print("Image has been Successfully inserted into the database.")

    except sqlcon.Error as error:
        print(f"Failed to insert images into the database {error}")


img_folder_path = r"C:\Users\User\GitHub Repositories\Source Images for Gift Website"
images = os.listdir(img_folder_path)

for img in range(len(images)):
    img_path = fr"{img_folder_path}\{images[img]}"
    imgNo = img + 1

    insertBLOB(imgNo, img_path)


print(f"All {len(images)} images has been inserted into the database in binary form.")

# print(convertToBinary(fr"{img_folder_path}\{images[0]}"))






'''https://pynative.com/python-mysql-blob-insert-retrieve-file-image-as-a-blob-in-mysql/#:~:text=To%20Store%20BLOB%20data%20in,table%20with%20a%20BLOB%20column.&text=This%20table%20contains%20the%20following%20two%20BLOB%20columns'''