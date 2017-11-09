import json
import hashlib

if __name__ == "__main__":
    excelDate_input = "{\"sign\":\"\",\"timestamp\":\"1498548999\",\"reason\":\"adfa\",\"groupID\":\"306\",\"status\":\"2\",\"shopID\":\"76023028\",\"orderID\":\"2017149854899923750\",\"platforms\":\"meituan\"}"
    excelDate_input = json.loads(excelDate_input)

    del excelDate_input["sign"]
    list = []
    for key, value in excelDate_input.items():
        if value is not None:
            temp = key + value
            list.append(temp)
    list.sort()
    result = "".join(list)

    __md5_encryption = hashlib.md5()
    __md5_encryption.update(result)

    print __md5_encryption.hexdigest()
