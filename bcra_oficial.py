import requests

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

def main(): 
    response = requests.get('https://api.estadisticasbcra.com/usd_of', auth=BearerAuth('eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTQxMzY1NzksInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJndWVyZXRhLm1hcnRpbkBnbWFpbC5jb20ifQ.keGbR-ILI52s89UbdxIT3_7X866hzHjStjVJ1F1eti9u78WDSw9GwBLsRh5ooFYuQtSvHS2zl13XrVYa9lmd_w'))
    if response.status_code == 200:
        d = response.json() 
        print(d[0])
        print(type(d))
        for x in d: 
             print(f'''Fecha: {x['d']}, Cotización Oficial: {x['v']}''') 
    

if __name__ == '__main__':
    main()