import os,time
class main:
    @staticmethod
    def main():
        ext_list=['.jpg','png','.pdf','.c']
        a=0
        ext=input(f'''Enter the type of file do want to change the name don't forget to add dot(.)
                  example {ext_list}: ''')
        list=os.listdir()
        for file in list:
            if file.endswith(ext):
                os.rename(file,f'{a}{ext}')
                a+=1
        if a==0:
            print('Invalid extention'.center(120,'-'))
            print(f'Exiting.', end='')
            time.sleep(1)
            print('\b.', end='')
            time.sleep(1)
            print('\b.', end='')
            
    @staticmethod
    def banner():
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')
        banner1=('''\nwelcome to image file renaming program\n''').center(120,'-')
        print(banner1)
        input('\npress ENTER to start the progrm:')

        
class renaming:
    @staticmethod
    def path():
        print(os.getcwd())
        check=input('\nDo you want to change the path (y/n): ')
        match check:
            case 'y':
                pth=input('\nEnter the path to change: ')
                if os.path.exists(pth):
                    os.chdir(pth)
                    main.main()
                else:
                    print('\nThe path is invalid ! \nExiting...\n')
            case 'n':
                main.main()

if __name__ =="__main__":
    main.banner()
    renaming.path()