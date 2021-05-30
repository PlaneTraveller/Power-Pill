# Power-Pill

## 		basic_data

### 				.json structure

​				a dict(dict1) whose keys are the 52 states' names and value is another dict(dict2)

​				the key of every dict2 are 'values'(digital data on the epidemic) and 'events'(maybe 				news about the epidemic, abandoned)

​				the values of 'values' is a dict(dict3)

​				the keys of dict3 are 'new-confirmed-cases' and 'new-deaths'

​				their values are both a list whose elements are dicts(dict4)

​				every dict4 has 4 keys: 'dt'(date), 'average', 'value', 'cumulative'

​				these values are the needed data

### 				.csv structure

​				index: date

​				column:  new_confirmed_cases_average

​							    new_confirmed_cases_value

​								new_confirmed_cases_cumulative

​								new_deaths_average

​								new_deaths_value

​								new_deaths_cumulative

## 		vaccinations

### 				.json structure

​				a list about data for a single state

​				the elements are dicts containing data for a certain date

​				every dict has 3 keys: 'doses_admin_daily', '7_day_avg', 'date'

​				these values are the needed data

### 				.csv structure

​				index: date

​				column: doses_admin_daily

​								7_day_avg

## 		another_hospitalization

### 				.json structure

​				a list with only one element which is a dict(dict1)

​				the keys of dict1 are different dates('2020-01-28', '2020-01-29')

​				the value of each is a dict(dict2) whose keys are 'inpatient_beds_used_covid' and 				'7_day_avg'

​				these values are the needed data

### 				.csv structure

​				index: date

​				column: inpatient_beds_used_covid

​								7_day_avg

## 		hospitalization

### 				.json structure

​				a list whose elements are dicts(dict1) containing the data for a single state

​				every dict1 has 2 keys: 'state', 'data'

​				the value of 'data' is a dict(dict2) whose keys are 'inpatient' and 'icu'

​				the value of both is a dict(dict3) whose keys are 'covid', 'non-covid', 'occ_this_week'. 				'occ_previous_week'

​				these values are the needed data(in percentage)

### 				.csv structure

​				one for inpatient and another for icu

​				index: covid

​							non-covid

​							occ_this_week

​							occ_previous_week

​				column: NAN
