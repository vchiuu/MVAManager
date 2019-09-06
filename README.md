 MVA Manager
The application is designed to aid clinics manage Motor Vehicle Accident patients to ensure the required appointments are scheduled and, paperwork and billing is completed in a timely manner. 

## Motor Vehicle Accident Coverage
When a Motor Vehicle Accident (MVA) patient begins their treatment, they must have complete forms:
* OCF-1 Application for Accident Benefits
* OCF-3 Disability Certificate
* OCF-5 Permission to Disclose Health Information
* OCF-23 Treatment Confirmation Form

If the patient requires further treatment after the first 12 weeks of treatment, then the patient and practitioner must have completed:
* OCF-18 Treatment and Assessment Plan

## Motor Vehicle Accident Treatment Rates & Billing 
|   Treatment Stage   |   Duration  |    Fee    |Typical Number of Appointments | Details                         |
|   :-------------:   | :---------: |  -------: |:----------------------------: | :-----------------------------: |
| Initial Assessment  |  1 session  |  $ 215.00 | 1 appointment                 | Initial visit after accident    |
|       Block 1       |   4 weeks   |  $ 775.00 | 2 appointments/week           | After the date of accident      |
|       Block 2       |   4 weeks   |  $ 500.00 | 1 appointment/week            | After the completion of Block 1 |
|       Block 3       |   4 weeks   |  $ 225.00 | 1 appointment/week            | After the complete of Block 2   | 
|      Extended       | (as needed) |   ------- | (as needed)                   | After approval of OCF-18        |
|      Discharge      |  1 session  |  $  85.00 | 1 appointment                 | End of treatment                |
| Goods and Services  | (as needed) |  $ 400.00 | (not applicable)              | Dispensed during Blocks 1 to 3  |
 
Note: During the first 12-weeks, number appointments may vary depending on the rates which the clinic decides to charge.
The following rates apply during extended treatment or, when patient has their own Extended Health Care (EHC) Benefits.

|       Treatment Type       | Cost     |
| :-------------------------:| -------: |
| Chiropractic               | $ 112.81 |
| Physiotherapy              | $  99.75 |
| Registered Massage Therapy | $  58.19 |

# Screenshots 

# MVA Manager Database Design
<kbd>![MVA Manager ERD Design](https://github.com/vchiuu/MVAManager/blob/master/MVAManager_ERD.jpg)</kbd>
# Using Flask

Create & Activate your Virtual Environment
``` 
env\Scripts\activate
```
Reset Local SQLite DB
```
(env) PS C:\location python
>>> from mvaManager import db, create_app
>>> db.create_all(app=create_app())
>>> db.drop_all(app=create_app())
>>> exit()
```
