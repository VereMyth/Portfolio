# Jeremy Beam 2502798
#Prompt for hourly pay and rate
#Ensure floats
#Calculate regular pay
#calculate overtime pay
#Display overtime pay.
def main():
    #Variable declartions
    
    REG_HOURS = 40 #base work week
    
    OT_MULTI = 1.5 #Time and a half Over time
    
    #prompt for input
    
    payrate = float(input('Enter hourly pay rate '))
    
    hours = float(input('Enter hours worked '))
    #calculate base pay
    pay = payrate * REG_HOURS #Normal pay rate

    #calculate calculate overtime pay if applicable
    if hours > REG_HOURS:
        
        overtime_hours = hours - REG_HOURS #calculating overtime
        
        overtime_pay = overtime_hours * payrate * OT_MULTI #overtime pay

        total_pay = payrate * REG_HOURS + overtime_pay #total pay with overtime
    else:       
        overtime_pay = 0
        total_pay = payrate * REG_HOURS + overtime_pay
    #output
    print(f'Regular pay: ${pay:,.2f}')
    print(f'Overtime pay: ${overtime_pay:,.2f}')
    print(f'Total pay is: ${total_pay:,.2f}')
        
   
        




main()
