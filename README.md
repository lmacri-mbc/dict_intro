Python Task: Fishing Tour Booking (Using a Dictionary)
You are writing a program to help a company manage bookings for their fishing tours. Your program must
collect information from the user and summarize it at the end.
Follow the instructions carefully.

�� Instructions
1. Create a function called collect_tour_info() to collect and display the data.
2. Inside the function:
��‍��‍�� Ask the user:

o How many people are going on the tour (must be between 1 and 4).
 If the number is outside that range, keep asking until it’s valid.

�� Ask the user to choose a destination:
Display the following options as a numbered list and ask for the number:
markdown
CopyEdit
1. Kaikoura
2. Port Underwood
3. Ships Cove

o Convert the number into the actual destination name (e.g. &quot;1&quot; → &quot;Kaikoura&quot;).
o If an invalid number is entered, default to “Kaikoura”.

�� Ask how many days the tour will last.
�� For each person going on the tour:
o Ask for their name and age.
o Store this as a dictionary with keys &quot;name&quot; and &quot;age&quot;.
3. Store all of the tour data inside one main dictionary called tour_data.
This dictionary should include:
o &quot;number_of_people&quot; (int)
o &quot;destination&quot; (string)
o &quot;length_days&quot; (int)
o &quot;people&quot;: a list of dictionaries, each containing a name and age
4. After collecting all data, print a summary showing:
o The number of people
o The destination
o The length of the tour
o The names and ages of each person
5. Use clear variable names and comments throughout your code.

✅ Example Output
yaml
CopyEdit
How many people are going on the tour? (Max 4): 2

Choose your destination:
1. Kaikoura
2. Port Underwood
3. Ships Cove
Enter the number of your destination choice: 3

How many days will the tour be? 3

Enter the name and age of each person:
Enter the name of person 1: Maya
Enter their age: 28
Enter the name of person 2: Ethan
Enter their age: 35

--- Tour Summary ---
Number of People: 2
Destination: Ships Cove
Length of Tour: 3 day(s)

People Information:
- Maya, Age: 28
- Ethan, Age: 35
