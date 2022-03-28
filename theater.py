
class Theater:

    def __init__(self):
        self.rows = 10
        self.seats_in_row = 20
        self.buffer = 3

        self.available_seats = [self.seats_in_row for row in range(self.rows)]

        self.reservations = [[] for i in range(self.rows)]

        self.preferred_rows = [5, 6, 4, 7, 8, 3, 9, 2, 1, 0]
        self.row_mapping = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J'}



    def available_ranges(self, row, buffer=0):
        """
        Returns ranges of seats which can be reserved for a given row.
        Buffer can be added optionally. 
        """
        row_reservations = self.reservations[row]

        ranges = []
        curr_start = 0
        end = self.seats_in_row-1

        for reservation in row_reservations:  #iterate over existing reservations to get empty seats
            if reservation[0]!=curr_start:
                ranges.append([curr_start, reservation[0]-1-buffer])

            curr_start = reservation[1]+1+buffer

        if len(row_reservations)>0:  #handle edge cases (No reservations, reservations at end)
            if row_reservations[-1][1]!=end and curr_start<=end:
                ranges.append([curr_start, end])
        else:
            ranges.append([curr_start, end])        

        return ranges


    def add_reservation(self, row, reservation_range):
        row_reservations = self.reservations[row]

        row_reservations.append(reservation_range)
        row_reservations.sort(key=lambda x: x[0])
        self.available_seats[row] -= (reservation_range[1] - reservation_range[0] + 1)

        #merge    
        i=0
        while(i<len(row_reservations)-1):
            curr = row_reservations[i]
            next = row_reservations[i+1]

            if curr[1]+1==next[0]:
                curr[1] = next[1]
                row_reservations.pop(i+1)
            else:
                i+=1

        self.reservations[row] = row_reservations        
    
    
    
    def reserve_in_range(self, num_seats, available_ranges):
        """
        Given a list of available ranges and buffer, return reservation range.
        Returns None if allocation not possible
        """
        for range in available_ranges:
            len_range = range[1] - range[0] + 1
            if num_seats > len_range:
                continue
            else:
                start_seat = range[0]
                end_seat = start_seat + num_seats - 1
                return [start_seat, end_seat]

        return None

    def reserve(self, num_seats):
        """
        Reserves number of seats specified and returns the seat numbers.
        Returns None if allocation not possible.

        Logic: Try to allocate a) seats together in preferred rows with buffers. 
                               b) seats together in preferred rows without buffers.
                               c) seats separately
        """

        if num_seats > sum(self.available_seats):
            return []

        #With Buffer
        for current_row in self.preferred_rows:
            if num_seats > self.available_seats[current_row]:
                continue

            else:
                available_ranges = self.available_ranges(current_row, self.buffer)
                reserved_range = self.reserve_in_range(num_seats, available_ranges)
                
                if reserved_range != None:
                    self.add_reservation(current_row, reserved_range)
                    reservation = [f"{self.row_mapping[current_row]}{i+1}" for i in range(reserved_range[0], reserved_range[1]+1)]
                    return reservation
        
        #Without buffer
        for current_row in self.preferred_rows:
            if num_seats > self.available_seats[current_row]:
                continue

            else:
                available_ranges = self.available_ranges(current_row)
                reserved_range = self.reserve_in_range(num_seats, available_ranges)
                
                if reserved_range != None:
                    self.add_reservation(current_row, reserved_range)
                    reservation = [f"{self.row_mapping[current_row]}{i+1}" for i in range(reserved_range[0], reserved_range[1]+1)]
                    return reservation

        #Separately with buffer
        reservation = []
        reservations_copy = self.reservations.copy()
        num_seats_copy = num_seats

        for current_row in self.preferred_rows:
            available_ranges = self.available_ranges(current_row, self.buffer)
            for seat_range in available_ranges:
                possible_seats = seat_range[1] - seat_range[0] + 1

                if possible_seats > num_seats:
                    seat_range[1] = seat_range[0] + num_seats - 1
                    possible_seats = num_seats
                
                self.add_reservation(current_row, seat_range)
                reservation += [f"{self.row_mapping[current_row]}{i+1}" for i in range(seat_range[0], seat_range[1]+1)]
                num_seats -= possible_seats

                if num_seats==0:
                    return reservation

        self.reservations = reservations_copy
        num_seats = num_seats_copy


        #Separately without buffer
        reservation = []
        reservations_copy = self.reservations.copy()
        num_seats_copy = num_seats

        for current_row in self.preferred_rows:
            available_ranges = self.available_ranges(current_row)
            for seat_range in available_ranges:
                possible_seats = seat_range[1] - seat_range[0] + 1

                if possible_seats > num_seats:
                    seat_range[1] = seat_range[0] + num_seats - 1
                    possible_seats = num_seats
                
                self.add_reservation(current_row, seat_range)
                reservation += [f"{self.row_mapping[current_row]}{i+1}" for i in range(seat_range[0], seat_range[1]+1)]

                num_seats -= possible_seats

                if num_seats==0:
                    return reservation       
       
        self.reservations = reservations_copy
        num_seats = num_seats_copy

        return []       

