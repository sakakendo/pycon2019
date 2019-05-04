from twilio.rest import Client

client = Client(
        'AC095f902bb60c7b8030b9fbafb627a454',
        'ae0d5c2d2e2821611ebf794047699d1f'
        )

call=client.calls.create(
        to='4704554424',
        from_='+12109780641',
        url ='http://demo.twilio.com/docs/voice.xml')

print(call)
print(call.sid)

