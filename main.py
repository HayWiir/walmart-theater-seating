from black import out
from theater import *

if __name__ == "__main__":
    
    theater = Theater()

    with open('input.txt', 'r') as reader:
        input = reader.read().splitlines()

    input_dict = {i.split()[0]:int(i.split()[1]) for i in input}    

    output_dict = {}

    for booking,num_tickets in input_dict.items():
        output_dict[booking] = theater.reserve(num_tickets)

    with open('output.txt', 'w') as writer:
        for booking, reservation in output_dict.items():
            out = f"{booking} {', '.join(reservation)}\n"
            writer.write(out)