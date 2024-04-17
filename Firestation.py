class firestation:
    def __init__(self) -> None:
        self.file_path = "report.txt"
        
    def file_report(self):
        with open(self.file_path, 'a') as file:
            file.write('Hello\n')  
        
def main():
    a = firestation()
    a.file_report()
    
if __name__ == "__main__":
    main()
    
