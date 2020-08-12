def getChildXpath(self, xpathObj, listObj):
    x = []
    for i in listObj:
        x.append(xpathObj.xpath(i))
    all_lists = sum(x, [])
    return all_lists
    
def ordered_set(self, alist):
    # Creates an ordered set of unique items
    mmap = {}  # implements hashed lookup
    oset = []  # storage for set

    for item in alist:
    # Save unique items in input order
        if item not in mmap:
            mmap[item] = 1
            oset.append(item)
    return oset
