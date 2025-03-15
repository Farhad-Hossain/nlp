from driver import Crowler
from selenium.webdriver.common.by import By
import time

source = 'https://guardianlife.com.bd/staff-list/'
cr = Crowler(source, 'firefox')

staffs = cr.data.find_element(
    by=By.ID,
    value='root'
)

staffs = staffs.find_elements(by=By.TAG_NAME, value='tr')

staff_list = []

for staff in staffs:
    single_staff = {}
    staff_infos = staff.find_elements(by=By.TAG_NAME, value='td')
    
    if len(staff_infos) > 5:
        single_staff['name'] = staff_infos[1].text
        single_staff['designation'] = staff_infos[2].text
        single_staff['department'] = staff_infos[3].text
        single_staff['contact'] = staff_infos[4].text
        single_staff['email'] = staff_infos[5].text

    staff_list.append(single_staff)
    
print(staff_list)

# staff_list = []

# for staff in staffs.find_elements(by=By.TAG_NAME, value='tr'):
#     staff_infos = staff.find_elements(by=By.TAG_NAME, value='td')
#     single_staff = {}
#     if len(staff_infos) > 5:
#         # single_staff['name'] = staff_infos[1].text
#         single_staff['designation'] = staff_infos[2].text
#         single_staff['department'] = staff_infos[3].text
#         single_staff['contact'] = staff_infos[4].text
#         single_staff['email'] = staff_infos[5].text

#     staff_list.append(single_staff)

# print(staff_list)

cr.teardown()


