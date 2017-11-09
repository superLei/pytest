# coding:utf-8
import unittest
import types


class ListCmp():

    def listEquals(self, list1, list2):
        isEquals = True

        if list1 == None or list2 == None:
            isEquals = False

        if isEquals == True and (type(list1) != "list" or type(list2) != "list"):
                isEquals = False

        if isEquals == True and (list1.__len__() != list2.__len__()):
            isEquals = False

        if isEquals == True:
            for i in range(list1.__len__()):
                subIsEquals = list1[i] in list2
                if subIsEquals == False:
                    isEquals = False
                    break

        if isEquals == True:
            for i in range(list2.__len__()):
                subIsEquals = list2[i] in list1
                if subIsEquals == False:
                    isEquals = False
                    break

        return isEquals


    def listEqualsByDictItemKeyList(self, list1, list2, itemKeyList):
        if itemKeyList == None :
            return self.listEquals(list1, list2)

        isEquals = True

        if list1 == None or list2 == None:
            isEquals = False

        # if isEquals == True and (type(list1) != "list" or type(list2) != "list"):
        #         isEquals = False

        if isEquals == True and (list1.__len__() != list2.__len__()):
            isEquals = False

        if isEquals == True:
            for i in range(list1.__len__()):
                # if type(list1[i]) != "dict":
                #     isEquals = False
                #     break
                subIsEquals = self.dictInListByKeyList(list1[i], list2, itemKeyList)
                if subIsEquals == False:
                    isEquals = False
                    break
        if isEquals == True:
            for i in range(list2.__len__()):
                # if type(list2[i]) != "dict":
                #     isEquals = False
                #     break
                subIsEquals = self.dictInListByKeyList(list2[i], list1, itemKeyList)
                if subIsEquals == False:
                    isEquals = False
                    break

        return isEquals



    def dictInListByKeyList(self, dict1={}, list1=[], keyList=[]):
        isInList = False
        for i in range(list1.__len__()):
            item = list1[i]
            itemIsEquals = True
            for keyI in range(keyList.__len__()):
                key = keyList[keyI]
                if dict1.has_key(key)==False or item.has_key(key)==False:
                    itemIsEquals = False
                    break
                if dict1[key] != item[key]:
                    itemIsEquals = False
                    break
            if itemIsEquals == True:
                isInList = True
                break
        return isInList

#
# if __name__ == '__main__':
#     # list1, list2 = ['abc', 456], [456, 'abc']
#     list1 = [{"a":1, "b":"b", "c":3}]
#     list2 = [{"b":"b", "a":1}]
#     # list1 = [{"a":1}]
#     # list2 = [{"a":1}]
#     keyList = ["a", "b", "c"]
#     print ListCmp().listEqualsByDictItemKeyList(list1, list2, keyList)




