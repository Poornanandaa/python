class employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):   
        print("Employee destroyed")
ob=employee()
del ob