from report import Report

class firestation:
    def __init__(self) -> None:
        self.file_path = "report.txt"
        
    def file_report(self, REPORT: Report):
        lines = ['-------------------------------------\n',
                 f'{REPORT.timestamp} \n',
                 f'Reporter Name     : {REPORT.Name} \n',
                 f'Reporter Cnic     : {REPORT.Cnic} \n',
                 f'Emergency Location: {REPORT.location} \n',
                 f'Emergency Type    : {REPORT.type} \n',
                 '-------------------------------------\n']
        
        with open(self.file_path, 'a') as file:
            file.writelines(lines)  
            
    def read_file(self):
        with open(self.file_path, 'r') as file:
            report = file.read()
            
        print(report)
        
    def dispatch(self, REPORT: Report):
        if REPORT.type == 'fire':
            print('Dispatching Firemen')
            
        elif REPORT.type == 'crime':
            print('Dispatching Police')
            
        elif REPORT.type == 'injury':
            print('Dispatching Medics')
            
        else:
            print('Invalid Report, Ignoring')
            return False
        
def main():
    obj = Report('Umer', '12400982', 'Karachi', '03132271030', 'Fire')
    
    a = firestation()
    a.file_report(obj)
    a.read_file()
    
if __name__ == "__main__":
    main()
    
