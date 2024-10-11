import pyautogui
import time
import os

flag = True  # 将flag声明为全局变量

def auto_login(input_lists):
    time.sleep(1)
    for input_str in input_lists:
        pyautogui.write(input_str)
        time.sleep(0.1)
        pyautogui.press('tab')
        time.sleep(0.1)
    pyautogui.press('enter')

def list_accounts():
    accounts_list = []
    for file in os.listdir('./data'):
        accounts_list.append(file.split('.')[0])
    return accounts_list

def read_file(account_name):
    with open(f'./data/{account_name}.txt', 'r', encoding='utf-8') as f:
        input_lists = f.read().split('\n')
    return input_lists

def select_account():
    accounts_list = list_accounts()
    if len(accounts_list) == 0:
        print('*** no accounts found ***')
    else:
        print('select your account')
        for i, account in enumerate(accounts_list):
            print(f'{i+1}. {account}')
        account_num = int(input('enter account number: '))
        account_name = accounts_list[account_num-1]
        input_lists = read_file(account_name)
        auto_login(input_lists)

def add_account():
    account_name = input('enter account name: ')
    input_lists = []
    while True:
        input_str = input('enter input, q to exit: \n')
        if input_str == 'q':
            break
        input_lists.append(input_str)
    with open(f'./data/{account_name}.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(input_lists))
    print(f'account {account_name} added')

def delete_account():
    accounts_list = list_accounts()
    if len(accounts_list) == 0:
        print('no accounts found')
    else:
        for i, account in enumerate(accounts_list):
            print(f'{i+1}. {account}')
        account_num = int(input('enter account number to delete: '))
        account_name = accounts_list[account_num-1]
        os.remove(f'./data/{account_name}.txt')
        print(f'account {account_name} deleted')

def menu():
    print('1. select account to auto login')
    print('2. add account')
    print('3. delete account')
    print('4. exit')
    choice = int(input('enter your choice: '))
    if choice == 1:
        select_account()
    elif choice == 2:
        add_account()
    elif choice == 3:
        delete_account()
    elif choice == 4:
        global flag
        flag = False
    else:
        print('invalid choice')

def run():
    while flag:
        try:
            menu()
        except Exception as e:
            print('invalid choice')

if __name__ == '__main__':
    run()