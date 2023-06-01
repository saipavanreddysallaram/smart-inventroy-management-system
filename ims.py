from flask import Flask,jsonify,request,render_template
app= Flask(__name__)
# establish connection
import pyodbc
server='LAPTOP-H93GIP9O\SQLEXPRESS'
database='newims'
driver='{sql server}'

connetion_string=f'DRIVER={driver};SERVER={server};DATABASE={database};trusted_connection=yes'

conn =pyodbc.connect(connetion_string)
cn = conn.cursor()
# we can see data
cn.execute('select * from customer')
print(cn.fetchall())
# insert data
cn.execute("insert into customer(customer_name,customer_addr,customer_email) values ('sanju','nlr','sanju@gmail.com')")
conn.commit()

customer_name='satis'
customer_addr='lko'
customer_email='sati@gmail.com'

#cn.execute(f"insert into customer(customer_name,customer_addr,customer_email) values ('{customer_name}','{customer_addr}','{customer_email}')")
#conn.commit()
@app.route('/show-customers')
def customer_show():
    cn = conn.cursor()
    cn.execute("select * from customer")
    data = []
    for i in cn.fetchall():
        customer = {}
        customer['customer_id'] = i[0]
        customer['customer_name'] = i[1]
        customer['customer_address'] = i[2]
        customer['customer_email'] = i[3]
        data.append(customer)

    return render_template('show-customer.html',data=data)

@app.route('/')
def home():
    return render_template('index.html')

if __name__=='__main__':
   app.run()