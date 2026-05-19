print("--- Programme dyal Halat l-Ma' ---")
print("Ktab '999' bach t-hebess l-programme.")

while True:
  t = float(input("entre la chaleur de (calsuime):"))

  if  t == 999:
      print("fin de programme ")
      break

if t<=0 :
 
        print("la chaleur de calsuime est solide ")
elif t > 0 and t < 100:
     print("la chaleur de calsuime est liquide ")
else :
     print("la chaleur de calsuime est gaze") 