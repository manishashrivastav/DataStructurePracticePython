# class Product:
#     def __init__(self , pid , name , price):
#         self.pid = pid
#         self.name = name
#         self.price = price

class Product:
    def __init__(self , data):
        self.data = data

class Stack:

    size = 0
    total = 0
    items = 0

    def __init__(self):
        # print(">> Stack Object Constructed")
        self.head = None
        self.current = None

    # Circular
    def push(self, object):

        # Stack.size += 1
        # Stack.items += object.quantity
        # Stack.total += (object.price * object.quantity)

        # print(">> object is:", object)
        object.next = None
        object.previous = None
        # print(">> object dictionary is:", object.__dict__)
        print()

        if self.head == None:
            self.head = object
            self.current = object
            # print("---------------------------------")
            # print(">> object added at head:", object)
            # print("---------------------------------")
        else:
            self.current.next = object
            object.previous = self.current

            self.head.previous = object

            self.current = object
            self.current.next = self.head

            # print(">> NEXT {} PREVIOUS {} and Data is {}".format(object.next, object.previous , object.previous.data))


    def pop(self):

        if self.head.previous != self.head:
            Stack.size -= 1
            temp = self.current
            self.current = temp.previous
            self.head.previous = self.current
            self.current.next = self.head

            return temp
        else:
            self.head = None
            self.current = None
            return None


class tree:
    sRef = Stack()
    def __init__(self):
        self.root = None
        # self.current = None

    def preOrderTraversal(self):
        temp = self.root
        print(temp.data )

        self.printNode(temp  )



    def printNode(self, temp ):

        # if temp.left != None:

        if temp.right != None:
            tree.sRef.push(Product(temp.right.data))
            # print("Node Added to Stack",temp.right.data)
        if temp.left != None:
            print(temp.left.data)

            self.printNode(temp.left )
        else:

            right =tree.sRef.pop()
            if right!=None:
                 print(right.data)

            self.printNode(temp)



    def insert(self , object):
        object.left = None
        object.right = None
        NodeAdded = False

        if self.root==None:
            self.root = object
            # self.current = object
            print("Root ", self.root.data)


        else:
            temp = self.root

            self.InsertAhead(object , NodeAdded , temp)
            # temp = self.root
            #
            # while NodeAdded != True:
            #     if temp.data > object.data:
            #         if temp.left ==None:
            #             temp.left = object
            #             print("Left Side of " ,temp.data ,"is ",object.data)
            #             NodeAdded= True
            #         else :
            #             temp = temp.left
            #     else:
            #         if temp.right ==None:
            #             temp.right = object
            #             print("Right Side " ,temp.data,"is ",object.data)
            #             NodeAdded= True
            #         else :
            #             temp = temp.right


    def InsertAhead(self , object , NodeAdded , temp):


        if temp.data > object.data:
            if temp.left ==None:
                temp.left = object
                print("Left Side of " ,temp.data ,"is ",object.data)
                NodeAdded= True
                return NodeAdded

            else :
                self.InsertAhead(object, NodeAdded , temp.left)
        else:
            if temp.right ==None:
                temp.right = object
                print("Right Side " ,temp.data,"is ",object.data)
                NodeAdded= True
                return NodeAdded

            else :
                self.InsertAhead(object , NodeAdded , temp.right)



tRef = tree()
tRef.insert(Product(40))
tRef.insert(Product(20))
tRef.insert(Product(50))
tRef.insert(Product(30))
tRef.insert(Product(25))
tRef.insert(Product(95))
tRef.insert(Product(15))


# tRef.preOrderTraversal()
