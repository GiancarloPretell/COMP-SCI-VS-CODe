guest_names = ['Grace Hopper', 'Richard Tapia','Timnit Gebru','Radia Perlman', 'Ada Lovelace','Ruzena Bajcsy']

number_of_guests = [2,3,1,2,2,1]

for name, count in zip(guest_names, number_of_guests):
    print(f"{name} is bringing {count} guest(s).")