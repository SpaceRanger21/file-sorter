import shutil
import os
import time


while True:
    print('Welcome to file sorter!')
    print('This program is used to sort files based on their file extension.')
    print('You can move/copy all files with the same extension to a different folder.\n')
    print('=======================================================================')
    print('How to use:')
    print('1. Enter the source directory containing all the files.')
    print('2. Enter the file extension of the files you want to move.')
    print('3. Enter the destination folder.\n')
    
    print('=======================================================================')
    print('1. Start Sorting')
    print('2. Cancel (exits this script)')
    
    choice = input('\nWhat do you want to do: ')

    if choice.isnumeric():
       
        if int(choice) == 2:
            break
        elif int(choice) == 1:

            moveORcopy = ''

            while moveORcopy == '':
                moveORcopy = input('\n1. move\n2. copy\nWhat do you want to do: ')
                x = moveORcopy.strip()
                if x.isnumeric() and (x == '1' or x == '2'):
                    break
                else:
                    print('Please enter either 1 or 2')
                    moveORcopy = ''

            src_dir = ''
            ext = ''
            dst_dir = ''

            # ----------------- Getting all necessary inputs -----------------
            while src_dir.strip() == '':
                src_dir = input('\nEnter the Source Directory: ')
                if os.path.exists(src_dir):
                    continue
                else:
                    print(f'Source Destination "{src_dir}" does not exist, please re-enter.')
                    src_dir = ''

            while ext.strip() == '':
                ext = input('\nEnter the File Extension: ')
                if ext.startswith('.'):
                    continue
                else:
                    new_str = '.' + ext
                    ext = new_str

            while dst_dir.strip() == '':
                dst_dir = input('\nEnter the Destination Directory: ')
                if os.path.exists(dst_dir):
                    continue
                else:
                    os.makedirs(dst_dir)

            # ----------------- Main Task Beings -----------------
            os.chdir(src_dir)
            files = os.listdir()
            count = 0

            if int(moveORcopy) == 1:
                start_time = time.time()

                for file in files:
                    if file.endswith(ext):
                        move_start_time = time.time()
                        shutil.move(file, dst_dir)
                        move_finish_time = time.time() - move_start_time
                        print(f'Moved "{file}" to "{dst_dir}" in {round(move_finish_time, 2)}s')
                        count += 1
                time_taken = time.time() - start_time
                print(f'Operation completed, moved {count} files in {round(time_taken, 2)}s')
            elif int(moveORcopy) == 2:
                start_time = time.time()

                for file in files:
                    if file.endswith(ext):
                        copy_start_time = time.time()
                        shutil.copy(file, dst_dir)
                        copy_finish_time = time.time() - copy_start_time
                        print(f'Copied "{file}" to "{dst_dir}" in {round(copy_finish_time, 2)}s')
                        count += 1
                time_taken = time.time() - start_time
                print(f'Operation completed, moved {count} files in {round(time_taken, 2)}s')
            break
        else:
            print('Please enter either 1 or 2')
    else:
        print('Please enter either 1 or 2')
