
# "بسم الله مجراها ومرساها"

class Category:
    # the constructor method
    def __init__(self, name):
        self.ledger = []
        self.name = name

    # get the object's readable format 
    def __str__(self):
        side_stars = ((30 - len(self.name)) // 2) * '*' 
        if ((30 - len(self.name)) % 2) != 0: 
            title = f'{side_stars}{self.name}{side_stars}*\n' 
        else: title = f'{side_stars}{self.name}{side_stars}\n' 
        total = 0
        items = ''
        for item in self.ledger:
# TO BE INSPECTED ... !
            items += f"{item['description'] [0:23]:23}{item['amount']:>7.2f}" + '\n'
            
            total += item['amount']
        
        result = title + items + f"Total: {total}"
        return result

    # deposite into category
    def deposit(self, amount, description=''):
       
        self.ledger.append({'amount': amount, 'description': description})
        
    # withdraw from category
    def withdraw(self, amount, description=''):
        self.amount = amount
        self.description = description
        if self.check_funds(amount):
            self.ledger.append({'amount': 0 - amount, 'description': description})
            return True
        else:
            return False
             
    
    # get current balance after tansactions (deposits & withdrawals = elements)
    def get_balance(self):
        balance = 0
        for element in self.ledger:
            balance += element['amount']  #checked...  element is officially a dict object.
        return balance

    # transfer balance to another category (self to new_category)
    def transfer(self, amount, new_category):
        if self.check_funds(amount):
            self.withdraw(amount,f'Transfer to {new_category.name}')
            new_category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    # inspect balance for withdrawals/transfers
    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False

    

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for desert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(30, 'winter Jacket')
# extra = Category('extra')
# extra.deposit(999)
# extra.withdraw(99, 'Mourinho')
# Check objects .. 
#print(food,'\n'*2, clothing, '\n'*5) 





def create_spend_chart(categories):
    
    
    # I. get category percentage of spending 
    total = 0
    
    # 1. get spendings of each category
    spendings = {} 
    for category in categories:
        spending_total = 0                  
        for dict_ in category.ledger:
          if dict_['amount'] < 0:
              spending_total += abs(dict_['amount'])
        spendings[category.name] = round(spending_total, 2)
        total += spending_total   
        total = round(total, 2)

    # 2. turn spendings into percentages based on total + (round down) 
    percentages = {}
    for category, spending in spendings.items():
        try:
            percentages[category] = (spending * 100) // total
            percentages[category] -= percentages[category] % 10
        except ZeroDivisionError:
            percentages[category] = 0
        #     raise ZeroDivisionError('What do you need a spend chart for if your spendings were Zero? Spend some money and try agian')
    
    # check
    #print('percentages: ', percentages)        
    
    # overall = 0
    # for value in percentages.values():
    #     overall += value
    # if overall < 100:
    #     percentages['Auto'] = 10
    

    # if percentages[category] % 10 > 5:
    # percentages[category] += 10 - (percentages[category] % 10)
    # else:

    # main str  
    title = 'Percentage spent by category\n'
    spend_chart = title + ""

    # display 0| - 100| + o
    for num in reversed(range(0, 101, 10)):
        spend_chart += f'{num}|'.rjust(4)
        for category in categories:
            if percentages[category.name] >= num:
                spend_chart += ' o '
            else:
                spend_chart += '   '
        
        spend_chart +=' \n'

    # scores line
    cust_scores = '-' * (len(categories)*3 + 1 )
    line =f'    {cust_scores}'
    spend_chart += line 
    
# TO BE INSPECTED ... !   
    # category vert names
    max_index = max([len(cat.name) for cat in categories])
    
    for index in range(max_index):
        line = ''
        for i, category in enumerate(categories):
            try:
                line += category.name[index]
            except IndexError :
                line +=  ' '
            if i < len(categories) - 1:
               line += '  '
        spend_chart += '\n     ' + line
        spend_chart += '  '



    return spend_chart.rstrip('\n')
    

# tests
#print('total spendings:\n', total)

print(create_spend_chart([clothing, food]))
#print('clothing: ', clothing)
#print(food, '\n' * 3, food.ledger)
#print(print('print call printed'))

