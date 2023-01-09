username ="rakesh"
password ="1234"
choice = 0
customer_username = input("Enter Your Username:")
customer_password = str(input("Enter Your 4 digits PIN:"))
amount = 1000
if customer_username==username and customer_password==password:
    while choice != 4:
        print('''
              1.Diposite
              2.Withdraw
              3.Ministatement
              4.Menu
              5.Exit
              ''')
        option = int(input('select Your Option:'))
        
        if option ==1:
            if option == 1:
                dep = int(input('Enter your Diposite Amount:'))
                while choice !=2:
                    print('''
                          if you insert the amount please select Yes, else No
                          1.Yes
                          2.No
                          3.Exit
                          ''')
                    select_option =int(input('select Yes/No:')) 
                    
                    if select_option == 1:
                        amount+= dep
                        print("="*18,"ATM","="*18)
                        print(" "*41)
                        print("Total Amount :",amount)
                        print(" "*41)
                        print("="*10,"Thanks for visiting","="*10)
                        exit()
                    if select_option == 3:
                        print("="*18,"ATM","="*18)
                        print(" "*41)
                        print("Plese re-enter your User/PIN")
                        print(" "*41)
                        print("="*10,"Thanks for visiting","="*10)
                        exit()

        elif option == 2:
            withd = int(input('Enter your withdraw Amount:'))
            while choice != 2:
                print('''
                      please select yes if your enter correct amount else no
                      1.Yes
                      2.no
                      3.exit
                      ''')
                select_option2 = int(input("select your option:"))
                if select_option2 == 1:
                    amount-= withd
                    print("="*18,"ATM","="*18)
                    print(" "*41)
                    print("Please take your amount")
                    print('Total Balance:',amount)
                    print(" "*41)
                    print("="*10,"Thanks for visiting","="*10)
                    exit()
                    
                elif select_option2 == 3:
                    print("="*18,"ATM","="*18)
                    print(" "*41)
                    print("="*10,"Thanks for visiting","="*10)
                    print(" "*41)
                    exit()
        elif option == 3:
            print("="*18,"ATM","="*18)
            print(" "*41)
            print("Username      :",username)
            print("PIN           :",len(password)*"*")
            print("Total Balance :",amount)
            print(" "*41)
            print("="*10,"Thanks for visiting","="*10)
            exit()
        elif option == 5:
            print("="*18,"ATM","="*18)
            print("="*10,"Thanks for visiting","="*10)
            exit()
            
else:
    print("Please Enter correct Username/PIN")
    exit()

                               
