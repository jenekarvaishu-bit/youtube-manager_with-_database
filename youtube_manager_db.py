import sqlite3

conn = sqlite3.connect('youtube_videos.db') 
cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
       
''')

def list_all_videos():
    cursor.execute(" SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video ():
    NAME = input("enter the video name: ")
    TIME = input("enter the time of video: ")
    cursor.execute("INSERT INTO videos(name,time)VALUES(?,?)",(NAME , TIME))
    conn.commit()

def update_video():
    NEW_NAME = input("enter the name of video you want to add: ")
    NEW_TIME = input("enter the time of the video: ")
    video_id = input("video id which you want to update: ")
    cursor.execute("UPDATE videos SET name = ? , time =? WHERE id =?",(NEW_NAME , NEW_TIME,video_id))
    conn.commit()


def delete_video():
    video_id = input("enter the video id you want to delete it: ")
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    conn.commit()

def main():
    while True:
        print("youtube manager|| \n  choose any option: ")
        print("1. list videos")
        print("2. add videos")
        print("3. update videos")
        print("4. delete videos")
        print("5. exist app")
        choice = input("enter your choice: ")


        match choice:
            case '1':
                list_all_videos()

            case '2':
                add_video()

            case '3':
                update_video()

            case '4':
                delete_video()

            case '5':
                break

            case _:
                print("Invalid choice...")



    conn.close()

if __name__ == "__main__":
    main()