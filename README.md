# genny
A Unique ID generator utility built on python 3.6.<br>
Ideal for generating Product ID, Employee ID, Job ID's etc.. 

# Utilities 
Genny exposes three utility classes <br>
GenId  genny.genid:  used for documents, application secret keys, job id's etc..<br>

NameId  genny.nameid:  used to generate Employee's Id, User Id's etc<br>


# Usage 
UseCase: <br>
genny.genid(DocTag)<br>

DocTags: String( 'doc', 'app', 'key', 'job', 'user', 'item', 'code','task', 'name')

			  		>>> import genny or 
			  		>>> from genny import genid  or
			  		>>> from genny import genid as gi
			  		
			  		>>> id = genny.genid('user')
			  		>>> id = genid('user')
			  		>>> id = gi('user')
			        Yeilds  ... U474390
			 		        ... U77301642
			 		        ... U1593055
    

UseCase: <br>
genny.nameid('fn, 'ln')

	Name Identification by initials fn='Jane', ln='Dear' and given number sequence sec=5.
    	
        
			  		>>> import genny
			  		>>> from genny import nameid
			  		>>> from genny import nameid as nid
			  		
			  		>>> id = genny.nameid('Peter','Built',6)
			  		>>> id = nameid('Peter','Built',5)
			  		>>> id = nid('Peter','Built',4)
                    >>> id = nid() # default false id 
                    
			 Yeilds ... PB474390
			 		... PB77301
			 		... PB1593
                    ... JD1951
    
    

# Dependencies
Python StringGenerator  
