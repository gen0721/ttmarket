import httpx

class CryptoBot:
    def __init__(self, api_key: str, api_url: str):
        self.api_key = api_key
        self.api_url = api_url
        self.client = httpx.Client(headers={'Authorization': f'Bearer {self.api_key}'})

    def deposit(self, amount: float, currency: str):
        data = {'amount': amount, 'currency': currency}
        response = self.client.post(f'{self.api_url}/deposit', json=data)
        return response.json()

    def withdraw(self, amount: float, currency: str):
        data = {'amount': amount, 'currency': currency}
        response = self.client.post(f'{self.api_url}/withdraw', json=data)
        return response.json()