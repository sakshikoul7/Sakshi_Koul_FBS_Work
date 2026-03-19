#to accept an integer amount from usernand tell minimum number of notes needed for representing that amount
amount=int(input("Enter the amount: "))
notes_2000=amount//2000
amount=amount%2000
notes_500=amount//500
amount=amount%500
notes_200=amount//200
amount=amount%200
notes_100=amount//100
amount=amount%100
notes_50=amount//50
amount=amount%50
notes_20=amount//20
amount=amount%20
notes_10=amount//10
amount=amount%10
notes_5=amount//5
amount=amount%5
notes_2=amount//2
amount=amount%2
notes_1=amount//1
amount=amount%1

print(f'Minimum number of notes needed for representing the amount is: {notes_2000} notes of 2000, {notes_500} notes of 500, {notes_200} notes of 200, {notes_100} notes of 100, {notes_50} notes of 50, {notes_20} notes of 20, {notes_10} notes of 10, {notes_5} notes of 5, {notes_2} notes of 2 and {notes_1} notes of 1')