
# In[1]:
#print statement
print(3+1)


# In[2]:
#additionoperation
3+1

# In[3]:
#mod-reminder
float(30%4)


# In[4]:
#result will be an interger
30//4


# In[27]:
#division-doubt
float(17/4)


# In[32]:
#use of hash


# In[6]:

#arithematic operation within print
print((23+32+64)/3)


# In[7]:
#bracket function
(9*7)+(5*7)


# In[8]:
#bracket function
(17*6)-((9*7)+(5*7))


# In[36]:
#Substraction
102-98


# In[35]:
3+2.5
print(type(3+2.5))


# In[9]:
0.1+0.1+0.1


# In[10]:
5/0


# In[11]:
#introduction to variables

# In[12]:
manila_pop = 20000

# In[42]:
manila_pop

# In[13]:
print(manila_pop)


# In[14]:
float(3)

# In[15]:
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6
# decrease the rainfall variable by 10% to account for runoff
rainfall *= 0.9
print(rainfall)
# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall
print(reservoir_volume)
# increase reservoir_volume by 5% to account for stormwater that flows
reservoir_volume *= 1.05
print(reservoir_volume)
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95
print(reservoir_volume)
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
reservoir_volume -= 2.5*100000
# print the new value of the reservoir_volume variable
print(reservoir_volume)


# In[16]:
manila_pop = 1780148
manila_area = 16.56
manila_pop_density = manila_pop/manila_area
print(int(manila_pop_density))


# In[17]:
manila_pop = 1781573
print(int(manila_pop_density))
#Python actually did the calculation to evaluate the expression on the right-hand-side, 
#manila_pop/manila_area and then assigned the variable manila_pop_density to be the value of that expression. 
#It promptly forgot the formula, only saving the result in the variable. 
#In order to update the value of manila_pop_density to take into account the change in manila_pop, 
#we need to run this line again:


# In[18]:
#boolean operators
42>43


# In[19]:
sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5
san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area
san_francisco_pop_density>rio_de_janeiro_pop_density


# In[20]:
print(san_francisco_pop_density > rio_de_janeiro_pop_density)


# In[1]:
print('vasundhara')


# In[7]:
x = 'vasundhara'
print x


# In[10]:
#concatenate strings
x = 'vasundhara'
y = 'panigrahi'
print (x+' '+y)


# In[11]:
pet_halibut = 'Why should I be tarred with the epithet "loony" merely because I have a pet halibut?'
print pet_halibut


# In[12]:
#use a backslash, \, to escape quotes
salesman = '"I think you\'re an encyclopaedia salesman"'
print salesman


# In[13]:
coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)


# In[15]:
length = len('vasundharapanigrahi')
length


# In[16]:
len(835)


# In[17]:
print(type(length))


# In[18]:
print(type("12"))


# In[19]:
print(type("hippo" *12))


# In[20]:
"hippo" *12


# In[21]:
count = int(4.0)
print(count)


# In[22]:
print(type(count))


# In[29]:
mon_sales = "121"
mon_sales = int(mon_sales)
print(type(mon_sales))


# In[34]:
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"
mon_sales = int(mon_sales)
tues_sales = int(tues_sales)
wed_sales = int(wed_sales)
thurs_sales = int(thurs_sales)
fri_sales = int(fri_sales)
totalSales = mon_sales+tues_sales+wed_sales+thurs_sales+fri_sales
print('This week\'s total sales: '+str(totalSales))


# In[36]:
#title method will return the string with capital first letter
print("charlotte hippopotamus turner".title())


# In[37]:
#the islower method inspects the string object it has been called with. 
#In this case the string object is "charlotte hippopotamus turner". islower then returns a bool 
#that indicates whether the string object consists of lowercase letters.

full_name = "charlotte hippopotamus turner"
print(full_name.islower())


# In[38]:
13.37.islower


# In[39]:
#important documentation https://docs.python.org/3/library/stdtypes.html#string-methods
x = "One fish, two fish, red fish, blue fish.".count('fish')
print(x)
# In[41]:
prophecy = "And there shall in that time be rumours of things going astray, and there will be a great confusion as to where things really are, and nobody will really know where lieth those little things with the sort of raffia work base, that has an attachment…at this time, a friend shall lose his friends’s hammer and the young shall not know where lieth the things possessed by their fathers that their fathers put there only just the night before around eight o’clock…"
vowel_count = 0
vowel_count +=prophecy.count('a')
vowel_count +=prophecy.count('A')
vowel_count +=prophecy.count('e')
vowel_count +=prophecy.count('E')
vowel_count +=prophecy.count('i')
vowel_count +=prophecy.count('I')
vowel_count +=prophecy.count('o')
vowel_count +=prophecy.count('O')
vowel_count +=prophecy.count('u')
vowel_count +=prophecy.count('U')
print(vowel_count)


# In[43]:
prophecy=prophecy.upper()
print(prophecy)


# In[44]:
city = "Seoul"
high_temperature = 18
low_temperature = 9
temperature_unit = "degrees Celsius"
weather_conditions = "light rain"
alert = "Today's forecast for " + city + ": The temperature will range from " + str(low_temperature) + " to " + str(high_temperature) + " " + temperature_unit + ". Conditions will be " + weather_conditions + "."


# In[ ]:



