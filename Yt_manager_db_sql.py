import sqlite3

conn = sqlite3.connect("youtube_vidoes_sql.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')


def list_video():
    cursor.execute(''' SELECT * FROM videos ''')
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id, newName, newTime):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (newName, newTime, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))


def main():
    while True:
        print("\n Youtube Manager with SQLITE DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. exit app")
        choice = input("Please enter the operation number you want to perform: ")
    
        match choice:
            case '1':
                list_video()
            case '2':
                name = input("Enter the video name: ")
                time = input("Enter the video duration: ")
                add_video(name, time)
            case '3':
                video_id = input("Enter the video id to update: ")
                newName = input("Enter the video name: ")
                newTime = input("Enter the video duration: ")
                update_video(video_id, newName, newTime)
            case '4':
                video_id = input("Enter the video id to delete: ")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid Choice 😶 Dear")
    

    conn.close()


if __name__ == "__main__":
    main()