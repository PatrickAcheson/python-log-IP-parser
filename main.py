import operator

#Patrick Acheson

def analyse_logs(file_open, list_ip):
    #reads in and opens the string in file varible
    with open(file_open, 'r') as file:
        #loops through each line of the file
        for line in file.readlines():
                #adds the first 14 characters to a list
                list_ip.append(line[:14])
        return list_ip


def extract_ip(list_ip, dic):
    #turns list_ip into a set called final list
    #this removes duplicate values
    final_list = set(list_ip)
    #loops through set
    for i in final_list:
        #counts amount of times i appears and defines as x
        x = list_ip.count(i)
        #updates dic with key and item x and i
        dic.update({i:x})
    return x , i


def find_most_frequent(dic):
    #sorts the dic by item into highest to lowest (using revese true)
    sorted_final = dict(sorted(dic.items(), key=operator.itemgetter(1), reverse=True))
    return sorted_final


def display_data(file_open, sorted_final):
    #creates a pair varible using items in set list
    first_pair = next(iter((sorted_final.items())))
    #prints the file open varible along side the index of each pair
    print(f"{file_open} contains the IP address {first_pair[0]} {first_pair[1]} times.")
    print("-" * 100)


def main():
    #defines the file to be used
    file_open = 'full_log.txt'  
    #defines list and dic varibles
    list_ip = []
    dic = {}

    print("-" * 50)
    print("LOG ANALYSIS SCRIPT")
    print("-" * 100)
    #fuctions that are run from main in order of interpreted
    analyse_logs(file_open, list_ip)
    extract_ip(list_ip, dic)
    sorted_final = find_most_frequent(dic)
    display_data(file_open, sorted_final)

#run main always first even from outwith main.py
if __name__ == "__main__":
    main()