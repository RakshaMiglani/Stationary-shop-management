# Stationary-shop-management

This is a menu driven code has two modes (admin & customer).
It stores data using 3 csv files(items,sales and customer) .
The password is saved in a mysql database.
The modules required to run the code are tabulate, mysql.connector and csv.
The code is written as a set of functions and a main code that uses an infinite loop with break to call the functions.
Before running the entier code, the create function needs to be run on the system to create all the required files.

## MENU- Admin Mode
1.Create New Product List<br>
2.Add<br>
3.View Stock less than 'n'<br>
4.View profit stats<br>
5.Create New Sales Record<br> 
6.Increment Stock<br>
7.Modify Price<br>
8.Bill<br>
9.Change Password<br>
10.View All<br>
11.Issue a Coupon to a Customer<br>
12.Exchange<br>
13.View Customers who have spent more than Rs.'n'<br>
14.Exit<br>

## MENU- Customer Mode
1.View All Products<br>
2.View Products of a Brand<br>
3.View Products of a given Description<br>
4.View Products in a Price Range<br>
5.Exit<br>


