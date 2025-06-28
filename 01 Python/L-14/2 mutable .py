'''
        data
                1. Mutable data
                2. immutable data

        mutable     -->  can be change/modify/update
        immutable   -->  cannot be change/modify/update

        --> String having immutable nature


        for ex 
                              (Immutable)            (mutable)
                               BOY NAME              GIRL NAME
                
        before marrigae       aditya patel         lior vadhavkar
        after  marrigae       aditya patel         lior patel

        Emp detail
        ----------

        Name     :  Aditya              cannot be change 
        Age      :  16                  can be change
        Salary   :  100.62              can be change
        mail id  :  aditya@123.com      cannot be change 
        passport :  123456689           cannot be change

    ---> List having mutable nature 
    ---> String having immutable nature 

'''

a = [10,20,30,40,50]
print(a)                            #  [10, 20, 30, 40, 50]
a[0] = 99                           
print(a)                            #  [99, 20, 30, 40, 50]

# String having immutable nature let me prf

b = "aditya"
print(b)
b[0] = 'p'
print(b)         #  TypeError: 'str' object does not support item assignment





