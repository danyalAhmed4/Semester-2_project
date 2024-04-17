from report import Report

class firestation:
    def __init__(self, REPORT: Report) -> None:
        self.file_path = "report.txt"
        self.report = REPORT
        
    def file_report(self):
        lines = ['-------------------------------------\n',
                 f'{self.report.timestamp} \n',
                 f'Reporter Name     : {self.report.Name} \n',
                 f'Reporter Cnic     : {self.report.Cnic} \n',
                 f'Emergency Location: {self.report.location} \n',
                 f'Emergency Type    : {self.report.type} \n',
                 '-------------------------------------\n']
        
        with open(self.file_path, 'a') as file:
            file.writelines(lines)  
            
    def read_file(self):
        with open(self.file_path, 'r') as file:
            report = file.read()
            
        print(report)
        
def main():
    obj = Report('Umer', '12400982', 'Karachi', 'Fire')
    
    a = firestation(obj)
    a.file_report()
    a.read_file()
    
if __name__ == "__main__":
    main()
    
