
class MoveRecord:
    def __init__(self, name, fromAddress, toAdress, miles, moveDate, selfPacking):
        self.name = name
        self.fromCity = fromAddress
        self.toCity = toAdress
        self.moveDate = moveDate
        self.miles = miles
        self.selfPacking = selfPacking
    
    def calculateTotalCost(self):
        packingCost = 500
        moveCost = self.calculateMoveCost()
        if self.selfPacking == 'no':
            return  moveCost + packingCost
        return moveCost

    # this would be a private method
    def calculateMoveCost(self):
        costPerMile = 10
        return costPerMile * self.miles

mr1 = MoveRecord('Rekha','75254','75259', 10, '12/13/2022', 'yes')
print(f'Cost of move: ${mr1.calculateTotalCost()}')
mr2 = MoveRecord('LazyRekha','75254','75259', 10, '12/13/2022', 'no')
print(f'Cost of move with packing: ${mr2.calculateTotalCost()}')

