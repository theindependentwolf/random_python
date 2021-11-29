import whois

def get_animal_names():
    with open('animalnames.txt') as f:
        lines = f.read().splitlines()
        return lines


def check_domain_availability(domain_check_list):
    available_list = []
    for domain in domain_check_list:
        try:
            domain_info = whois.whois(domain)
            print('domain: ', domain, ' is taken.')            
        except:
            print('domain: ', domain, ' is available.')
            available_list.append(domain)

    print(available_list)

prefix = 'nft'
suffix_list = get_animal_names()
domain_check_list = [prefix + suffix + '.com' for suffix in suffix_list if ' ' not in suffix]
check_domain_availability(domain_check_list)