import requests
import json

def get_instance_public_ip():
    # כתובת ה-URL לקריאה ל-REST API של Jenkins
    url = 'http:/192.168.49.1:8080/job/terraform/lastSuccessfulBuild/api/json'

    # מבצעים בקשה GET ל-REST API
    response = requests.get(url)

    # בודקים אם הבקשה הצליחה
    if response.status_code == 200:
        # פענוח תוצאת הבקשה
        data = response.json()
        # מחזירים את כתובת ה-IP הציבורית של המכונה
        return data['actions'][0]['parameters'][0]['value']
    else:
        # אם הבקשה נכשלה, מדפיסים הודעת שגיאה
        print("Failed to retrieve instance public IP:", response.status_code)
        return None

# קריאה לפונקציה ושמירת התוצאה
instance_public_ip = get_instance_public_ip()

# מדפיסים את כתובת ה-IP הציבורית של המכונה
print("Instance public IP:", instance_public_ip)
