
""" This file contains a script which reads product information from a text and a CSV file and dumps it into a JSON file """

import json
import os
import csv
import pickle



""" This function reads the product information from a text file and dumps it into a dictionary
"""
def read_textFile():
    products_info={}
    try:
        file_size = os.path.getsize("products.txt")
        print(file_size)
        # if file size is 0, it is empty
        if (file_size == 0):
            print("File is empty")
        else:
            with open("products.txt",'r') as filereader:
                for lines in filereader:
                    if lines == "\n":
                        print("found empty line")
                    elif "Product ID" or "Name" or "Price" or "In Stock" in lines:
                        if ':' in lines:
                            lis_product=lines.split(":")
                            products_info[lis_product[0]]=lis_product[1].strip()
                        else:
                            print("Incorrect data format: Details missing in the line")
                    else:
                        print("None of the product details available in the line")  
            return products_info
    except FileNotFoundError:
        print("File not found or wrong path")


""" This function reads the product information from a CSV file and dumps it into a list of dictionaries
"""
def read_csvFile():
    products_list=[]
    try:
        file_size = os.path.getsize("products.txt")
        print(file_size)
        # if file size is 0, it is empty
        if (file_size == 0):
            print("File is empty")
        else:
            with open('products.csv', newline='')as file:
                csvFile = csv.DictReader(file)
                for row in csvFile:
                    products_list.append(row)
        return products_list
    except FileNotFoundError:
        print("File not found or wrong path")


""" This function dumps the unified data into a JSON file
"""
def dump_productsInfo_json(dict,list):
    if(os.path.isfile("output.json")):
        os.remove("output.json")
    print("The final text file data is......")
    print(dict)
    print("The final CSV file data is......")
    print(list)
    dict_list=[dict,list]
    with open("output.json", "w") as outfile: 
        json.dump(dict_list, outfile)
        print(json.dumps(dict_list, indent=4, separators=(',', ': ')))


# This is a main function
def main():
    print("Looking for a text file name products.txt..........")
    products_info_text=read_textFile()
    print("Looking for a CSV file name products.csv..........")
    products_Info_CSV= read_csvFile()
    print("dumping python objects into JSON file")
    dump_productsInfo_json(products_info_text, products_Info_CSV)
    


if __name__=="__main__":
    main()