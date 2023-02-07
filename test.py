def sorteren(lst):
    lijst = []
    for i in lst:
        lijst.append(i)
    print(lijst)
    def sort():
        for i in range(len(lijst)-1):
            if lijst[i] > lijst[i+1]:
                print(lijst[i])
                lijst[i], lijst[i+1] = lijst[i+1], lijst[i]
                sort()
    sort()
    return lijst



print(sorteren([-53, -92, 61, 77, 78, -25]))


