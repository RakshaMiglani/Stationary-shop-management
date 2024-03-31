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

 ## DESCRIPTION OF UDFs
<table>
<tr><th>S.no.</th>
<th>UDF-NAME</th>
<th>DESCRIPTION</th>
<th>Menu option no.</th></tr>
<tr><td>1.</td>
<td>create()</td>
<td>Creates 3 empty csv files items,sales and customer</td>
<td>1-Admin (with check)</td></tr>
<tr><td>2.</td>
<td>mode()</td>
<td>Accepts mode from user and verifies in case of admin</td>
 <td>-----------------</td></tr>
<tr><td>3.</td>
<td>search()</td>
<td>Accepts description and brand(if needed) and returns itemID</td>
<td>Admin & Customer</td></tr>
<tr><td>4.</td>
<td>genID()</td>
<td>Generates a unique ID</td>
<td>Admin </td></tr>
<tr><td>5.</td>
<td>add()</td>
<td>Adds new product to items.csv and sales.csv after assigning a unique id to it by calling genID()</td>
<td>2-Admin</td></tr>
<tr><td>6.</td>
<td>view_all()</td>
<td>Displays details of all products</td> 
<td>10-Admin & 1-Customer</td></tr>
<tr><td>7.</td>
<td>view_stock(n)</td>
<td>Displays product details for products with stock less than ‘n’</td>
<td>3-Admin</td></tr>
<tr><td>8.</td>
<td>view_b(b)</td>
<td>Displays product details of brand ‘b’</td>
<td>2-Customer</td></tr>
<tr><td>9.</td>
<td>view_d(d)</td>
<td>Displays product details with  description ‘d’</td>
<td>3-Customer</td></tr>
<tr><td>10.</td>
<td>view_p(ll,ul)</td>
<td>Displays product details with price in between ‘ll’ and ‘ul’</td>
<td>4-Customer</td></tr>
<tr><td>11.</td>
<td>inc_stock()</td>
<td>Increases stock of a particular item after accepting itemID or calling search()</td>
<td>6-Admin</td></tr>
<tr><td>12.</td>
<td>mod_p(x)</td>
<td>Modifies the price of a particular item after accepting itemID or calling search(). If x=2 cp is changed and sp is changed if x=3</td>
<td>7-Admin</td></tr>
<tr><td>13.</td>
<td>view_profit()</td>
<td>Displays content of sales.csv</td>
<td>4-Admin</td></tr>
<tr><td>14.</td>
<td>buy_bill()</td>
<td>Accepts itemID or calls search(). Decrement stock and increase profit. increments the amount spent by customer. Generates a bill and calls pay(c)</td>
<td>8-Admin</td></tr>
<tr><td>15.</td>
<td>change()</td>
<td>Changes the password to enter Admin mode</td>
<td>9-Admin</td></tr>
<tr><td>16.</td>
<td>create_p()</td>
<td>Deletes previous sales records and creates a new sales record</td>
<td>5-Admin(with check)</td></tr>
<tr><td>17.</td>
<td>pay(c)</td>
<td>Accepts the mode of payment if card accepts card details and collects amount ‘c’ </td>
<td>Admin & Customer</td></tr>
<tr><td>18.</td>
<td>exchange(x,y=1)</td>
<td>It increments stock of item with ID ‘x’ by ‘y’ and issues store credit to customer after accepting phone no.</td>
<td>12-Admin</td></tr>
<tr><td>19.</td>
<td>coupon(x)</td>
<td>Increments store credit of a customer by ‘x’ after accepting phone no.</td>
<td>11-Admin</td></tr>
<tr><td>20.</td>
<td>viewc(x=0)</td>
<td>Displays customer details with amount spent greater than ’x’</td>
<td>13-Admin</td></tr>
</table>

