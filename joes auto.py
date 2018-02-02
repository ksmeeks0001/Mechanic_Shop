from tkinter import*
import webbrowser
from time import gmtime , strftime
class Mechanic():

    def __init__(self):
        self.root = Tk()
        self.root.title('Mechanic Shop')

        #frames
        self.frame_left = Frame(self.root)
        self.frame_right = Frame(self.root)
        self.frame_center = Frame(self.root)
     
        #variables for checks
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        self.var7 = IntVar()

        #set
        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)
        self.var7.set(0)
    
        #check buttons
        self.chb1 = Checkbutton(self.frame_left, text = 'Oil Change' ,
                                variable = self.var1)
        self.chb2 = Checkbutton(self.frame_left, text = 'Lube Job' ,
                                variable = self.var2)
        self.chb3 = Checkbutton(self.frame_left, text = 'Radiator Flush' ,
                                variable = self.var3)
        self.chb4 = Checkbutton(self.frame_left, text = 'Transmission Flush' ,
                                variable = self.var4)
        self.chb5 = Checkbutton(self.frame_left, text = 'Inspection' ,
                                variable = self.var5)
        self.chb6 = Checkbutton(self.frame_left, text = 'Muffler Replacement' ,
                                variable = self.var6)
        self.chb7 = Checkbutton(self.frame_left, text = 'Tire Rotation' ,
                                variable = self.var7)
        
        #pack checks
        self.chb1.pack(side= TOP)
        self.chb2.pack(side=TOP)
        self.chb3.pack(side=TOP)
        self.chb4.pack(side=TOP)
        self.chb5.pack(side=TOP)
        self.chb6.pack(side=TOP)
        self.chb7.pack(side=TOP)

       

       
        #pack frames
        self.frame_left.pack(side=LEFT)
        self.frame_center.pack(side=LEFT)
        self.frame_right.pack(side=RIGHT)

         #buttons
        self.print_button = Button(self.frame_center, text = 'PRINT',
                                   command = self.receipt)
                                   
        self.print_button.pack(side = BOTTOM)

        self.tender_button = Button(self.frame_center, text = 'TENDER',
                                    command = self.tender)
        self.tender_button.pack(side=BOTTOM)

        


        self.price_button = Button(self.frame_center, text = 'TOTAL',
                                   command = self.show_total)
        self.price_button.pack(side=BOTTOM)

        

        

        

         #LABEL to show total
        self.price = StringVar()
        self.label = Label(self.frame_right, textvariable = self.price)
        self.label.pack(side=TOP)

        self.price.set('SUB $' + '0' + '\nTAX $' + '0' +
                       '\nTOTAL $' + '0')

        #customer pay entry
        self.pay_entry = Entry(self.frame_right)
        self.pay_entry.pack(side=TOP)


        #change label
        self.change = StringVar()
        self.change_label = Label(self.frame_right,
                                  textvariable=self.change)
        self.change_label.pack(side=TOP)
        self.change.set('----------\nChange Due: 0')

        self.total = 0 #initialize total
        self.tax = self.total * .06
        self.customer_paid = 0 #intialize customer paid
        self.change_due = 0
        self.root.mainloop()
        
    def show_total(self):
        self.total = 0
        #check if checks buttons are on/off
        #add to total if check button on
        if self.var1.get() == 1: 
            self.total += 30
        if self.var2.get() == 1:
            self.total += 20
        if self.var3.get() == 1:
            self.total += 40
        if self.var4.get() == 1:
            self.total += 100
        if self.var5.get() == 1:
            self.total += 35
        if self.var6.get() == 1:
            self.total += 200
        if self.var7.get() == 1:
            self.total += 20
        
        self.tax = self.total * .06
        self.price.set('SUB $' + str(self.total) + '\nTAX $' +
                       str(format(self.tax,'.2f')) +
                       '\nTOTAL $' + str(format(self.total + self.tax, '.2f')))

           
                
         
    def receipt(self):
           #write info to a text doc for printing  
        name = str(strftime("%Y-%m-%d %H %M %S", gmtime())) + '.txt'
        receipt = open(name , 'w') 
        receipt.write("Joe's Mechanic Shop\n") #header
            #print individual services performed
        if self.var1.get() == 1: 
                receipt.write('\nOil Change $30')
        if self.var2.get() == 1:
                receipt.write('\nLube Job $20') 
        if self.var3.get() == 1:
                receipt.write('\nRadiator Flush $40')
        if self.var4.get() == 1:
                receipt.write('\nTransmission Flush $100')
        if self.var5.get() == 1:
                receipt.write('\nInspection $35')
        if self.var6.get() == 1:
                receipt.write('\nMuffler Replcament $200')
        if self.var7.get() == 1:
                receipt.write('\nTire Rotation $20')

           #print subtotal tax and total
        receipt.write("\n\n\tSUB: $" + str(self.total) +
                      '\n\tTAX: $' + str(format(self.tax, '.2f')) +
                         '\n\tTOTAL: $' + str(format(self.total +
                                             self.tax, '.2f')))
        if self.customer_paid == 'card':
            receipt.write("\n\n-----------------------\nChange Due: CASHLESS")
        else:         
            receipt.write("\n\n-----------------------\nChange Due: " +
                        str(format(self.change_due, '.2f')))
        receipt.close()
    
        webbrowser.open(name)
                      
    def tender(self):
        self.customer_paid = self.pay_entry.get()
        if self.customer_paid != 'card':            
            self.change_due = float(self.customer_paid)- (self.total + self.tax)
            self.change.set('----------\nChange Due: ' +
                            str(format(self.change_due, '.2f')))
                               
                      
Joes = Mechanic()

