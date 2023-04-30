from tkinter import*
import random
import time
import datetime

root = Tk()
root.geometry("1600x8000")
root.title("Restaurant management system")

Tops = Frame(root, width=1600, relief=SUNKEN)
# A relief is a border decoration.
# The possible values are:SUNKEN,RAISED,GROOVE,RIDGE,and FLAT.
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)


#==============================#TIME===================================#

localtime = time.asctime(time.localtime(time.time()))
lblInfo = Label(Tops, font=('helvetica', 50, 'italic'), text="DELIGHTS RESTAURANT ", fg="Purple", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)
lblInfo = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="Red", bd=10, anchor='w')
lblInfo.grid(row=1, column=0)

def Ref():
    x = random.randint(10000, 500000)
    random_reference = str(x)
    rand.set(random_reference)

    if(Fries.get() == ""):
        Cost_Fries = 0
    else:
        Cost_Fries = float(Fries.get())

    if (Noodles.get() == ""):
        Cost_Noodles = 0
    else:
        Cost_Noodles = float(Noodles.get())

    if (Drinks.get() == ""):
        Cost_Drinks = 0
    else:
        Cost_Drinks = float(Drinks.get())

    if (Soups.get() == ""):
        Cost_Soups = 0
    else:
        Cost_Soups = float(Soups.get())

    if (Biryani.get() == ""):
        Cost_Biryani = 0
    else:
        Cost_Biryani = float(Biryani.get())

    if (Pizzas.get() == ""):
        Cost_Pizzas = 0
    else:
        Cost_Pizzas = float(Pizzas.get())

    if (Burgers.get() == ""):
        Cost_Burgers = 0
    else:
        Cost_Burgers = float(Burgers.get())

    if (Sandwiches.get() == ""):
        Cost_Sandwiches = 0
    else:
        Cost_Sandwiches = float(Sandwiches.get())

    if (WaterBottles.get() == ""):
        Cost_WaterBottles = 0
    else:
        Cost_WaterBottles = float(WaterBottles.get())

    Cost_of_Fries = Cost_Fries * 50
    Cost_of_Noodles = Cost_Noodles * 60
    Cost_of_Drinks = Cost_Drinks * 20
    Cost_of_Soups = Cost_Soups * 80
    Cost_of_Biryani = Cost_Biryani * 100
    Cost_of_Pizzas = Cost_Pizzas * 150
    Cost_of_Burgers = Cost_Burgers * 90
    Cost_of_Sandwiches = Cost_Sandwiches * 90
    Cost_of_WaterBottles = Cost_WaterBottles * 20


    CostofMeal = "Rs", str(
        '%.2f' % (Cost_of_Fries + Cost_of_Drinks + Cost_of_Noodles + Cost_of_Soups + Cost_of_Burgers +
                  Cost_of_Sandwiches + Cost_of_Biryani + Cost_of_Pizzas + Cost_of_WaterBottles))

    PayTax = ((Cost_of_Fries + Cost_of_Drinks + Cost_of_Noodles + Cost_of_Soups + Cost_of_Burgers +
               Cost_of_Sandwiches + Cost_of_Biryani + Cost_of_Pizzas + Cost_of_WaterBottles) * 0.2)

    TotalCost = (Cost_of_Fries + Cost_of_Drinks + Cost_of_Noodles + Cost_of_Soups + Cost_of_Burgers +

                 Cost_of_Sandwiches + Cost_of_Biryani + Cost_of_Pizzas + Cost_of_WaterBottles)

    Ser_Charge = ((Cost_of_Fries + Cost_of_Drinks + Cost_of_Noodles + Cost_of_Soups + Cost_of_Burgers +
                       Cost_of_Sandwiches + Cost_of_Biryani + Cost_of_Pizzas + Cost_of_WaterBottles) / 99)

    Service = "Rs", str('%.2f' % Ser_Charge)

    OverAllCost = "Rs", str('%.2f' % (PayTax + TotalCost + Ser_Charge))

    PaidTax = "Rs", str('%.2f' % PayTax)

    Service_Charges.set(Service)
    Cost.set(CostofMeal)
    StateTax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)

def ref_Exit():
    root.destroy()

def ref_Reset():
    rand.set("")
    Fries.set("")
    Noodles.set("")
    Drinks.set("")
    Soups.set("")
    Biryani.set("")
    Pizzas.set("")
    Burgers.set("")
    Sandwiches.set("")
    WaterBottles.set("")

    Cost.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charges.set("")
    StateTax.set("")


########################## Restaurant INFO ###############################

rand = StringVar()
Fries = StringVar()
Noodles = StringVar()
Drinks = StringVar()
Soups = StringVar()
Biryani = StringVar()
Pizzas = StringVar()
Burgers = StringVar()
Sandwiches = StringVar()
WaterBottles = StringVar()

Cost = StringVar()
SubTotal = StringVar()
Service_Charges = StringVar()
StateTax = StringVar()
Total = StringVar()


################################# Reference ###########################

lblreference = Label(f1, font=("Times New Roman", 16, "bold"), text="Reference", bd=16, anchor="w")
lblreference.grid(row=0, column=0)
textreference = Entry(f1, font=("Times New Roman", 16, "bold"), textvariable=rand, bd=10, insertwidth=4, bg="sky blue",
                      justify="right")
textreference.grid(row=0, column=1)


######################################Fries########################################

lblFries = Label(f1, font=("Times New Roman", 16, "bold"), text="Fries", bd=16, anchor="w")
lblFries.grid(row=1, column=0)
textFries = Entry(f1, font=("Times New Roman", 16, "bold"), textvariable=Fries, bd=10, insertwidth=4, bg="powder blue",
                  justify="right")
textFries.grid(row=1, column=1)


################################# Noodles ########################################

lblNoodles = Label(f1, font=("Times New Roman", 16, "bold"), text="Noodles", bd=16, anchor="w")
lblNoodles.grid(row=2, column=0)
textNoodles = Entry(f1, font=("Times New Roman", 16, "bold"), textvariable=Noodles, bd=10, insertwidth=4, bg="powder blue",
                    justify="right")
textNoodles.grid(row=2, column=1)


################################ Drinks ########################################

lblDrinks = Label(f1, font=("Times New Roman", 16, "bold"), text="Drinks", bd=16, anchor="w")
lblDrinks.grid(row=3, column=0)
textDrinks = Entry(f1, font=("Times New Roman", 16, "bold"), textvariable=Drinks, bd=10, insertwidth=4, bg="powder blue",
                   justify="right")
textDrinks.grid(row=3, column=1)


################################# Soups ##########################################

lblSoups = Label(f1, font=("Times New Roman", 16, "bold"), text="Soups", bd=16, anchor="w")
lblSoups.grid(row=3, column=0)
textSoups = Entry(f1, font=("Times New Roman", 16, "bold"), textvariable=Soups, bd=10, insertwidth=4, bg="powder blue",
                  justify="right")
textSoups.grid(row=3, column=1)


############################### Biryani ###########################################

lblBiryani = Label(f1, font=("Times New Roman", 16, "bold"), text="Biryani", bd=16, anchor="w")
lblBiryani.grid(row=4, column=0)
textBiryani = Entry(f1, font=("Times New Roman", 16, "bold"), textvariable=Biryani, bd=10, insertwidth=4, bg="powder blue",
                    justify="right")
textBiryani.grid(row=4, column=1)


############################### Pizzas ############################################

lblPizzas = Label(f1, font=("Times New Roman", 16, "bold"), text="Pizzas", bd=16, anchor="w")
lblPizzas.grid(row=0, column=2)
textPizzas = Entry(f1, font=("Times New Roman", 16, "bold"), textvariable=Pizzas, bd=10, insertwidth=4, bg="powder blue",
                   justify="right")
textPizzas.grid(row=0, column=3)


############################## Burgers ############################################

lblBurgers = Label(f1, font=("Times New Roman", 16, "bold"), text="Burgers", bd=16, anchor="w")
lblBurgers.grid(row=1, column=2)
textBurgers = Entry(f1, font=("Times New Roman", 16, "bold"), textvariable=Burgers, bd=10, insertwidth=4, bg="powder blue",
                    justify="right")
textBurgers.grid(row=1, column=3)


############################ Sandwiches ###########################################

lblSandwiches = Label(f1, font=("Times New Roman", 16, "bold"), text="Sandwiches", bd=16, anchor="w")
lblSandwiches.grid(row=2, column=2)
textSandwiches = Entry(f1, font=("Times New Roman", 16, "bold"), textvariable=Sandwiches, bd=10, insertwidth=4,
                       bg="powder blue", justify="right")
textSandwiches.grid(row=2, column=3)


############################ WaterBottles ###################################

lblWaterBottles = Label(f1, font=("Times New Roman", 16, "bold"), text="WaterBottles", bd=16, anchor="w")
lblWaterBottles.grid(row=3, column=2)
textWaterBottles = Entry(f1, font=("Times New Roman", 16, "bold"), textvariable=WaterBottles, bd=10, insertwidth=4,
                         bg="powder blue", justify="right")
textWaterBottles.grid(row=3, column=3)

########################### Cost of Meal ####################################

lblCost = Label(f1, font=("Times New Roman", 16, "bold"), text="Cost of Meal", bd=16, anchor="w")
lblCost.grid(row=0, column=4)
textCost = Entry(f1, font=("Times New Roman", 16, "bold"), textvariable=Cost, bd=10, insertwidth=4,
                         bg="powder blue", justify="right")
textCost.grid(row=0, column=5)


######################### Service Charges #################################

lblService_Charges = Label(f1, font=("Times New Roman", 16, "bold"), text="Service Charges", bd=16, anchor="w")
lblService_Charges.grid(row=1, column=4)
textService_Charges = Entry(f1, font=("Times New Roman", 16, "bold"), textvariable=Service_Charges, bd=10, insertwidth=4,
                         bg="powder blue", justify="right")
textService_Charges.grid(row=1, column=5)


############################### State Tax ########################################

lblStateTax = Label(f1, font=("Times New Roman", 16, "bold"), text="State Tax", bd=16, anchor="w")
lblStateTax.grid(row=2, column=4)
textStateTax = Entry(f1, font=("Times New Roman", 16, "bold"), textvariable=StateTax, bd=10, insertwidth=4,
                         bg="powder blue", justify="right")
textStateTax.grid(row=2, column=5)


############################### Sub Total ########################################

lblSubTotal = Label(f1, font=("Times New Roman", 16, "bold"), text="Sub Total", bd=16, anchor="w")
lblSubTotal.grid(row=3, column=4)
textSubTotal = Entry(f1, font=("Times New Roman", 16, "bold"), textvariable=SubTotal, bd=10, insertwidth=4,
                         bg="powder blue", justify="right")
textSubTotal.grid(row=3, column=5)


################################# Total Cost #######################################

lblTotal = Label(f1, font=("Times New Roman", 16, "bold"), text="Total Cost", bd=16, anchor="w")
lblTotal.grid(row=4, column=4)
textTotal = Entry(f1, font=("Times New Roman", 16, "bold"), textvariable=Total, bd=10, insertwidth=4,
                         bg="powder blue", justify="right")
textTotal.grid(row=4, column=5)



##################################### Buttons ####################################

btn_total = Button(f1, padx=16, pady=8, bd=16, fg="black", font=("Times New Roman", 16, "bold"),
                   width=10, text="Total", bg="powder blue", command=Ref)
btn_total.grid(row=7, column=1)

btn_total = Button(f1, padx=16, pady=8, bd=16, fg="black", font=("Times New Roman", 16, "bold"),
                   width=10, text="Reset", bg="powder blue", command=ref_Reset)
btn_total.grid(row=7, column=2)

btn_total = Button(f1, padx=16, pady=8, bd=16, fg="black", font=("Times New Roman", 16, "bold"),
                   width=10, text="Exit", bg="powder blue", command=ref_Exit)
btn_total.grid(row=7, column=3)


root.mainloop()

