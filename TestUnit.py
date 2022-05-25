# -*- coding: utf-8 -*-
"""
Created on Thu May 19 23:09:53 2022

@author: thepr
"""
#import docx
#import openpyxl
import unittest
import datetime
from ..Source import AutomationCodeCWC

class TestAutomationCode(unittest.TestCase):
    excelFilename = r"../Resources/SampleInput.xlsx"
    wordFilename = r"../Resources/SampleOutput.docx"
    row = 2
    
    def testGetData(self):
        outdata = AutomationCodeCWC.getdata(self.excelFilename,self.row)
        ExpectedSelectAttribute = {'Timestamp': datetime.datetime(2021, 8, 2, 19, 40, 36, 423000), 'Tune-Up Date': datetime.datetime(2021, 7, 21, 0, 0), 'Resident Name': 'Ben Griffith', 'Case Number': '21-07-01-I', 'Building/House Number': 3941, 'Direction': 'NW', 'Street Name': '34TH', 'Street Type': 'DR', 'Apartment Number': None, 'City': 'Gainesville', 'State': 'FL', 'Zip Code': 32605, 'Energy Coach Names': 'Karen Sem and Belina Meador', 'Duration of Tune-up': 2.5, 'Resident is:': 'Homeowner', 'Number of residents in household:': 2, 'Dwelling Type': 'Single-family wood frame', 'Electric Meter Number': 76362, 'Electric Utility Provider': 'GRU', 'Water Meter Number': None, 'Water Utility Provider': 'GRU', 'Gas Meter Number': 74023, 'Gas Utility Provider': 'GRU', 'Wastewater Disposal': 'City sewer', 'Water Meter': 'Explained connection with meter and utility bill, and how and when wastewater is charged', 'Utility Bill Review': 'Compared months (energy usage vs. cost-12 month comparison), Checked wastewater volume on bill for apparent excess', 'Garbage Can Size': '35 gal (2 bags) $24.00/mo', 'Does resident fill garbage can each week?': 'Yes', 'Does resident recycle?': 'Yes', 'Comments on utilities, other fuel sources present (fireplace or propane tank?) and garbage:': 'Also composts!', 'Number of exterior doors': None, 'Number of sliding doors': None, 'Exterior doors details': 'Doors OK', 'Number of windows': 11, 'Type of windows': 'Single-pane', 'Window details': 'All windows are OK', 'Number of malfunctioning windows': 0, 'Comments on exterior doors and windows': 'Cracked panes on one window. Resident had questions about energy efficiency benefits of morning sun (light vs heat).', 'Foundation Type': 'Slab on grade (skip to Attic Venting if this type)', 'Foundation/Skirting Details': 'N/A (slab on grade)', 'Floor Insulation': 'No insulation present', 'Floor Insulation Details': 'N/A (slab on grade)', 'Attic venting present': 'Soffit/Eave, Off-ridge', 'Attic Venting Details': 'Vents OK', 'What kind of roof covering?': 'Asphalt/wood/tile/slate', 'What is the approximate age of the roof?': 'unknown', 'General Exterior': 'OK', 'Comments on general exterior': None, 'Condenser Coil': 'Condenser is OK', 'Refrigerant Lines': 'Line is OK', 'Did you install pipe insulation?': 'No', 'Plumbing Details': 'N/A', 'Outdoor Lighting': "Outdoor Lighting OK, Inefficient incandescent bulbs, not replaced as they aren't used often.", 'Pool Pump': 'N/A', 'Comments on outdoor central A/C, plumbing, and lighting': 'Refrigerant line pipe insulation was in great condition', 'Number of wall/window AC units': 0, 'Window/Wall Units': 'N/A', 'Reported (or estimated) age of air handler?': '1 year', 'Reported date of last service of air handler?': 'n/a', 'Programmable Thermostat': 'Has programmable thermostat, Resident already uses great temperature settings', 'Current Thermostat Setting': None, 'Air Handler / Furnace Details': 'OK', 'Air Handler Filters': 'Filter is dirty; recommended cleaning or replacement', 'Air Filter Size': 0, 'Furnace Type': 'Electric', 'Gas or Oil Furnaces': 'N/A', 'Comments on indoor heating and cooling systems': None, 'Insulation Type': 'Batt', 'Insulation Material': 'Fiberglass', 'Estimated Existing R-value': 'R-30', 'Attic Insulation Details': 'OK (insulation sufficient)', 'Duct Work Details': 'OK', 'Outlet and Switch Plate Cover Details': 'Identified possible air leaks, Recommended outlet/switch gaskets', 'Number of switch + outlet gaskets installed:': 12, 'Lighting Details': 'Inefficient incandescent bulbs were present', 'Number of LEDs installed by CWC:': 12, 'Number of fluorescent tubes in home:': 2, 'Range': 'Electric', 'Kitchen Sink Leaks': 'Leak at faucet; recommended repair by plumber', 'Kitchen Sink Aerator Details': 'Blocked/missing/inefficient aerator ( > 1.5 gpm)', 'GPM of aerator that was changed out': 'N/A', 'Refrigerator Temperature': 39, 'Refrigerator Temperature Setting ': None, 'Refrigerator Details': "Fridge coils dirty/blocked; couldn't access to clean but recommended resident cleans them", 'Number of additional freezers:': 0, 'Number of additional refrigerators:': 0, 'Separate Freezer/Fridges:': 'N/A', 'Dishwasher Details:': 'Asked about or checked heat dry setting; advised not to use heat-dry setting', 'Comments on attic, lighting, gaskets and kitchen': None, 'Toilet Details': 'Toilet is more than 1.6 gpf; recommended upgrade to 1.6 gpf model', 'Did you install a water displacement bag?': 'Yes', 'Vanity Sink Leaks (Bathroom 1)': 'N/A - no sink leaks', 'Vanity Sink Aerator Details': 'Blocked/missing/inefficient aerator ( > 1 gpm)', 'Shower/Tub Details': 'Shower head old/inefficient (>1.5 gpm), 2 inefficient showerheads', 'Did you install a lower gpm shower head? (Bath 1)': "No (put comment about why you didn't at the end of this page)", 'Type of shower head installed': None, 'GPM of shower head that was changed out': None, 'Toilet Details (Bathroom 2)': 'Toilet is more than 1.6 gpf; recommended upgrade to 1.6 gpf model', 'Did you install a water displacement bag? (B2)': 'No (not needed or no room in tank)', 'Vanity Sink Leaks (Bathroom 2)': 'N/A - no bathroom vanity sink leaks', 'Vanity Sink Aerator Details (Bathroom 2)': 'Blocked/missing/inefficient aerator ( > 1 gpm)', 'Shower/Tub Details (Bathroom 2)': 'OK', 'Did you install a lower gpm shower head? (Bathroom 2)': 'No', 'Type of shower head installed (bath 2)': 'Handle', 'Comments on Bathrooms': 'Guest bathroom showerhead used 0.8gpm. There were 2, 2.5gpm showerheads in the master bath.', 'Water Heater': 'Natural gas', 'Current temperature of water?': 108, 'Water Heater Details': 'OK', 'Did you insulate water heater pipes?': 'No', 'Gas water heaters only:': 'Piping appears OK', 'Current setting if gas water heater?': None, 'Washing Machine Details:': 'OK', 'Clothes Dryer:': 'Electric', 'Clothes Dryer Details:': 'Dryer vent blocked/damaged; cleared dryer vent', 'Utility Sink:': 'OK', 'Does resident have WORKING smoke detectors in home?': 'Yes', 'Does resident have ANY gas appliances in the household?': 'Yes', 'If YES to previous question, did you install a plug-in CO detector?': 'Yes', 'Comments on water heater, washer, dryer, utility sink, safety check': 'Water heater pipe insulation was great', 'EDUCATIONAL MEETING WITH RESIDENT:': "Reviewed specific recommendations from the tune-up with resident; pointed out key components around the home, Reviewed TIP SHEET with resident; discussed applicable ones, Asked resident which of the tips are doable; which one(s) will they commit to doing by CWC's 4-6 week follow-up?, Left tip sheet with resident, Reviewed contents of, and left information packet with resident", 'Which of the tips did the resident commit to?': 'increase hot water temperature to 120 degrees', "Resident's preference for follow-up questionnaire/interview": 'Email', 'Any additional comments': None, "While many factors can affect any further action at this site, the Energy Coach believes that this client's repair needs are:": 'Routine', 'Comments if other than routine:': None, 'Repair Needs:': 'Plumbing  Leaks, Window repair or replacement', 'If water heater needs replacement, provide any details:': None, 'Current R-Value:': 30, 'If marked other for appliance that needs replacing, which one?': None, 'Describe the plumbing leaks, if any?': 'Kitchen faucet - slow, not terribly urgent', 'Number of windows needing repair/replacement:': 1, 'Number of window screens needing repair/replacement:': 0, 'Number of doors needing repair/replacement:': 0, 'Other Repair Needs:': None, 'Comments on repairs needed:': '1 window pane is cracked in 2 places', 'Anything special that the CWC needs to know about the family or home?': None, 'Were there any accidents on site? Please explain:': 'Not at the tune-up site', None: None}
    
        
        self.assertEqual(outdata, ExpectedSelectAttribute)
if __name__ == "__main__":
    unittest.main()
    