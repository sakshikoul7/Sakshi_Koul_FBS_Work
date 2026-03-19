#to convert the time entered in seconds into hours, minutes and seconds
time=float(input("Enter the time in seconds: "))
           
hours =time //3600
rem_time=time%3600

minutes=rem_time//60
seconds=rem_time%60
print(f'{time} seconds is equal to {hours} hours, {minutes} minutes and {seconds} seconds.')


                 