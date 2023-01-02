from flask import Flask, render_template, request

app = Flask(__name__)
current_account=[]

accounts=[
      {
      "username":"aaa",
      "pin":111,
      "credit":1000,
      "transactions":[{"amount":-200, "timestamp":"10.12.2022"}]  
    },
           {
      "username":"bbb",
      "pin":222,
      "credit":800,
      "transactions":[{"amount":-200, "timestamp":"10.12.2022"}]   
    }
      ]


@app.route('/')
def home():
    message="Welcome to Bank Model"

    return render_template("home.html", message=message)
  
@app.route('/login')
def login():
  current_username = request.args.get("username","aaa")
  current_pin = request.args.get("pin",1)
  wrong_pin=0
  while wrong_pin <=3:
    for account in accounts:
      if account.username == current_username and account.pin == current_pin:
        current_account.append(account)
      else:
        wrong_pin+=1
        if wrong_pin==3:
            print("Falsche PIN! Konto gesperrt!") 

  return render_template("login.html", current_username=current_username, current_pin=current_pin, current_account=current_account)

# @app.route('/bankmodel')

@app.route('/logout')
def logout():
  current_account=[]
  current_username = "a"
  current_pin = 1
  
  return render_template("logout.html", current_username=current_username, current_pin=current_pin, current_account=current_account)


@app.route('/kontodetails')
def kontodetails(current_account):
  
  return render_template("kontodetails.html", current_account=current_account)       
# def withdraw(current_credit, money):
#   if current_credit <= money:
#       current_credit -= money
#       print(f"Du hast {money} € abgehoben.")
#   else:
#       print("Du kannst nur " + str(current_credit) + " € abheben!")
        
# def pay_in(current_credit, money):
#   current_credit += money
  
# def bankmodel():

     


#     return render_template("bankmodel.html", current_username=current_username, current_pin=current_pin, current_credit=current_credit, accounts=accounts, pay_in=pay_in(), withdraw=withdraw() )
  
if __name__ == '__main__':
    app.run()