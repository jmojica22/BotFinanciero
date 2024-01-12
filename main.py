import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate('Data/env.json')

    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://jmojica-yfqylr.firebaseio.com/'
    })

    ref = db.reference('server/saving-data/fireblog')
    users_ref = ref.child('users')
    users_ref.set({
        'alanisawesome': {
            'date_of_birth': 'June 23, 1912',
            'full_name': 'Alan Turing'
        },
        'gracehop': {
            'date_of_birth': 'December 9, 1906',
            'full_name': 'Grace Hopper'
        }
    })

