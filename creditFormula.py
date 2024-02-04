from datetime import datetime, timedelta
import customtkinter

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

root = customtkinter.CTk()

root.geometry("500x400")





cost_label =   customtkinter.CTkLabel(root, text="Enter plan cost:", font=("Arial", 20), text_color="#FFCC70")
cost_label.pack()

cost_entry = customtkinter.CTkEntry(root)
cost_entry.pack()

start_label = customtkinter.CTkLabel(root, text="Enter start date (YYYY-MM-DD):",  font=("Arial", 20), text_color="#FFCC70")
start_label.pack()

start_entry = customtkinter.CTkEntry(root)
start_entry.pack()

end_label = customtkinter.CTkLabel(root, text="Enter end date (YYYY-MM-DD):", font=("Arial", 20), text_color="#FFCC70" )

end_label.pack()
end_entry = customtkinter.CTkEntry(root)
end_entry.pack()

calculate_button = customtkinter.CTkButton(root, text="Calculate", command=credit, corner_radius=32, fg_color="#C850C0", hover_color="#4158D0", border_color="#FFCC70", border_width=4)

calculate_button.pack()


formula_label = customtkinter.CTkLabel(root, text="")
formula_label.pack()

difference_label = customtkinter.CTkLabel(root, text="")
difference_label.pack()

root.mainloop()
