class Student:

    def __init__(self, roll, name, age):
        self.roll = roll
        self.name = name
        self.age = age

    def __str__(self):
        return "{} \t {} \t {}".format(self.roll, self.name, self.age)

class HashTable:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = []

        for i in range(0, capacity):
            self.buckets.append(None)

    def hashFunction(self, key):
        hashCode = key % self.capacity
        return hashCode

    def put(self, student):



        key = student.roll+student.age
        index = self.hashFunction(key)
        added = False

        if self.buckets[index] ==None:
            self.buckets[index] = student
            print(">> Student Added at index:", index, "Details:", student)

        else:
            while added !=True:
                if index <len(self.buckets)-1:
                    index +=1
                else:
                    index=0
                if self.buckets[index] == None:
                    self.buckets[index] = student
                    print(">> Student Added at index:", index, "Details:", student)
                    added =True
        self.size += 1

    def contains(self, student):

        key = student.roll + student.age
        index = self.hashFunction(key)
        Found =False
        if self.buckets[index]!= student:
            print("Found --> ", student)

        else:
            while Found !=True:

                if index <len(self.buckets)-1:
                    index +=1
                else:
                    index=0

                if self.buckets[index] == student:
                    print("Found --> " , student)

    def iterate(self):
        pass
        # # output will be unordered due to hashing :(
        for i in range(0, len(self.buckets)):
            if self.buckets[i]!= None:
                print(">> Iterating in Bucket:", i)
                print(self.buckets[i])

            print("~~~~~~~~~~~~~~~~~~~~~~~~")


    def remove(self, student):
        pass
        # key = student.roll + student.age
        # index = self.hashFunction(key)
        # if len(self.buckets[index]) != 0:
        #     self.buckets[index].remove(student)
        #     print("Student Removed")
        #     self.iterate()



s1 = Student(101, "John", 23)
s2 = Student(111, "Jen", 21)
s3 = Student(197, "Jim", 24)
s4 = Student(153, "Jack", 25)
s5 = Student(121, "Joe", 27)
s6 = Student(111, "Jain", 27)



hTable = HashTable()
hTable.put(s1)
hTable.put(s2)
hTable.put(s3)
hTable.put(s4)
hTable.put(s5)
hTable.put(s6)
hTable.iterate()
print()
hTable.contains(s6)


