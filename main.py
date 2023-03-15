import pymysql
from flask import Flask ,request,render_template
import datetime
from pprint import pprint
app = Flask(__name__)


conn = pymysql.Connect(host="127.0.0.1", port=3306, user="root", password="8080", database="hrconnect")


@app.route("/data")
def main():
    salary_value = request.args.get("salary")
    with conn:
        with conn.cursor() as cursor:
            data = []
            sql = f"select first_name,last_name,email,phone_number from employees where salary >= {salary_value};"
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                first_name, last_name, email,contact_number = i
                if contact_number:
                    contact_number = contact_number.split('.')

                    contact_number = "".join(contact_number)
                else:
                    pass
                data.append({"Employee_name":first_name+" "+last_name,"Email":email,"Contact":contact_number})

    return render_template("data.html", data=data)


@app.route("/task2")   # URL-binding
def main2():
    with conn:
        with conn.cursor() as cursor:
            data2 = []
            sql = "select first_name,last_name,hire_date from employees where salary >= {0} and department_id between" \
                  " {1} AND {2};".format(4200, 30, 110)
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                first_name, last_name, hire_date = i
                hire_date = datetime.datetime.strptime(hire_date, "%d-%b-%y")
                hire_date = hire_date.strftime("%Y-%d-%m")
                data2.append({"Hire_Date":hire_date, "Employee_names": first_name + " " + last_name})


    return render_template("task2.html", data=data2)


if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)







