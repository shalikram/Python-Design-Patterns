
class Property:
    def DocumentFactory(self):
        return self.ConcreteDocumentFactory()

class House(Property):
    def ConcreteDocumentFactory(self):
        return HouseRentalDocument()

class Flat(Property):
    def ConcreteDocumentFactory(self):
        return FlatRentalDocument()

class Document:
    title = "Lease Agreement"

class HouseRentalDocument(Document):
    def __init__(self):
        self.title = "House Lease Agreement"

class FlatRentalDocument(Document):
    def __init__(self):
        self.title = "Apartment Lease Agreement"

if __name__ == '__main__':
    # Test : House
    house = House()
    doc = house.DocumentFactory()
    print 'House Document Title: ', doc.title

    # Test : Flat
    flat = Flat()
    doc = flat.DocumentFactory()
    print 'Flat Document Title: ', doc.title