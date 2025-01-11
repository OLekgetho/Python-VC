class Beginner:
    def evennum(self, numbers):
        for x in numbers:
            if x % 2 == 0:
                print(x)

    def sumpos(self,numbers):
        i = 0
        positive = 0
        while i < len(numbers):
            if numbers[i] > 0:
                positive += numbers[i]
            i += 1
        print(positive)

    def counta(self,words):
        count = 0
        for x in words:
            if "a" in x :
                count += 1
        print(count)

class Intermediate:

    def maximum(self,numbers):
        curr = numbers[0]
        for x in numbers:
            if x > curr:
                curr = x
        print(curr)

    def reverse(self,items):
        curr = []
        x = len(items) - 1
        while x >= 0:
            curr.append(items[x])
            x -= 1
        print(curr)

    def cummulative(self,numbers):
        new = []
        sum = 0
        for x in numbers:
            sum += x
            new.append(sum)
        print(new)

class Advanced:

    def multiplication(self):
        first = []

        for x in range(1, 11):
            second = []
            for y in range(1, 11):
                mult = x * y
                second.append(mult)
            first.append(second)
        print(first)

    def filsort(self, numbers):
        new = []
        for x in numbers:
            if x > 50:
                new.append(x)
        new.sort()
        print(new)

    def duplicate(self, numbers):
        seen = []
        dup = []

        for x in numbers:
            if x in seen:
                dup.append(x)
            else:
                seen.append(x)
        print(dup)

    def mermove(self, list1, list2):
        seen = []
        for x in list2:
            list1.append(x)

        for x in list1:
            if x in seen:
                continue
            else:
                seen.append(x)
        seen.sort()
        print(seen)


if __name__ == '__main__':
    advanced = Advanced()
    words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
    numbers = [1, 2, 3, 2, 4, 5, 3, 6, 7, 4]
    items = [1, 2, 3, 4, 5, 93]
    list1 = [1, 3, 5, 7, 9]
    list2 = [2, 3, 5, 8, 10]
    advanced.mermove(list1, list2)

    


