
from pyzillow import pyzillow
def main():
    with open("Key.text", 'r') as f:
        key = f.readline()
        #print(key)
        zillow_data = pyzillow.ZillowWrapper(key)
        result = zillow_data.get_deep_search_results('200 S California Avenue, CA', '94306')
        data = pyzillow.GetDeepSearchResults(result)
        print(data.zillow_id)
main()      
