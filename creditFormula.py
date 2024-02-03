from datetime import datetime, timedelta
from tkinter import *

def credit():
    plan_cost = float(cost_entry.get())
    start_date = start_entry.get()
    end_date = end_entry.get()
    start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = datetime.strptime(end_date, "%Y-%m-%d")
    
    credit_per_day = plan_cost / 30.00
    date_diff = end_datetime - start_datetime
    total_credit = credit_per_day * date_diff.days
    
    formula_text = f"Formula: {plan_cost} / 30.00 * {date_diff.days} days"
    difference_text = f"Difference in days: {date_diff.days}"
    
    result_label.config(text="{:.2f}".format(total_credit))
    
    formula_label.config(text=formula_text)
    difference_label.config(text=difference_text)

root = Tk()
root.geometry("400x250")

cost_label = Label(root, text="Enter plan cost:")
cost_label.pack()
cost_entry = Entry(root)
cost_entry.pack()

start_label = Label(root, text="Enter start date (YYYY-MM-DD):")
start_label.pack()
start_entry = Entry(root)
start_entry.pack()

end_label = Label(root, text="Enter end date (YYYY-MM-DD):")
end_label.pack()
end_entry = Entry(root)
end_entry.pack()

calculate_button = Button(root, text="Calculate", command=credit)
calculate_button.pack()

result_label = Label(root)
result_label.pack()

formula_label = Label(root, text="")
formula_label.pack()

difference_label = Label(root, text="")
difference_label.pack()

root.mainloop()
