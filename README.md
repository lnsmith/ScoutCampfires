# ScoutCampfires
Purpose - to allow online management of budget records for each scouting group (pack or troop), and to provide a space to share updates/information about past and future events. 

# Current Phase: Phase 1 
Phase 1: 
Welcome Screen, choose Cub Scout or Scout BSA 
	Routes to budget url -> budget view {% scout_type_id %} - data displayed is based on scout_type_id passed in 
		
Data displayed = BudgetItem with description and total (entered via the admin page) 

Data to enter = BudgetRecord(s) using a form and calculate total (via calculate button that runs python on data in database and returns to display in view) 

# Future Phases: 
Phase 2: 
Search for Pack/Troop by ZipCode 
	create new model GroupType - Pack/Troop choices, ZipCode, Pack/Troop name - this phase will have only web dev inputting this information OR a person given an admin account/password that can input it 
	
Phase 3: 
Authentication for cub master/troop leaders to manage their information (posts, group specific budget, (possible calendar entries or allow them to add an existing google calendar account and embed it) 
	Information regarding group specific budget will include what percentage of sales the group takes from individual sales 
