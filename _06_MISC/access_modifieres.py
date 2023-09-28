'''

'''

'''
Access modifiers : public  protected private default
'''
'''
public class Employee:
     public Employee(eid,name,sal):  # constructor
         this.eid = eid
         this.name = name
         this.sal = sal
        
    private void getedata(): 
         println("Emp data")

Employee madhu = Employee(100, 'MadhuN', 10000)
madhu.getedata()

'''


class Employee:
    def __init__(self):
        pass

    def _resuable(self):
        return "hello"
    def _getx(self):
        return "Hello"
    def _load(self):
        pass
    def _process(self):
        pass
    def __validate(self):
        pass
    def _final_format(self):
        pass
    def _sort(self):
        pass
    def _extract_zip(self):
        val = self._getx()
        print(val)

    def get_edata(self):
        val = self._extractzip()
        print(val)
        # 1000 lines of code
        '''
           I. Load zip file  
           II. Extract zip file 
           III. Sort by type of file
           IV. Validate each file 
           V. Iterate through each file type 
           VI. Process 
           VII. Save it 
        '''
        # I. Load zip file
        file = self._load()
        # II. Extract zip file
        data = self._extract_zip(file)
        # III. Sort the data
        sort_data = self._sort(data)
        self._process()
        self._validate()
        self._final_format()



emp = Employee()
emp.get_edata()


'''
2 Use cases: 
    - If method code complexity : Code Refactoring
        - seggreate methods : divide: mulitple protected or private methods 
    - For reusability 
        - 2 or more methods needs same logic : protected or private methods
'''


