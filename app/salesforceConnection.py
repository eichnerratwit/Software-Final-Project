import requests

# Endpoint and authorization details for Salesforce API
_endpoint = 'https://curious-badger-kyez48-dev-ed.my.salesforce.com'
version = '60.0'
access_token = '00Daj000003SPmz!AQEAQKFgoI0Tx4WbRNLuyoo3D_Ddf.2UyKjeIzZTpAnImNXJAmB8b4_3blkjSQJJu2alvlxW0.d1NFSzp0dh5n1rqVHuLh50'

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
}


def addResume(resume_text, cover_text, app_status):
    """Adds an applicant's resume and cover letter to Salesforce"""
    URL = f'{_endpoint}/services/data/v{version}/sobjects/Applicant__c/'
    data = {
        'Cover_Letter__c': resume_text,
        'Resume__c': cover_text,
        'Status__c': app_status
    }
    requests.post(URL, headers=headers, json=data)


def makeNewUser(first_name, last_name, username, email, password, user_type):
    """Takes a new users information and creates a record of that information in salesforce."""
    URL = f'{_endpoint}/services/data/v{version}/sobjects/User__c/'
    data = {
        'firstName__c': first_name,
        'lastName__c': last_name,
        'Name': username,
        'email__c': email,
        'password__c': password,
        'type__c': user_type
    }
    requests.post(URL, headers=headers, json=data)


def validateUser(email, password):
    """Checks to see if entered user information is valid or not and returns either true or false"""
    query = f"SELECT Id, Name FROM User__c WHERE email__c = '{email}' AND password__c = '{password}' LIMIT 1"
    URL = f"{_endpoint}/services/data/v{version}/query/"
    params = {'q': query}

    response = requests.get(URL, headers=headers, params=params)

    if response.status_code == 200:
        results = response.json()
        if results['totalSize'] > 0:
            return True
    return False
