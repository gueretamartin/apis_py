import requests

def main():
    url = 'http://api.open-notify.org/astros.json'
    response = requests.get(url)    
    
    if response.status_code == 200:
        d = response.json() 
        people = d['people'] 
        print(f'People in Space: ({len(people)})')
        for x in people:
            print(x['name'])

if __name__ == '__main__':
    main()