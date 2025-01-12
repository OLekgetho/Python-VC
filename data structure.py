class Datatructure:
    def staticarray(self):
        from arrays.unsorted_array import UnsortedArray
        unsorted_array = UnsortedArray(max_size=5,typecode='i')
        unsorted_array.insert(10)
        unsorted_array.insert(30)
        unsorted_array.insert(2)
        unsorted_array.insert(3)
        unsorted_array.insert(50)

        print(f"Initial array: {unsorted_array}")

        index = unsorted_array.find(50)
        print(f"Element 50 found at index: {index}")

        unsorted_array.traverse(lambda x: print(f"Element: {x}"))

        max_min_min = unsorted_array.max_and_min_in_array()

        print(max_min_min)



if __name__ == '__main__':
    datastructure = Datatructure()
    datastructure.staticarray()