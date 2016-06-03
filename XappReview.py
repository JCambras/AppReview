import sys 
import csv
import datetime

#Sample edit - ready for pull

yes = set(['yes', 'ye', 'YES', 'YE', 'y', 'Y', 'Yes', 'YEs'])
no = set(['no', 'NO', 'n', 'nO', 'No'])
testtype = set (['H', 'HSPT', 'HSP', 'h', 'hsp', 'hspt', 'TACHS', 'tachs', 't', 'TACH', 
'COOP', 'coop', 'co-op' 'COO', 'CHSEE', 'CHSE', 'chsee'])
goback = set (['GO BACK', 'Go Back', 'Re-do', 'RE-DO', 'go back', 'goback', 'return', 're-do', 'redo', 're do'])

qcontinue = "\nWhen you are ready to proceed, please press 'Enter'"
do_over = ("""\n\nThank you for those responses!
\nWould you like to continue to the next section?

Press 'Enter' to continue
Type: 'go back' to re-do the previous section

\n""")

		
while True:

	currentDate = datetime.date.today()
	
	data = []
	prompt1 = "Rate this grade on a scale from 1-100: "
	prompt2 = "Rate on a scale from 1-5 (with 5 being the highest): "

	#let's gather some basic information on the applicant.  This will help with yield %"
	
	print "\nWelcome to the Xavier High School Application Review Process!"
	
	print "\nYou can quit this program anytime by typing 'Ctrl-C'"
	
	print "\nSECTION 1: GENERAL INFORMATION"
	
	while True:
		moveon = raw_input(qcontinue)
		
		# gather reviewer and applicant data
		
		reviewer_first_name = str(raw_input("\nWhat is the reviewer's first name?	"))
		reviewer_last_name = str(raw_input("What is the reviewer's last name?	"))
	
		print "\nNow we need some basic information for the applicant:\n"
	
		application_ID = int(raw_input("What is the student's application ID number?	  "))
		first_name = raw_input("\nApplicant's first name:      ")
		middle_initial = raw_input("Applicant's middle initial:    ")
		last_name = raw_input("Applicant's last name:         ")
		
		#store gathered data in list
		
		
		#where does applicant live?

		while True:
			NYC = str(raw_input("\nDoes the student live in one of the five boroughs? (y/n):	"))
			if NYC in yes:
				Borough = raw_input("""\nGreat!  In which borough does the student live?\n
 \t* Brooklyn\t\t* Bronx\t\t* Manhattan
 \t* Queens\t\t* Staten Island	
 
 >> """)
				Local = "NA"
				break
			elif NYC in no:
				Local = raw_input("""\nInteresting!  Where does he live?\n
	\t* Long Island
	\t* New Jersey
	\t* Westchester/Rockland County
	\t* Other Location (please specify)
	 
 >> """)
				Borough = "NA"
				break
			else:
				print "Please enter 'yes' or 'no' to the question above and try again.\n\n"
				continue		


		#what type of school does the applicant attend?
		school_type = raw_input("""\nWhich type of school does the student attend?\n
	\t* Catholic
	\t* Orthodox
	\t* Public
	\t* Charter
	\t* Independent
	\t* Other

 >> """)
	
		
		
		elem_school = raw_input("""\nPlease enter the elementary school of the applicant: 
	
 >> """)

	

		caretakers = raw_input("\nDoes the applicant have one or two primary caretakers?	")
	
	
		fin_aid = raw_input("\nIs the applicant applying for financial aid? (y/n)	")
		 
		
		move_on = raw_input(do_over)
		if move_on in goback:
			continue
		else:
			break
		
		#store data
		
	
	#Time to evaluate the application!#
	print "\n\n--------------------------\n"
	print "\nNow let's move on to evaluate %s's application.\n" % first_name
	
	print  "\nSECTION TWO: SIXTH GRADE\n"
	
	
	while True:
	
		try:
			sixth_grade_question = str(raw_input("Do we have the applicant's sixth grade scores? "))
			if sixth_grade_question in yes:
			
				while True:
		
					try:
						sixth_grade_english = int(raw_input("\nWhat was the applicant's 6th grade English grade?	"))
						if 0 < sixth_grade_english <=100:
							break
						else:
							print "\nError!  Please enter an integer from 1-100"
							continue
					except ValueError:
						print "\nError!  Please provide an integer from 1 - 100"
						continue
				
				while True:
		
					try:
						sixth_grade_math = int(raw_input("\nWhat is the applicant's 6th grade math grade?	"))
						if 0 < sixth_grade_math <= 100:
							break
						else:
							print "\nError!  Please enter an integer from 1-100"
					except ValueError:
						print "\nError!  Please provide an integer from 1 - 100"
				
				while True:
					try:
						sixth_grade_history = int(raw_input("\nWhat is the applicant's 6th grade history grade?	"))
						if 0 < sixth_grade_history <= 100:
							break
						else:
							print "\nError!  Please enter an integer from 1-100"
					except ValueError:
						print "\nError!  Please provide an integer from 1 - 100"
				
				while True:
					try:
						sixth_grade_science = int(raw_input("\nWhat is the applicant's 6th grade science grade?	"))
						if 0 < sixth_grade_science <= 100:
							break
						else:
							print "\nError! Please enter an integer from 1-100"
					except ValueError:
						print "\nError!  Please provide an integer from 1 - 100"
	

				while True:
					try:
						religion_q6 = str(raw_input("\nDid the applicant take religion in 6th grade?	"))
						if religion_q6 in yes:
							sixth_grade_religion = int(raw_input("\nWhat was the applicant's 6th grade religion grade? "))
							if 0 < sixth_grade_religion <= 100:
								break
							else:
								print "Please enter an integer from 1-100"
						elif religion_q6 in no:
							sixth_grade_religion = "NA"
							break
						else:
							print "Invalid Entry: Please enter 'yes' or 'no'"
					except ValueError:
						print "Please enter 'yes' or 'no' to the question above and try again.\n\n"
	
				while True:
					try:
						fl_q6 = str(raw_input("\nDid the applicant take a foreign language in 6th grade?	"))
						if fl_q6 in yes:
							sixth_grade_fl = int(raw_input("\nWhat was the applicant's 6th grade foreign language grade? "))
							if 0 < sixth_grade_fl <= 100:
								break
							else:
								print "Please enter an integer from 1-100"
						elif fl_q6 in no:
							sixth_grade_fl = "NA"
							break
						else:
							print "Invalid Entry: Please enter 'yes' or 'no'"
					except ValueError:
						print "Please enter 'yes' or 'no' to the question above and try again.\n\n"
				
				move_on = raw_input(do_over)
				if move_on in goback:
					continue
				else:
					break
			elif sixth_grade_question in no:
				print "\nOK - we will move forward without analyzing the candidate's sixth grade grades"
				sixth_grade_english = "NA"
				sixth_grade_math = "NA"
				sixth_grade_history = "NA"
				sixth_grade_science = "NA"
				religion_q6 = "NA"
				sixth_grade_religion = "NA"
				fl_q6 = "NA"
				sixth_grade_fl = "NA"
				break
			else:
				print "Please enter 'yes' or 'no' to the question above and try again.\n\n"

		except ValueError:
			pass
	
	print "\nSECTION THREE: SEVENTH GRADE\n"

	while True:
			
		while True:
			try:
				seventh_grade_english = int(raw_input("\nWhat was the applicant's 7th grade English grade?	"))
				if 0 <= seventh_grade_english < 100:
					break
				else:
					print "\nError! Please provide an integer from 1-100!"
					continue
			except ValueError:
				print "\nError!  Please provide an integer from 1 - 100"
				
		while True:
			try:
				seventh_grade_math = int(raw_input("\nWhat was the applicant's 7th grade math grade?		"))
				if 0 <= seventh_grade_math < 100:
					break
				else:
					print "\nError! Please provide an integer from 1-100!"
					continue
			except ValueError:
				print "\nError!  Please provide an integer from 1 - 100"
				
		while True:
			try:
				seventh_grade_history = int(raw_input("\nWhat was the applicant's 7th grade history grade?	"))
				if 0 <= seventh_grade_history < 100:
					break
				else:
					print "\nError! Please provide an integer from 1-100!"
					continue	
			except ValueError:
				print "\nError!	Please provide an integer from 1 - 100!"
				
		while True:
			try:
				seventh_grade_science = int(raw_input("\nWhat was the applicant's 7th grade science grade?	"))
				if 0 <= seventh_grade_science < 100:
					break
				else:
					print "\nError: Please provide an integer from 1-100!"
					continue
			except ValueError:
				print "\nError!  Pleae provide an integer from 1 - 100!"

		while True:
			try:
				religion_q7 = str(raw_input("\nDid the applicant take religion in 7th grade?	"))
				if religion_q7 in yes:
					seventh_grade_religion = int(raw_input("\nWhat was the applicant's 7th grade religion grade? "))
					if 0 < seventh_grade_religion <= 100:
						break
					else:
						print "\nError! Please enter an integer from 1 - 100"
						continue
				elif religion_q7 in no:
					seventh_grade_religion = "NA"
					break
				else:
					print "\nInvalid Entry: Please enter 'yes' or 'no'"
			except ValueError:
				print "\nPlease enter 'yes' or 'no' to the question above and try again.\n\n"

		while True:
			try:
				fl_q7 = str(raw_input("\nDid the applicant take a foreign language in 7th grade?	"))
				if fl_q7 in yes:
					seventh_grade_fl = int(raw_input("\nWhat was the applicant's 7th grade foreign language grade? "))
					if 0 < seventh_grade_fl <= 100:
						break
					else:
						print "\nError:  Please enter an integer from 1 - 100" 
						continue
				elif fl_q7 in no:
					seventh_grade_fl = "NA"
					break
				else:
					print "\nError: Please enter 'yes' or 'no' to the question above and try again.\n\n"
			except ValueError:
				print "\nError: Please enter 'yes' or 'no' to the question above and try again."
				
		move_on = raw_input(do_over)
		if move_on in goback:
			continue
		else:
			break
	
	print  "\nThe application review is now 40% complete."
	
	print "\nSECTION FOUR: EIGHTH GRADE\n"
	
	while True:
	
		try:
			eighth_grade_question = str(raw_input("Do we have the applicant's eighth grade scores? "))
			if eighth_grade_question in yes:
			
				while True:
					try:
						eighth_grade_english = int(raw_input("\nWhat was the applicant's 8th grade English grade?	"))
						if 0 <= eighth_grade_english < 100:
							break
						else:
							print "\nError! Please provide an integer from 1-100!"
							continue
					except ValueError:
						print "Error!  Please provide an integer from 1 - 100"
				
				while True:
					try:
						eighth_grade_math = int(raw_input("\nWhat was the applicant's 8th grade math grade?		"))
						if 0 <= eighth_grade_math < 100:
							break
						else:
							print "\nError! Please provide an integer from 1-100!"
							continue
					except ValueError:
						print "\nError!  Please provide an integer from 1 - 100"
				
				while True:
					try:
						eighth_grade_history = int(raw_input("\nWhat was the applicant's 8th grade history grade?	"))
						if 0 <= eighth_grade_history < 100:
							break
						else:
							print "\nError! Please provide an integer from 1-100!"
							continue	
					except ValueError:
						print "\nError!	Please provide an integer from 1 - 100!"
				
				while True:
					try:
						eighth_grade_science = int(raw_input("\nWhat was the applicant's 8th grade science grade?	"))
						if 0 <= eighth_grade_science < 100:
							break
						else:
							print "\nError: Please provide an integer from 1-100!"
							continue
					except ValueError:
						print "\nError!  Pleae provide an integer from 1 - 100!"

				while True:
					try:
						religion_q8 = str(raw_input("\nDid the applicant take religion in 8th grade?	"))
						if religion_q8 in yes:
							eighth_grade_religion = int(raw_input("\nWhat was the applicant's 8th grade religion grade? "))
							if 0 < eighth_grade_religion <= 100:
								break
							else:
								print "\nError! Please enter an integer from 1 - 100"
								continue
						elif religion_q8 in no:
							eighth_grade_religion = "NA"
							break
						else:
							print "\nInvalid Entry: Please enter 'yes' or 'no'"
					except ValueError:
						print "\nPlease enter 'yes' or 'no' to the question above and try again.\n\n"

				while True:
					try:
						fl_q8 = str(raw_input("\nDid the applicant take a foreign language in 8th grade?	"))
						if fl_q8 in yes:
							eighth_grade_fl = int(raw_input("\nWhat was the applicant's 8th grade foreign language grade? "))
							if 0 < eighth_grade_fl <= 100:
								break
							else:
								print "\nError:  Please enter an integer from 1 - 100" 
								continue
						elif fl_q8 in no:
							eighth_grade_fl = "NA"
							break
						else:
							print "\nError: Please enter 'yes' or 'no' to the question above and try again.\n\n"
					except ValueError:
						print "\nError: Please enter 'yes' or 'no' to the question above and try again."
				
				move_on = raw_input(do_over)
				if move_on in goback:
					continue
				else:
					break
			
			elif eighth_grade_question in no:
					
				eighth_grade_english = "NA"
				eighth_grade_math = "NA"
				eighth_grade_history = "NA"
				eighth_grade_science = "NA"
				religion_q8 = "NA"
				eighth_grade_religion = "NA"
				fl_q8 = "NA"
				eighth_grade_fl = "NA"
				break
			else:
				print "Please enter 'yes' or 'no' and try again. \n\n"

		except ValueError:
			pass
	
	
	print  "\nThe application review is 60% complete! Here are some strengths and weaknesses:"
	
	print "\n--------------------------------\n"
	
	print """\n
 \nImportant Information:\n
 \t* 7th grade is worth twice as much as 6th grade.
 \t* 8th grade grades are not used in the calculation.
 \t* Religion and Foreign Langauge grades are not considered in the formula
	"""
	
	if sixth_grade_question in yes:
		english_total = int((sixth_grade_english + (seventh_grade_english*2))/3)
		math_total = int((sixth_grade_math + (seventh_grade_math*2))/3)
		history_total = int((sixth_grade_science + (seventh_grade_science*2))/3)
		science_total = int((sixth_grade_science + (seventh_grade_science*2))/3)
	else:
		english_total = seventh_grade_english
		math_total = 	seventh_grade_math
		history_total = seventh_grade_science
		science_total = seventh_grade_science
	
	
	total_grade_score = int(((english_total*2) + math_total + science_total + history_total)/5)
	
	#storing all scoring data
	

	
	print """
 \nHere are the Weighted GPA's for each subject:\n
 \t* Weighted English Grade:		%d
 \t* Weighted Math Grade:   		%d
 \t* Weighted History Grade:		%d
 \t* Weighted Science Grade:		%d
	
	
 \t* Composite Weighted GPA of the 'core' classes':\t%d\n\n """ % (english_total, math_total, history_total, science_total, total_grade_score)
	
	proceed_five = raw_input("""
 \nLet's take a quick look at the strengths and weaknesses.  
	
 \nPress 'Enter' to continue:	""") 
	
	print "\nStrengths:\n"
	
	if english_total >= 90:
		print "\tEnglish"
	else:
		pass
		
	if math_total >= 90:
		print "\tMath"
	else:
		pass
	
	if history_total >= 90:
		print "\tHistory"
	else:
		pass
		
	if science_total >= 90:
		print "\tScience"
	else:
		pass
	
	if english_total <90 and math_total <90 and history_total <90 and science_total <90:
		print "\tNone"
	else: 
		pass
	
	print "\n"
	
	print "\nWeaknesses:\n"

	if english_total <= 80:
		print "\tEnglish"
	else:
		pass
		
	if seventh_grade_math <= 80:
		print "\tMath"
	else:
		pass
		
	if seventh_grade_history <= 80:
		print "\tHistory"
	else:
		pass
		
	if seventh_grade_science <= 80:
		print "\tScience"
	else:
		pass
	
	
	if english_total > 80 and math_total > 80 and history_total > 80 and science_total > 80:
		print "\tNone"
	else: 
		pass
	
	
	proceed_one = raw_input("\n\nPress 'Enter' to proceed. 	")

	
	
	# Now, an overview of all of the grades#
	
	print "\n--------------------------------"
	print "\n--------------------------------"
	print "\n--------------------------------\n"
	
	#on to testing#
	#TODO - other testing scores#

	proceed = raw_input("""
	\n\nNext, we will analyze the applicant's scores on his standardized test.
	\nIf the student took multiple, use the one on which they did bettter.
	\nFor the scores themselves, make sure you look at the NATIONAL AVERAGE.
	
	\nWhen you have the test scores ready and are ready to proceed, press 'Enter'.
	""")
	
	print "SECTION FIVE: STANDARDIZED TEST SCORES"
	
	while True:
		try:
			test_type = str(raw_input("""\nPlease indicate which test we will be using:
			
 	* HSPT
 	* TACHS
 	* COOP
 	* CHSEE
 	* Other
 	
 	>> """))
			if test_type in testtype:
				print "\nGreat!  Let's look at how he scored in the specific categories of the %s." % test_type
				break
			elif test_type == 'OTHER' or test_type == 'other':
				other_test = str(raw_input("\nOk - please indicate which test the student took:	"))
				print "\nGreat - let's look at the results of %s"	% other_test
				break
			else:
				print """\nPlease indicate if the student took the TACHS or the HSPT.  
				\nIf he did not take either one, write 'neither'"""
				continue
		except ValueError:
			print """\nPlease indicate if the student took the TACHS or the HSPT.  
			\nIf he did not take either one, write 'neither'"""
	
	
	print "\n\n--------------------------\n"
	
	while True:
		while True:
			try:
				reading_score = int(raw_input("\nWhat is the applicant's National Percentile (NP) in reading?		"))
				if 0 <= reading_score < 100:
					break
				else:
					print "\nError:  Please provide an integer from 1 - 100"
					continue
			except ValueError:
				print "\nPlease enter a valid integer from 1 - 100"
				
		while True:
			try:
				language_score = int(raw_input("\nWhat is the applicant's NP in language?		"))
				if 0 <= language_score < 100:
					break
				else:
					continue
			except ValueError:
				print "\nPlease enter a valid integer from 1 - 100"

			
		while True:
			try:
				math_score = int(raw_input("\nWhat is the applicant's NP in math?		"))
				if 0 <= math_score < 100:
					break
				else:
					print "\nError:  Please provide an integer from 1 - 100"

			except ValueError:
				print "\nPlease enter a valid integer from 1 - 100"

		while True:
			try:
				composite_score = int(raw_input("\nWhat is the applicant's NP in Total Achievement?	")) 
				if 0 <= composite_score < 100:
					break
				else:
					print "\nError:  Please provide an integer from 1 - 100"
			except ValueError:
				print "\nError:  Please provide an integer from 1 - 100"
		
			
		move_on = raw_input(do_over)
		if move_on in goback:
			continue
		else:
			break
				
	
	

	if composite_score >= 95:
		print "\n\nWow!  Probably an Ignatian Scholar's candidate!\n"
	elif composite_score >= 90 and composite_score < 95:
		print "\n\nGreat!  Typically, students with score are accepted.\n"
	elif composite_score >=80 and composite_score < 90:
		print """\n\n%s test scores are above average.  
	\nAny red flags?  Please note in the 'comments' section at the end.\n""" % first_name
	elif composite_score >= 50 and composite_score < 80:
		print """\n\%s test grades are below average, but he still falls in our 80 percent range.
	\nHis grades will be the major determining factor in acceptance.\n""" % first_name
	elif composite_score >= 25 and composite_score < 50:
		print """\n\nAlthough %s has a below-average test grade, he still falls in our 80 percent range.
	\nHis grades will be the major determining factor in acceptance.
	\nAs a reference, students in this range with 85+ averages have done fine,
	\nbut students with these scores and B-/C grades have really struggled.\n""" % first_name
	elif composite_score >= 0 and composite_score < 25:
		print """\n\nStudents with total achievement scores under a 25 really struggle at Xavier.
	\nIf %s has an 'A' average, his candidacy is worth discussing.
	\nHowever, if he has anything less than an 'A' average, %s is most likely not a good fit.\n""" % (first_name, first_name)
	else:
		pass	
			
			
	proceed_two = raw_input("""
	\nThe application review is now 80% complete!
	
	\nThank you for entering the test scores.  
	\nWe will now be looking at the application.
	
	\nWhen you are ready to proceed, press 'Enter'.""")

	print "\n\n--------------------------\n"

	#now on to the application.  Scale of 1-5...each one represents a certain multiplier#
	print "\n\nSECITON SIX: STUDENT RESPONSES ON APPLICATION."
	
	print """\nHow would you rate the student's short-answer responses?
			\n
 Things to keep in mind:
  *  The student responses should portray some desire to attend Xavier.
  *  The parent response should portray an understanding of our mission.
  *  The student should be interested in at least two DIFFERENT activities
  *  There is no perfect formula in judging an application.  Trust your gut!\n\n"""

	print """
 Here is how you should rate the applicant:
  5:  The student's application is excellent and mission-oriented.
  4:  The student's application is very good and mission-oriented.
  3:  The student communicates sufficient reasons for attending Xavier.
  2:  The student does not provide sufficient reasons for wanting to attend.
  1:  The student clearly has no interest in attending Xavier High School.\n"""

	print "\n--------------------------\n"

	while True:		
		
		while True:
		
			try:
				application = int(raw_input(prompt2))
				if 0 <= application < 100:
					break
				else:
					print "\nError:  Please provide an integer from 1 - 100"
					continue
						
			except ValueError:
				print "\nPlease enter a valid integer from 1 - 100"
		
		if application == 5:
			print "\n\nSo %s's application is stellar.  Great!\n" % first_name
			break
		elif application == 4:
			print "\n\n%s has a pretty good application and would fit in well with our school community.\n" % first_name
			break
		elif application == 3:
			print """\n\n
	So this means %s's application was decent.  
	Please mention 'red flags' in the comments section at the end.\n""" % first_name
			break
		elif application == 2 or application == 1:
			print """\n\nThis is a cause for concern.  
	\nPlease let us know why %s received this grade in the comments section.\n""" % first_name
			break
		else:
			print "\n\nThe number you entered needs to be an integer from 1-5.  Please enter again.\n\n"
			continue

	print "\n--------------------------\n"



	print """\n
	\nDo you have any special comments about %s's application?
	\nIs there anything on the application - good or bad - 
	\nthat cannot be objectified but should be considered?\n\n""" % first_name

	comments = raw_input("Enter your comments here: ")
	
	
	print "\n\n--------------------------\n"

	print "Thank you for those comments - they will be noted.\n"
	
	proceed_three = raw_input("We will now proceed to the applicant overview.  Press 'Enter' when ready.")


	print "\n\n----------------\n\n"

	#Overview
	print "Here is the overview of %s's application:\n\n" % first_name

#General Info
	print "\tReviewer's First Name: 				%s" % reviewer_first_name
	print "\tReviewer's Last Name: 				%s" % reviewer_last_name
	
	print "\n\n\tFirst Name: 					%s" %  first_name
	print "\tMiddle Initial: 				%s" % middle_initial
	print "\tLast Name: 					%s\n" % last_name
	print "\tType of School: 				%s" % school_type
	print "\tName of School: 				%s" % elem_school
	print "\tNumber of Primary Caretakers: 			%s" % caretakers
	print "\tFinancial Aid Candidate?			%s" % fin_aid

#Grades
	print "\n\tWeighted English Score: 		%r" % english_total
	print "\tWeighted Math Score:			%r" % math_total
	print "\tWeighted Science Score: 		%r" % science_total
	print "\tWeighted History Score:  		%r" % history_total
	print "\tWeighted Overall GPA:			%r\n\n" % total_grade_score
	
#Test Scores	
	print "\tReading Score National Average: 		%d" % reading_score
	print "\tLanguage Score National Average: 		%d" % language_score
	print "\tMath Score National Average: 			%d" % math_score
	print "\tComposite Score National Average: 		%d\n" % composite_score
	
#Applicant Multiplier
	print "\tApplication Score: %r\n\n" % application
	

#Comments
	print "Here are the special comments: %s\n" % comments

# TODO:  YIELD %
	
	
	total_test_score = int((math_score+language_score+(reading_score*2))/4)
	
	orf = int(((total_grade_score*1.5)+total_test_score)*.4)
	
	if orf >= 95:
		orf_rec = "Accept into Ignatian Scholars with a Merit Award"
	elif orf >= 92 and orf < 95:
		orf_rec = "Accept into Ignatian Scholars"
	elif orf >= 88 and orf < 92:
		orf_rec = "Regular Accept"
	elif orf >= 85 and orf < 88:
		orf_rec = "Accept with Reservations"
	elif orf >= 78 and orf < 85:
		orf_rec = "Possibly Accept with X-Prep & Full Grades"
	else:
		orf_rec = "Deny"
	
	
	
	print """Based on the information provided, 
 \n%s's Objective Ranking Factor (ORF) Score is a(n) %r out of 100.\n"""  % (first_name, orf)
	
	print "\n%s's computer-generated recommendation is: %r" % (first_name, orf_rec)
	
	proceed_four = raw_input("""\n\nWe will now proceed to the reviewer's recommendation.  
	
	\nPress 'Enter' when ready.""")

	print "\n\n--------------------------\n"

	print "\nNow it's time to make your final recommendation.\n"
	
	print "\nThe computer generated reocmmendation was to '%s'" % orf_rec
	
	rec = str(raw_input("""
 \nPlease make a recommendation now.
	
 \nHere are your options:
	
 \t*: Accept with Honors
 \t*: Regular Accept
 \t*: Accept with Reservations
 \t*: Accept with X-Prep
 \t*: Not Sure
 \t*: Deny
 
 \n>>	"""))


	print "\nThank you.  Your recommendation of %s has been recorded!" % rec 


	print "\n\n----------------\n\n"

	#confirmation


	while True:
		submit = raw_input("Would you like to submit this application review? (y/n)	    ")
		if submit in yes:
			data.append(currentDate)
			data.append(str(reviewer_first_name))
			data.append(str(reviewer_last_name))
			data.append(int(application_ID))
			data.append(first_name)
			data.append(middle_initial)
			data.append(last_name)
			
			data.append(NYC)
			data.append(Borough)
			data.append(Local)
			data.append(school_type)
			data.append(elem_school)
			data.append(caretakers)
			data.append(fin_aid)
			
			
			data.append(sixth_grade_english)
			data.append(sixth_grade_math)
			data.append(sixth_grade_history)
			data.append(sixth_grade_science)
			data.append(religion_q6)
			data.append(sixth_grade_religion)
			data.append(fl_q6)
			data.append(sixth_grade_fl)
			
			data.append(int(seventh_grade_english))
			data.append(int(seventh_grade_math))
			data.append(int(seventh_grade_history))
			data.append(int(seventh_grade_science))
			data.append(religion_q7)
			data.append(seventh_grade_religion)
			data.append(fl_q7)
			data.append(seventh_grade_fl)
			
			data.append(eighth_grade_english)
			data.append(eighth_grade_math)
			data.append(eighth_grade_history)
			data.append(eighth_grade_science)
			data.append(religion_q8)
			data.append(eighth_grade_religion)
			data.append(fl_q8)
			data.append(eighth_grade_fl)
			
			data.append(int(english_total))
			data.append(int(math_total))
			data.append(int(history_total))
			data.append(int(science_total))
			data.append(int(total_grade_score))
			
			data.append(int(reading_score))
			data.append(int(language_score))
			data.append(int(math_score))
			data.append(int(composite_score))
			
			data.append(int(application))
			data.append(comments)
			data.append(int(orf))
			data.append(orf_rec)
			data.append(rec)
	
			print "\nExcellent! The application review for %s has been submitted!\n" % first_name	
			results = open('appresults.csv', 'ab')
			dataWriter = csv.writer(results)
			dataWriter.writerow(data)
			results.close()
			break
		elif submit in no: 
			start_over = raw_input("\nYou indicated that you would like to start over without submitting.  Do you wish to start over?	")
			if start_over in yes:
				import sys
				sys.exit(0)
				break
			elif start_over in no:
				continue
			else:
				continue

	

	while True:
		start_over = raw_input("""
 \nThank you for submitting the previous application.\n  
 \nWould you like to review another application?	""")
		if start_over == 'yes' or start_over == 'y' or start_over == 'Yes':
			break
		else:
			sys.exit(0)
		


	
