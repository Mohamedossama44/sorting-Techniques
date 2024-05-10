from matplotlib import pyplot as plt
from tkinter import messagebox
from tkinter import *
import numpy as np
import random
import time

def quickSort(start, end, A):

    x = random.randint(start, end) # randomized partioning
    A[start], A[x] = A[x], A[start]
    pivot = start

    while (start < end):
        if A[pivot] > A[end]:
            A[pivot], A[end] = A[end], A[pivot]
            pivot = end       ## bhafz 3l pivot yfdl l rkm l e5trto fl awl
            start = start + 1 ## kda  fy rkm etrtb mn 3l shmal f hzwd lstart
        elif A[pivot] < A[start]:
            A[pivot], A[start] = A[start], A[pivot]
            pivot = start
            end = end - 1 ## kda fy rkm etrtb mn l a5r f hn2s l end
        elif pivot == start:
            end = end - 1
        elif pivot == end:
            start = start + 1 ## lw wsl lel if dy fa kda l rkm l 3nd l start asghr mn pivot f y3tbr f mkano
    return pivot

def random_quick(start, end, A):
    if end <= start:
        return
    else:
        pivot = quickSort(start, end, A)
        random_quick(start, pivot - 1, A)
        random_quick(pivot + 1, end, A)
    return

# x = random.randint(8, 10)
# print(x)
# a=[4,6,8,2,8,1]
# print(len(a))
# random_quick(0,len(a)-1,a)
# print(a)
def random_quick_moduled(start, end, A, K):
    pivot = quickSort(start, end, A)
    if K > len(A):
        return
    else:
        if pivot + 1 == K: # since array is zero based then if we need the 5th element
            return A[pivot] # it is in the index 4 of the array --- pivot da l element f mkano l sa7
        elif pivot + 1 > K:
            return random_quick_moduled(start, pivot - 1, A, K)
        else:
            return random_quick_moduled(pivot + 1, end, A, K)

# arr500=[4,6,2,5]
# print(random_quick_moduled(0,len(arr500)-1,arr500,5))

def call_merge(A):
    mid = len(A) // 2
    if len(A) > 1:
        firstArray = A[:mid]
        secondArray = A[mid:]
        call_merge(firstArray)
        call_merge(secondArray)
        index1 = 0
        index2 = 0
        mainInd = 0
        while index1 < len(firstArray) and index2 < len(secondArray): # index1 da awl element 3l first sorted array
            if firstArray[index1] <= secondArray[index2]:             # index 2 da awl element 3l second sorten array
                A[mainInd] = firstArray[index1]                       # main index bysahwr 3la awl mkan fady fl main arrya
                mainInd += 1
                index1 += 1
            else:
                A[mainInd] = secondArray[index2]
                mainInd += 1
                index2 += 1
        while index1 < len(firstArray):
            A[mainInd] = firstArray[index1]
            mainInd += 1
            index1 += 1
        while index2 < len(secondArray):
            A[mainInd] = secondArray[index2]
            mainInd += 1
            index2 += 1
# print("merge ")
# merge_arr=[23,32,554,1,4]
# call_merge(merge_arr)
# print(merge_arr)

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  #
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):# start from the last parent till the first parent at index =0
        heapify(arr, n, i)

    # (sorting) bgeb max fl a5r
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)# agep max fo2 3lshan hhoto fl a5r next iteraion


# arr = [12, 11, 13, 5, 6, 7, ]
# print("length arr"+str(len(arr)))
# heapSort(arr)
# n = len(arr)
# print('Sorted array is')
# for i in range(n):
#     print(arr[i])


def InsertionSorter(A):
    for i in range(1, len(A)):
        j = i
        key = A[i]
        while j > 0 and key < A[j - 1]:
            A[j] = A[j - 1]
            j = j - 1
        A[j] = key

    return
# arr4 = [12, 11, 13, 5, 6, 7, ]
# InsertionSorter(arr4)
# print(arr4)
def SelectionSorter(A):
    counter = 0 # l mkan l hhaot fy asghr element && l hwa awl mkan b3tbr en hwa l minimum
    l = 0
    minimum = A[0]
    for y in range(0, len(A) - 1): # aknha A-2 l2n akhr element not inclusive
        for m in range(y + 1, len(A)):
            if A[m] <= minimum:
                minimum = A[m]
                l = m
        if A[l] <= A[counter]:
            A[l] = A[counter]
            A[counter] = minimum
            counter = counter + 1
            minimum = A[counter]
    return
#
# arr2 = [12, 11, 13, 5, 6, 7, ]
# SelectionSorter(arr2)
# print(arr2)



def hybrid_merge_selection(A, threshould):
    if len(A) <= threshould:
        SelectionSorter(A)
    elif len(A) > 1:
        mid = len(A) // 2
        firstArray = A[:mid]
        secondArray = A[mid:]
        hybrid_merge_selection(firstArray, threshould)
        hybrid_merge_selection(secondArray, threshould)
        index1 = 0
        index2 = 0
        mainInd = 0
        while index1 < len(firstArray) and index2 < len(secondArray):
            if firstArray[index1] <= secondArray[index2]:
                A[mainInd] = firstArray[index1]
                mainInd += 1
                index1 += 1
            else:
                A[mainInd] = secondArray[index2]
                mainInd += 1
                index2 += 1
        while index1 < len(firstArray):
            A[mainInd] = firstArray[index1]
            mainInd += 1
            index1 += 1
        while index2 < len(secondArray):
            A[mainInd] = secondArray[index2]
            mainInd += 1
            index2 += 1

def tester(sizes):
    b = len(sizes)

    graphlist = list([])
    first = list()
    second = list()
    third = list()
    fourth = list()
    fifth = list()

    for i in range(0, b, 1):
        unsorted = np.random.choice(1000000, sizes[i], replace=True) # replace m3nha en value x mmkn ttl3 kza mra
        res = unsorted.tolist()
        res1 = unsorted.tolist()
        res2 = unsorted.tolist()
        res3 = unsorted.tolist()
        res4 = unsorted.tolist()


        start = time.time()
        heapSort(res)
        end = time.time()
        first.append(end - start)
        print("Running time for Heap Sort of " + str(sizes[i]) + " elements is " + str((end - start)*1000) + " msec")

        start = time.time()
        InsertionSorter(res1)
        end = time.time()
        second.append(end - start)
        print("Running time for insertion Sort of " + str(sizes[i]) + " elements is " + str((end - start)*1000) + " msec")

        start = time.time()
        SelectionSorter(res2)
        end = time.time()
        third.append(end - start)
        print("Running time for Selection Sort of " + str(sizes[i]) + " elements is " + str((end - start)*1000) + " msec")

        start = time.time()
        random_quick(0, len(res3) - 1, res3)
        end = time.time()
        fourth.append(end - start)
        print("Running time for quick Sort of " + str(sizes[i]) + " elements is " + str((end - start)*1000) + " msec")

        start = time.time()
        call_merge(res4)
        end = time.time()
        fifth.append(end - start)
        print("Running time for merge Sort of " + str(sizes[i]) + " elements is " + str((end - start)*1000) + " msec")

        print("\n")

    graphlist.append(first)
    graphlist.append(second)
    graphlist.append(third)
    graphlist.append(fourth)
    graphlist.append(fifth)

    return graphlist


def plotter(sizes, graphlist):
    sorts = ["Heap sort", "Insertion sort", "Selection sort", "Quick sort", "Merge sort"]
    plt.xlabel("Size of Array")
    plt.ylabel("Time for Execution (msec)")
    plt.yticks([0, 10000, 35000, 70000, 100000])
   # plt.xticks([10, 1000, 15000, 25000, 50000])
    plt.xticks(sizes)

    plt.title("Execution Graph")
    for i in range(0, len(graphlist[0])):
        plt.plot(sizes, graphlist[i], label=sorts[i])
        for j in range(0, len(graphlist[0])):
            plt.scatter(sizes[j], graphlist[i][j], c="black")
    plt.legend() # which line represent what data ((lable))
    plt.show()


####################################
#       GUI
####################################
root=Tk()
root.geometry("300x190")
root.title("lab 1")

def run():
    sizes = [10, 5000, 10000, 15000, 20000]
    Graph = tester(sizes)
    plotter(sizes, Graph)

def kth_smallest_element():
    if(len(ent1.get())==0 and len(ent2.get())==0):
     return

    try:
        arrsize = int(ent1.get())
        k_element = int(ent2.get())
    except:
        messagebox.showinfo("ERROR","wrong values")
        return

    if(isinstance(arrsize,int) and isinstance(k_element,int) and arrsize>0 and k_element>0):
        generated_array = np.random.choice(100,arrsize, replace=True)
        res=generated_array.tolist()
        array1=str(res)
        start=time.time()
        num=random_quick_moduled(0,len(res)-1,res,k_element)
        end=time.time()
        messagebox.showinfo("Kth element", "Kth Element: " + str(num) + "\nRunning time: " + str(
            (end - start) * 1000) + "msec \n Array:" + "".join(array1))
        ent1.delete(0,END)
        ent2.delete(0,END)
    else:
        messagebox.showinfo("ERROR","wrong values")

def sort_hypird():
    if (len(ent3.get()) == 0 and len(ent4.get()) == 0):
        return

    try:
        arrsize = int(ent3.get())
        threshold = int(ent4.get())
    except:
        messagebox.showinfo("ERROR","wrong values")
        return

    if (isinstance(arrsize, int) and isinstance(threshold, int) and arrsize > 0 and threshold > 0):
        generated_array = np.random.choice(100, arrsize, replace=True)
        res1 = generated_array.tolist()
        res2 = generated_array.tolist()

        start = time.time()
        call_merge(res1)
        end = time.time()
        merge = (end - start) * 1000
        messagebox.showinfo("Merge sort only", "Time for merge sorting only is " + str(merge) + " msec")
        time.sleep(2)

        start = time.time()
        hybrid_merge_selection(res2, threshold)
        end = time.time()
        hybrid = (end - start) * 1000
        messagebox.showinfo("hybrid sort", "Time taken for the same array for hybrid is " + str(hybrid) + " msec")

        messagebox.showinfo("hybrid and merge",
                            "Time taken by merge only is " + str(merge) + "\nTime taken by hybrid is " + str(hybrid))
        ent3.delete(0, END)
        ent4.delete(0, END)
    else:
        messagebox.showinfo("ERROR","wrong values")

lb1=Label(root,text="Compare between Sorting Algorithms")
lb1.grid(row=0,column=0)

btn=Button(root,command=run,text="run",width="6",height="1",bg="black",fg="white")
btn.grid(row=0,column=1)

###################################### kth element

lblfrm=LabelFrame(root,text="Find kth smallest element")
lblfrm.grid(row=2,column=0)

lb1=Label(lblfrm,text="Size of array")
lb1.grid(row=0,column=0)

ent1=Entry(lblfrm,width=10)
ent1.grid(row=0,column=1)

lb1=Label(lblfrm,text="Kth element")
lb1.grid(row=1,column=0)

ent2=Entry(lblfrm,width=10)
ent2.grid(row=1,column=1)

btn1=Button(lblfrm,command=kth_smallest_element,text="Find",width="6",height="1",bg="black",fg="white")
btn1.grid(row=1,column=3)

################################# Hypird
lblfrm=LabelFrame(root,text="Sort using HybirdMerge")
lblfrm.grid(row=3,column=0)

lb1=Label(lblfrm,text="Size of array")
lb1.grid(row=0,column=0)

ent3=Entry(lblfrm,width=10)
ent3.grid(row=0,column=1)

lb1=Label(lblfrm,text="THRESHOLD")
lb1.grid(row=1,column=0)

ent4=Entry(lblfrm,width=10)
ent4.grid(row=1,column=1)

btn2=Button(lblfrm,command=sort_hypird,text="Sort",width="6",height="1",bg="black",fg="white")
btn2.grid(row=1,column=3)

root.resizable(0,0)
root.mainloop()