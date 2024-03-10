
presidents = ["Washington, George, 2/22/1732, 12/14/1799", "Adams, John, 10/30/1735, 7/4/1826", "Jefferson, Thomas, 4/13/1743, 7/4/1826", "Madison, James, 3/16/1751, 6/28/1836", "Monroe, James, 4/28/1758, 7/4/1831"]

for president_info in presidents:
    # Split the information into parts
    last_name, first_name, birth_date, death_date = president_info.split(', ')

    # Format and print the information
    formatted_info = "{} {} ({} - {})".format(first_name, last_name, birth_date, death_date)
    print(formatted_info)