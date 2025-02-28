# li = ["eat","tea","tan","ate","nat","bat"]


def anagram_generator(sequence) -> list:
    asci_dict = {} 

    for word in sequence:
        temp_list = [0] * 26

        for character in word:
            temp_list[(ord(character) % 97)] += 1
        dict_key = tuple(temp_list)

        if dict_key in asci_dict:
            asci_dict[dict_key].append(word)

        else:
            asci_dict[dict_key] = [word]
            
    return list(asci_dict.values())


if __name__ == '__main__':
        
    words = input("Enter words seperated by space : ")

    li = words.split(' ')

    print(anagram_generator(li))