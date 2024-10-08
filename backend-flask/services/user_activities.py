from datetime import datetime, timedelta, timezone
class UserActivities:
  def run(user_handle):
    try :
      # xray
      segment = xray_recorder.begin_segment('user_activities')
      model = {
        'errors': None,
        'data': None
      }

      now = datetime.now(timezone.utc).astimezone()

      if user_handle == None or len(user_handle) < 1:
        model['errors'] = ['blank_user_handle']
      else:
        now = datetime.now()
        results = [{
          'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
          'handle':  'Insha',
          'message': 'Just live',
          'created_at': (now - timedelta(days=1)).isoformat(),
          'expires_at': (now + timedelta(days=31)).isoformat()
        }]
        model['data'] = results
        # xray
      subsegment = xray_recorder.begin_subsegment('mock-data')
      dict = {
        "now": now.isoformat(),
        "results-size" : len(model['data']) 
      }
      subsegment.put_metadata('key',dict,'namespace')
      xray_recorder.end_subsegment()
    finally :
      xray_recorder.end_subsegment()

    return model