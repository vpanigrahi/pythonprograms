
# coding: utf-8

# In[266]:

#lists
python_versions = [1.0, 1.5, 1.6, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6]


# In[267]:

python_versions[-1] #The index -1 refers to the last element of the list, -2 to the second to last, and so on.


# In[268]:

my_list = ['a','b','c','d','e']


# In[269]:

my_list[4]


# In[270]:

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]


# In[271]:

days_in_month[8]


# In[272]:

def how_many_days(month_number):
    """Returns the number of days in a month.
    WARNING: This function doesn't account for leap years!
    """
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    return days_in_month[month_number+1]
 
print(how_many_days(8))


# In[273]:

#slicingLists
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


# In[274]:

q3 = months[6:9]


# In[275]:

print(q3)


# In[276]:

first_half = months[:6]
print(first_half)


# In[277]:

second_half = months[6:]
print(second_half)


# In[278]:

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']


# In[279]:

#doubt
print(len(eclipse_dates))
print(eclipse_dates[7:10])


# In[280]:

sample_string = "And Now For Something Completely Different"
sample_list = ['Graham', 'John', 'Terry', 'Eric', 'Terry', 'Michael']
sample_string[4]


# In[281]:

sample_list[5]


# In[282]:

sample_string[12:21]


# In[283]:

sample_list[2:4]


# In[284]:

len(sample_string)


# In[285]:

len(sample_list)


# In[286]:

'thing' in sample_string


# In[287]:

'Rowan' in sample_list


# In[288]:

#The obvious difference is that strings are sequences of letters, while list elements can be any type of object. 
#A more subtle difference is that lists can be modified, but strings can't be:


# In[289]:

sample_list[3] = 'Vasu'
print(sample_list)


# In[290]:

sample_string[8] = 'f'


# In[291]:

#The technical term for whether an object can be modified is mutability. Lists are mutable, while strings are immutable


# In[292]:

sentence1 = "I wish to register a complaint."
sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]


# In[293]:

sentence2[6]="!"
print sentence2


# In[294]:

sentence2[0]= "Our Majesty"
print sentence2


# In[295]:

sentence1[30]="!"


# In[296]:

sentence2[0:2] = ["We", "want"]
print sentence2


# In[297]:

#strings are immutable
name = "Old Woman"
person = name
name = "Dennis"
print(name)
print(person)


# In[298]:

batch_sizes = [15, 6, 89, 34, 65, 35]
max(batch_sizes)


# In[299]:

python_varieties = ['Burmese Python', 'African Rock Python', 'Ball Python', 'Reticulated Python', 'Angolan Python']
x=max(python_varieties)
x


# In[300]:

#doubt
max([42, 'African Swallow'])


# In[301]:

min(batch_sizes)


# In[302]:

sorted(batch_sizes)


# In[303]:

nautical_directions = "\n".join(["fore", "aft", "starboard", "port"])
print(nautical_directions)


# In[304]:

def top_three(input_list):
    input_list=sorted(input_list)
    x=input_list[-1]
    y=input_list[-2]
    z=input_list[-3]
    return x,y,z
    


# In[305]:

df=[2, 3, 5, 6, 8, 4, 2, 1]
top_three(df)


# In[306]:

def median(numbers):
    numbers.sort() 
    if len(numbers) % 2:
        middle_index = int(len(numbers)/2)
        return numbers[middle_index]
    else:
        right_of_middle = len(numbers)//2 
        left_of_middle = right_of_middle - 1
        return (numbers[right_of_middle] + numbers[left_of_middle])/2


# In[307]:

numbers=[2, 3, 5, 6, 8, 4, 1]
median(numbers)


# In[308]:

def list_sum(input_list):
    y = 0
    for i in input_list:
        y=i+y
    return y


# In[309]:

test1 = list_sum([1, 2, 3])
test1


# In[310]:

for i in range(len([1, 20, 3])):
    print i


# In[311]:

test2 = list_sum([-1, 0, 1])
test2


# In[312]:

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0
for token in tokens:
    if token[0] == '<':
        count += 1
print count


# In[313]:

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0
for i in tokens:
    if i[0] == '<':
        count += 1
        print i[0]
print count


# In[314]:

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0
for i in tokens:
    if i[count] == '<':
        count += 1
        print i[count]
print count


# In[315]:

hmp=[]
for i in tokens:
    hmp.append(i.title())
    print hmp


# In[316]:

hmp


# In[317]:

for number in range(4):
    print(number)


# In[318]:

def html_list(inputlist):
    print("<ul>")
    for i in inputlist:
        print "<li>"+i+"</li>" 
    print("</ul>")
    return
 


# In[319]:

inputlist = ['First element', 'Second element', 'Third element']
print("<ul>")
for i in inputlist:
    print "<li>"+i+"</li>"
print("</ul>")


# In[320]:

x=html_list(inputlist)


# In[321]:

y=0
while y*y<80:
    y+=1
if y*y==24:
    pass
else:
    y=y-1
    


# In[322]:

y


# In[323]:

y="vasundhara"
len(y)


# In[324]:

headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]
news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break
print news_ticker


# In[325]:

#wrong method
dedupe_list=["India","India","Delhi","Bhopal","Bhopal"]
y=0
i=0
if dedupe_list[y]==dedupe_list[i+1]:
    del dedupe_list[y]
    for i in range(len(dedupe_list)):
        i=i+1
        print i
    print dedupe_list
    if y < range(len(dedupe_list)):
        y=y+1
        print y
elif dedupe_list[y]!=dedupe_list[i+1]:
    for i in range(len(dedupe_list)):
        i=i+1
        print i
   


# In[326]:

def remove_duplicates(source):
    target = []

    for element in source:
        if element not in target:
            target.append(element)

    return target


# In[327]:

x=remove_duplicates(dedupe_list)
print x


# In[328]:

x


# In[329]:

#wrong method
dedupe_list=["India","India","Delhi","Bhopal","Bhopal"]
y=0
i=1

for y in range(len(dedupe_list)):
    for i in range(len(dedupe_list)):
        if dedupe_list[y]==dedupe_list[i]:
            del dedupe_list[i]
            i=i+1
        else:
            i=i+1
    y=y+1
    


# In[330]:

for y in range(len(dedupe_list)):
    print y


# In[331]:

x=set(dedupe_list)


# In[332]:

x


# In[333]:

nearest_square=set()
y=0
while y*y<2000:
    nearest_square.add(y*y)
    y+=1

    


# In[334]:

nearest_square


# In[335]:

population={'Shanghai':17.8,'Istanbul':13.3,'Karachi':13.0,'Mumbai':12.5}
population.get('kyx')


# In[336]:

population['contain']


# In[337]:

population.get('Shanghai')


# In[338]:

country_list=['Malta',
 'Sudan',
 'Oman',
 'Jamaica',
 'Pakistan',
 'Netherlands',
 'Venezuela',
 'Tuvalu',
 'Kazakhstan',
 'Namibia',
 'Congo {Democratic Rep}',
 'Qatar',
 'El Salvador',
 'Macedonia',
 'Morocco',
 'Albania',
 'Netherlands',
 'Namibia',
 'Moldova',
 'Djibouti',
 'Malaysia',
 'Belarus',
 'Niger',
 'Thailand',
 'Burkina',
 'Panama',
 'Libya',
 'Kuwait',
 'Dominican Republic',
 'Andorra',
 'Nauru',
 'Guyana',
 'Austria',
 'Germany',
 'Morocco',
 'Sudan',
 'Lebanon',
 'Bahamas',
 'Austria',
 'Chad',
 'Canada',
 'Ivory Coast',
 'Papua New Guinea',
 'Mali',
 'Marshall Islands',
 'Morocco',
 'Angola',
 'New Zealand',
 'Mali',
 'Moldova',
 'Libya',
 'Bulgaria',
 'Honduras',
 'Comoros',
 'Tunisia',
 'Peru',
 'Greece',
 'Montenegro',
 'Austria',
 'Cambodia',
 'St Lucia',
 'Ecuador',
 'Taiwan',
 'Colombia',
 'Liechtenstein',
 'Monaco',
 'Iraq',
 'Zambia',
 'Sri Lanka',
 'Poland',
 'Vanuatu',
 'Barbados',
 'Mauritius',
 'Turkmenistan',
 'Taiwan',
 'Israel',
 'Mali',
 'United Arab Emirates',
 'Zimbabwe',
 'Sao Tome & Principe',
 'Kuwait',
 'Canada',
 'Vietnam',
 'Zambia',
 'Rwanda',
 'Kosovo',
 'Nepal',
 'Indonesia',
 'Suriname',
 'Mali',
 'Chile',
 'Luxembourg',
 'Papua New Guinea',
 'Norway',
 'Brunei',
 'Ecuador',
 'Turkey',
 'Pakistan',
 'Mozambique',
 'Senegal',
 'Algeria',
 'Laos',
 'Vietnam',
 'Kosovo',
 'Belize',
 'Bhutan',
 'Andorra',
 'Russian Federation',
 'Cambodia',
 'Madagascar',
 'Slovenia',
 'Malaysia',
 'Belgium',
 'Sweden',
 'Nepal',
 'Germany',
 'Fiji',
 'Australia',
 'Kenya',
 'Sudan',
 'Nepal',
 'Niger',
 'Palau',
 'Serbia',
 'Chad',
 'Bhutan',
 'Poland',
 'Nicaragua',
 'Barbados',
 'Hungary',
 'Algeria',
 'Ukraine',
 'China',
 'Latvia',
 'Panama',
 'Papua New Guinea',
 'Sweden',
 'Zimbabwe',
 'Jordan',
 'Sao Tome & Principe',
 'Mexico',
 'Sudan',
 'Czech Republic',
 'New Zealand',
 'Uruguay',
 'Kuwait',
 'Liberia',
 'Canada',
 'Seychelles',
 'Liberia',
 'Saudi Arabia',
 'Sierra Leone',
 'South Sudan',
 'Bolivia',
 'Philippines',
 'Mauritania',
 'United States',
 'Hungary',
 'Bhutan',
 'Netherlands',
 'Burkina',
 'Congo {Democratic Rep}',
 'Central African Rep',
 'Burkina',
 'Poland',
 'Guinea',
 'United States',
 'Luxembourg',
 'Chile',
 'Kuwait',
 'Vatican City',
 'Maldives',
 'Ethiopia',
 'France',
 'Mozambique',
 'Nicaragua',
 'Portugal',
 'United States',
 'South Sudan',
 'Bangladesh',
 'Belize',
 'Mozambique',
 'Pakistan',
 'Sao Tome & Principe',
 'Israel',
 'Antigua & Deps',
 'Equatorial Guinea',
 'Grenada',
 'Liberia',
 'Nauru',
 'St Kitts & Nevis',
 'Armenia',
 'Italy',
 'San Marino',
 'Congo {Democratic Rep}',
 'Suriname',
 'Mauritius',
 'Albania',
 'Samoa',
 'Bosnia Herzegovina',
 'South Sudan',
 'Trinidad & Tobago',
 'Nigeria',
 'Bolivia',
 'South Africa',
 'Qatar',
 'South Sudan',
 'Morocco',
 'Benin',
 'Kuwait',
 'Tajikistan',
 'Guyana',
 'Indonesia',
 'Turkmenistan',
 'Sierra Leone',
 'Mali',
 'Antigua & Deps',
 'Turkmenistan',
 'Seychelles',
 'Bulgaria',
 'Rwanda',
 'Czech Republic',
 'Philippines',
 'Norway',
 'Germany',
 'Tonga',
 'United Arab Emirates',
 'Syria',
 'Bahamas',
 'Armenia',
 'Paraguay',
 'Zambia',
 'Samoa',
 'Senegal',
 'Kiribati',
 'Taiwan',
 'Gabon',
 'Cuba',
 'Comoros',
 'Bhutan',
 'Seychelles',
 'Mexico',
 'Bhutan',
 'El Salvador',
 'Tunisia',
 'Liechtenstein',
 'Czech Republic',
 'Congo',
 'Jordan',
 'Djibouti',
 'Macedonia',
 'Finland',
 'Denmark',
 'San Marino',
 'Cuba',
 'Botswana',
 'Equatorial Guinea',
 'United Kingdom',
 'Tanzania',
 'Bosnia Herzegovina',
 'Algeria',
 'El Salvador',
 'Senegal',
 'Myanmar, {Burma}',
 'Pakistan',
 'Malaysia',
 'Oman',
 'Tanzania',
 'Gabon',
 'Tonga',
 'Vietnam',
 'Sudan',
 'Slovakia',
 'Tajikistan',
 'Kyrgyzstan',
 'Kiribati',
 'Zambia',
 'San Marino',
 'Saudi Arabia',
 'South Sudan',
 'Mexico',
 'Uruguay',
 'Cyprus',
 'Syria',
 'Panama',
 'Sierra Leone',
 'Finland',
 'Iraq',
 'United States',
 'Dominican Republic',
 'Czech Republic',
 'Latvia',
 'Bolivia',
 'Korea North',
 'Angola',
 'Germany',
 'Malawi',
 'Guinea-Bissau',
 'Ghana',
 'Lithuania',
 'East Timor',
 'Honduras',
 'Bahamas',
 'Algeria',
 'Luxembourg',
 'Eritrea',
 'Gabon',
 'Mauritania',
 'Cambodia',
 'Solomon Islands',
 'Haiti',
 'Jamaica',
 'Kyrgyzstan',
 'Tanzania',
 'Marshall Islands',
 'Lithuania',
 'Bahrain',
 'East Timor',
 'Botswana',
 'Marshall Islands',
 'Grenada',
 'France',
 'St Lucia',
 'Eritrea',
 'Azerbaijan',
 'Ghana',
 'New Zealand',
 'El Salvador',
 'Cape Verde',
 'Hungary',
 'Botswana',
 'Bosnia Herzegovina',
 'Kuwait',
 'Saudi Arabia',
 'Indonesia',
 'Qatar',
 'Germany',
 'Argentina',
 'Georgia',
 'Fiji',
 'Tajikistan',
 'Vanuatu',
 'Samoa',
 'Togo',
 'Gambia',
 'Sudan',
 'Cambodia',
 'Argentina',
 'Canada',
 'Nepal',
 'Grenada',
 'Vietnam',
 'Cameroon',
 'Cameroon',
 'Lebanon',
 'Rwanda',
 'United Kingdom',
 'Cambodia',
 'Paraguay',
 'Guinea',
 'Kosovo',
 'Switzerland',
 'Mauritius',
 'Fiji',
 'Paraguay',
 'Thailand',
 'Eritrea',
 'Guatemala',
 'Suriname',
 'Palau',
 'Mozambique',
 'Bangladesh',
 'Australia',
 'South Africa',
 'Yemen',
 'India',
 'Peru',
 'Korea North',
 'Oman',
 'Moldova',
 'St Kitts & Nevis',
 'Benin',
 'India',
 'Grenada',
 'Taiwan',
 'Madagascar',
 'Paraguay',
 'Angola',
 'Saudi Arabia',
 'Antigua & Deps',
 'Marshall Islands',
 'Micronesia',
 'Benin',
 'Monaco',
 'Cuba',
 'Kuwait',
 'Serbia',
 'Oman',
 'Bahamas',
 'Norway',
 'Thailand',
 'Malawi',
 'Guyana',
 'Denmark',
 'South Africa',
 'China',
 'Oman',
 'New Zealand',
 'Austria',
 'Venezuela',
 'Syria',
 'Rwanda',
 'Dominican Republic',
 'Algeria',
 'Honduras',
 'Solomon Islands',
 'Palau',
 'Cape Verde',
 'Ghana',
 'Algeria',
 'Pakistan',
 'Morocco',
 'Kenya',
 'Switzerland',
 'Malta',
 'China',
 'South Sudan',
 'Jamaica',
 'East Timor',
 'Malta',
 'Benin',
 'China',
 'Algeria',
 'United Kingdom',
 'Palau',
 'Ireland {Republic}',
 'Maldives',
 'Swaziland',
 'Guinea',
 'Haiti',
 'Lesotho',
 'Korea South',
 'Italy',
 'Nigeria',
 'Kiribati',
 'Kyrgyzstan',
 'Antigua & Deps',
 'Saint Vincent & the Grenadines',
 'United States',
 'Mongolia',
 'Saudi Arabia',
 'Haiti',
 'Czech Republic',
 'Portugal',
 'Mauritius',
 'Samoa',
 'Honduras',
 'Vietnam',
 'Algeria',
 'Marshall Islands',
 'Kiribati',
 'Fiji',
 'Ivory Coast',
 'Tajikistan',
 'Nicaragua',
 'Portugal',
 'Equatorial Guinea',
 'Ivory Coast',
 'Zambia',
 'New Zealand',
 'Somalia',
 'Senegal',
 'Mongolia',
 'Montenegro',
 'Ghana',
 'Bahrain',
 'Laos',
 'Paraguay',
 'Guinea-Bissau',
 'Bosnia Herzegovina',
 'Tanzania',
 'Gambia',
 'Sierra Leone',
 'Canada',
 'Bolivia',
 'Iraq',
 'Ivory Coast',
 'Zimbabwe',
 'Turkmenistan',
 'Bhutan',
 'Venezuela',
 'Ghana',
 'Panama',
 'Philippines',
 'Kenya',
 'Mali',
 'Tunisia',
 'Turkmenistan',
 'Ukraine',
 'Egypt',
 'Burundi',
 'Qatar',
 'Latvia',
 'Slovenia',
 'Gambia',
 'Algeria',
 'Poland',
 'Myanmar, {Burma}',
 'Panama',
 'Myanmar, {Burma}',
 'Central African Rep',
 'United Kingdom',
 'Comoros',
 'Yemen',
 'Liechtenstein',
 'Gambia',
 'Ethiopia',
 'Malaysia',
 'Italy',
 'Brazil',
 'Brazil',
 'Russian Federation',
 'Nicaragua',
 'Switzerland',
 'Georgia',
 'Georgia',
 'Dominica',
 'Liberia',
 'Tonga',
 'St Kitts & Nevis',
 'Vatican City',
 'Luxembourg',
 'Barbados',
 'Croatia',
 'Samoa',
 'St Lucia',
 'Comoros',
 'Burundi',
 'Philippines',
 'Mali',
 'Yemen',
 'Singapore',
 'Brazil',
 'Benin',
 'Slovenia',
 'Qatar',
 'Tajikistan',
 'Qatar',
 'Seychelles',
 'Somalia',
 'Zimbabwe',
 'Marshall Islands',
 'Ukraine',
 'Japan',
 'Sudan',
 'St Kitts & Nevis',
 'Botswana',
 'Slovakia',
 'Azerbaijan',
 'Philippines',
 'United States',
 'Nauru',
 'Albania',
 'Burundi',
 'Dominican Republic',
 'Bolivia',
 'France',
 'Antigua & Deps',
 'Georgia',
 'Finland',
 'Benin',
 'Oman',
 'Dominica',
 'Belize',
 'South Africa',
 'Libya',
 'Cyprus',
 'Ecuador',
 'France',
 'Namibia',
 'Zimbabwe',
 'Dominica',
 'Belgium',
 'United Arab Emirates',
 'Pakistan',
 'Colombia',
 'Vatican City',
 'Chad',
 'Algeria',
 'Malaysia',
 'Cambodia',
 'Equatorial Guinea',
 'Slovenia',
 'Bolivia',
 'Kazakhstan',
 'Japan',
 'New Zealand',
 'Morocco',
 'Romania',
 'Mexico',
 'Tonga',
 'Eritrea',
 'Senegal',
 'Belize',
 'Kosovo',
 'Benin',
 'Eritrea',
 'Egypt',
 'Korea North',
 'Taiwan',
 'Taiwan',
 'Guatemala',
 'Slovenia',
 'Somalia',
 'Spain',
 'Libya',
 'Dominica',
 'Togo',
 'Taiwan',
 'Morocco',
 'Finland',
 'Iraq',
 'Albania',
 'Hungary',
 'Angola',
 'St Lucia',
 'Seychelles',
 'Seychelles',
 'Andorra',
 'Serbia',
 'Mauritius',
 'Jamaica',
 'Ivory Coast',
 'Sudan',
 'Bahrain',
 'Australia',
 'France',
 'China',
 'United Kingdom',
 'Marshall Islands',
 'Guinea',
 'Japan',
 'Cuba',
 'Sierra Leone',
 'Sri Lanka',
 'Antigua & Deps',
 'Georgia',
 'India',
 'Germany',
 'Congo',
 'Cameroon',
 'Brunei',
 'Uganda',
 'South Africa',
 'Ecuador',
 'St Lucia',
 'Congo {Democratic Rep}',
 'Bahamas',
 'Syria',
 'Czech Republic',
 'Pakistan',
 'Tanzania',
 'Sao Tome & Principe',
 'Burkina',
 'Nigeria',
 'Mali',
 'Greece',
 'Vatican City',
 'South Sudan',
 'Morocco',
 'Burkina',
 'Switzerland',
 'Kosovo',
 'Gabon',
 'Paraguay',
 'Romania',
 'Mongolia',
 'Zambia',
 'Syria',
 'Netherlands',
 'Zambia',
 'Dominican Republic',
 'Iceland',
 'Libya',
 'Lebanon',
 'Antigua & Deps',
 'Albania',
 'Turkey',
 'New Zealand',
 'Somalia',
 'Guinea-Bissau',
 'El Salvador',
 'Israel',
 'Central African Rep',
 'Korea North',
 'Zambia',
 'Switzerland',
 'Taiwan',
 'Namibia',
 'Mauritania',
 'Sudan',
 'Ghana',
 'Moldova',
 'East Timor',
 'Brunei',
 'Swaziland',
 'Cambodia',
 'Saint Vincent & the Grenadines',
 'Netherlands',
 'Papua New Guinea',
 'Georgia',
 'Tonga',
 'Mauritius',
 'Canada',
 'Guinea-Bissau',
 'Norway',
 'Singapore',
 'Morocco',
 'Cape Verde',
 'Pakistan',
 'Central African Rep',
 'Myanmar, {Burma}',
 'United Arab Emirates',
 'Maldives',
 'Ghana',
 'Saudi Arabia',
 'Netherlands',
 'Albania',
 'Bahamas',
 'Papua New Guinea',
 'Kosovo',
 'Lesotho',
 'Panama',
 'Argentina',
 'India',
 'Kazakhstan',
 'Angola',
 'Guinea',
 'Ukraine',
 'Congo',
 'Bahrain',
 'Israel',
 'Sudan',
 'Qatar',
 'Belarus',
 'Ghana',
 'Algeria',
 'Macedonia',
 'Grenada',
 'Spain',
 'Antigua & Deps',
 'Comoros',
 'Egypt',
 'Belize',
 'Haiti',
 'Eritrea',
 'Poland',
 'Bhutan',
 'Cape Verde',
 'Uganda',
 'Syria',
 'Libya',
 'Thailand',
 'Bahrain',
 'Slovenia',
 'Luxembourg',
 'Tunisia',
 'Guinea-Bissau',
 'Bhutan',
 'Uzbekistan',
 'Togo',
 'Madagascar',
 'Greece',
 'Guinea-Bissau',
 'Afghanistan',
 'Zambia',
 'Hungary',
 'Albania',
 'India',
 'Sao Tome & Principe',
 'Honduras',
 'Albania',
 'Cape Verde',
 'Turkmenistan',
 'Antigua & Deps']


# In[339]:

country_counts={}
for country in country_list:
    if country in country_counts:
        country_counts[country] += 1
    else:
        country_counts[country] = 1


# In[340]:

country_counts


# In[341]:

list=['j','j','k','l','l','w','q']
l_counts={}
for element in list:
    if element in l_counts:
        l_counts[element] += 1
        print l_counts
    else:
        l_counts[element] = 1
        print l_counts
l_counts


# In[342]:

Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963, 
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}
b_count={}
for element in Beatles_Discography:
    if element in b_count:
        b_count[element]+=1
    else:
        b_count[element]=1


# In[343]:

import numpy as np
c_count={}
ma=0
for element in Beatles_Discography.values():
    if element in c_count:
        c_count[element]+=1
        if c_count[element]>ma:
            ma=c_count[element]
            choice=element
    else:
        c_count[element]=1
print c_count
np.max(c_count.values())
choice


# In[344]:

choice


# In[345]:

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}
elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True


# In[346]:

elements


# In[365]:

monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}


# In[366]:

total=0
for month in monthly_takings.keys():
    total = total + sum(monthly_takings[month])
    print total


# In[367]:

total


# In[ ]:



