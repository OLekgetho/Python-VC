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

    def evennum(self,numbers):
        even = []
        for x in numbers:
            if x % 2 == 0:
                even.append(x)
            else:
                continue
        print(even)

    def multiply(self,numbers):
        curr = 1
        for x in numbers:
            curr = x * curr
        print(curr)

    def largest(self,numbers):
        curr = 0
        for x in numbers:
            if x > curr:
                curr = x
            else:
                continue
        print(curr)

    def occur(self, numbers):
        occur = 0
        for x in numbers:
            if x == 3:
                occur += 1
            else:
                continue
        print(occur)

    def str(self, words):
        four = []
        for x in words:
            length = len(x)
            if length > 4:
                four.append(x)
            else: continue
        print(four)

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

    def reverses(self, items):
        end = len(items) - 1
        new = []
        x = 0
        while x <= end:
            new.append(items[end])
            end -= 1
        print(new)

    def neg(self, numbers):
        curr = 0
        leng = len(numbers) - 1
        x = 0
        while x < leng:
            if numbers[x] < 0:
                curr = numbers[x]
            x += 1

        print(curr)

    def cumm(self,numbers):
        curr = 1
        leng = len(numbers) - 1
        x = 0
        while x <= leng:
            curr = numbers[x] * curr
            x += 1
        print(curr)

    def sumodd(self,numbers):
        curr = 0
        leng = len(numbers)-1
        x = 0
        while x <= leng:
            if numbers[x] % 2 != 0:
                curr = numbers[x] + curr
            x += 1
        print(curr)

    def zero(self, numbers):
        num = []
        leng = len(numbers) - 1
        x = 0
        while x <= leng:
            if numbers[x] != 0:
                num.append(numbers[x])
            x += 1
        print(num)

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

    def common(self, list1, list2):
        com = []
        for x in list2:
            if x in list1:
                com.append(x)
        print(com)

    def vowels(self, text):
        new = text.lower()
        vowels = ["a","e","i","o","u"]
        vowelcount = 0
        for x in new:
            if x in vowels:
                vowelcount += 1
        print(vowelcount)

    def square(self, numbers):
        square = []
        for x in numbers:
            x **= 2
            square.append(x)
        print(square)

    def group(self,numbers):
        even = []
        odd = []
        x = 0
        leng = len(numbers)-1
        while x <= leng:
            if numbers[x] % 2 == 0:
                even.append(numbers[x])
            else:
                odd.append(numbers[x])
            x += 1
        print(even,odd)

    def palindrom(self,words):
        word = []
        for x in words:
            reverse = x[::-1]
            if reverse == x:
                word.append(x)
            else:
                continue
        print(word)

class Complex:

    def unique(self, numbers):
        count = 0
        seen = []
        for x in numbers:
            if x not in seen:
                seen.append(x)
                count += 1
            else:
                continue
        print(count)

    def nested(self, numbers):
        single = []
        for x in numbers:
            for y in x:
                single.append(y)
        print(single)

    def freq(self,numbers):
        seen = {}
        for x in numbers:
            if x not in seen:
                seen[x] = 1
            else:
                seen[x] += 1
        print(seen)

    def table(self,n):
        table = []
        for x in range(1,11):
            num = x * n
            table.append(num)
        print(table)

    def element(self,items):
        last = items[-1]
        for x in range(len(items) -1 , 0, -1):
            items[x] = items[x -1]
        items[0] = last
        print(items)









if __name__ == '__main__':
    complex = Complex()
    advanced = Advanced()
    beginner = Beginner()
    intermediate = Intermediate()
    items = [10, 20, 30, 40, 50]
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    n = 7
    complex.element(items)

    


