# use sqlalchemy
import db.session as session
import db.models as models


def create_user(data):
  get_payload = data
  try:
    user = models.Users(**get_payload)
    session.add(user)
    session.commit()
  except Exception as e:
    return False, str(e)
  return True, None

def create_wallet(data):
  get_payload = data
  try:
    wallet = models.Wallets(**get_payload)
    session.add(wallet)
    session.commit()
  except Exception as e:
    return False, str(e)
  return True, None

def create_transactions(data):
  balance = session.query(models.Wallets).filterby(user_id=data['user_id'])
  if transaction_payload['transaction_type'] == 'kredit' and balance < (data['amount'] * len(data['recipients'])):
    return False, "balance is not enough"
  transaction_payload = {}
  transaction_payload['transaction_type'] = data['transaction_type']
  .
  .
  .
  try:
    transaction = models.Transactions(**transaction_payload)
    session.add(transaction)
    session.commit()
  except Exception as e:
    return False, str(e)
  if transaction_payload['transaction_type'] == 'kredit':
      add_recipients(data)
  return True, None

def add_recipients(data):
  recipients_payload = {}
  try:
    for recipient in data['recipients']:
      recipient = recipient_payload['recipient'] = data['recipient']
      .
      .
      models.Recipients(**recipient_payload)
      session.add(recipient)
    session.commit()
  except Exception as e:
    return False, str(e)
  return True, None
   

def balance_worker():
  data = session.query(models.Transactions).filterby(user_id=data['user_id']).filterby(transaction_id=transaction_id).filterby(status='success')
  for x in data:
    
  
  
  
