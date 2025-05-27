# Task 1
try: 
    with open ("diary.txt", "a") as diary: 
        prompt = "What happened today? "
        while True:
            line = input(prompt)
            diary.write(line + "\n") # add the answer to diary 
            if line == "done for now":
                diary.write(line + "\n")
                break
            prompt = "What else? "

except Exception as e: 
    print("An exception occurred.")
    print(f"Exception type: {type(e).__name__}")


