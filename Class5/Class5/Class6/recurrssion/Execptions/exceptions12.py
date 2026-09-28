try:
    result = 5+50
except:
    print("Error occurred")
else:
    print("No exception, result is", result)    
finally:
    print("Execution completed")        