import json

file_used = 'youtube.txt'

def load_data():
    try:
        with open(file_used, 'r') as file:
            return json.load(file) # convert srting data into json format and load data
    except FileNotFoundError:
        return []

def save_data_helper(vidoes):
            with open(file_used, 'w') as file:
                json.dump(vidoes, file) # write data in file and following format, data to be passed (vidoes) and in which is is saved named file.

def list_all_vidoes(vidoes):
    print('\n')
    print('*' * 101)
    for index, video in enumerate(vidoes, start = 1):
        print(f'{index}. Video title is "{video['name']}" and the duration of video is {video['time']} ')
    print('*' * 101)

def add_video(vidoes):
    name = input('Enter video name: ')
    time = input('Enter video duration: ')
    vidoes.append({'name': name, 'time': time})
    save_data_helper(vidoes)

def update_video(vidoes):
    list_all_vidoes(vidoes)
    index = int(input("Enter the video number to be updated: "))
    if 1<= index <= len(vidoes):
        new_name = input('Please enter the video\'s new name: ')
        new_time = input('Please enter the video\'s new duration: ')
        vidoes[index-1] = {'name': new_name, 'time': new_time}
        save_data_helper(vidoes)
    else:
        print("Invalid Index Selected 😶 Dear")

def delete_video(vidoes):
    list_all_vidoes(vidoes)
    index = int(input("Enter the video number to be deleted: "))
    if 1<= index <= len(vidoes):
        del vidoes[index-1]
        save_data_helper(vidoes)
    else:
        print("Invalid Index Selected 😶 Dear")


def main():
    vidoes = load_data()

    while True:
        print('\n Youtube Manager App || Choose an option to continue')
        print('1. List all youtube vidoes.')
        print('2. Add a new video.')
        print('3. Update existing video.')
        print('4. Delete a video.')
        print('5. Exit the app.')
        Choose_Option = input('Please enter your choice: ')
        # print('Currently video data is: ', vidoes)

        match Choose_Option:
            case '1':
                list_all_vidoes(vidoes)
            case '2':
                add_video(vidoes)
            case '3':
                update_video(vidoes)
            case '4':
                delete_video(vidoes)
            case '5':
                break
            case _:
                print("Invalid Choice 😶 Dear")

                   
if __name__ == "__main__" :
    main()

