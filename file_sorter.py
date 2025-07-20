import shutil
import os
import time


class BackgroundColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


while True:
    print('\nWelcome to file sorter!')
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
    
    choice = input(F'\n{BackgroundColors.HEADER}What do you want to do: {BackgroundColors.ENDC}')

    if choice.isnumeric():
       
        if int(choice) == 2:
            break
        elif int(choice) == 1:

            moveORcopy = ''

            while moveORcopy == '':
                moveORcopy = input(F'\n1. move\n2. copy\n{BackgroundColors.HEADER}\nWhat do you want to do: {BackgroundColors.ENDC}')
                x = moveORcopy.strip()
                if x.isnumeric() and (x == '1' or x == '2'):
                    break
                else:
                    print(f'{BackgroundColors.FAIL}ERROR: Please enter either 1 or 2{BackgroundColors.ENDC}')
                    moveORcopy = ''

            src_dir = ''
            ext = ''
            dst_dir = ''

            # ----------------- Getting all necessary inputs -----------------
            while src_dir.strip() == '':
                src_dir = input(f'\n{BackgroundColors.HEADER}Enter the Source Directory: {BackgroundColors.ENDC}')
                if os.path.exists(src_dir):
                    continue
                else:
                    print(f'{BackgroundColors.FAIL}ERROR: Source Destination "{src_dir}" does not exist, please re-enter.{BackgroundColors.ENDC}')
                    src_dir = ''

            while ext.strip() == '':
                ext = input(f'\n{BackgroundColors.HEADER}Enter the File Extension: {BackgroundColors.ENDC}')
                if ext.startswith('.'):
                    continue
                else:
                    new_str = '.' + ext
                    ext = new_str

            while dst_dir.strip() == '':
                dst_dir = input(f'\n{BackgroundColors.HEADER}Enter the Destination Directory: {BackgroundColors.ENDC}')
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
                        print(f'{BackgroundColors.OKGREEN}Moved {BackgroundColors.OKCYAN}"{file}" {BackgroundColors.OKGREEN}to {BackgroundColors.OKCYAN}"{dst_dir}" {BackgroundColors.OKGREEN}in {round(move_finish_time, 2)}s{BackgroundColors.ENDC}')
                        count += 1
                time_taken = time.time() - start_time
                print(f'{BackgroundColors.OKGREEN}Operation completed, moved {count} files in {round(time_taken, 2)}s{BackgroundColors.ENDC}')
            elif int(moveORcopy) == 2:
                start_time = time.time()

                for file in files:
                    if file.endswith(ext):
                        copy_start_time = time.time()
                        shutil.copy(file, dst_dir)
                        copy_finish_time = time.time() - copy_start_time
                        print(f'{BackgroundColors.OKGREEN}Copied {BackgroundColors.OKCYAN}"{file}" {BackgroundColors.OKGREEN}to {BackgroundColors.OKCYAN}"{dst_dir}" {BackgroundColors.OKGREEN}in {round(copy_finish_time, 2)}s{BackgroundColors.ENDC}')
                        count += 1
                time_taken = time.time() - start_time
                print(f'{BackgroundColors.OKGREEN}Operation completed, moved {BackgroundColors.OKCYAN}{count} files {BackgroundColors.OKGREEN}in {round(time_taken, 2)}s{BackgroundColors.ENDC}')
            break
        else:
            print(f'{BackgroundColors.FAIL}ERROR: Please enter either 1 or 2{BackgroundColors.ENDC}')
    else:
        print(f'{BackgroundColors.FAIL}ERROR: Please enter either 1 or 2{BackgroundColors.ENDC}')
