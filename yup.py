'''

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC90743e6f877af6ad8cfeb9e0507af200"
# Your Auth Token from twilio.com/console
auth_token  = "feb9e0d01ecf796d7f343fff6b629373"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to = "+12762027141",
    from_ = "+19719839257",
    body = "Hello from Python!  ")

print(message.sid)

'''

from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
# Your Account SID from twilio.com/console
account_sid = "AC90743e6f877af6ad8cfeb9e0507af200"
# Your Auth Token from twilio.com/console
auth_token  = "feb9e0d01ecf796d7f343fff6b629373"
client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Say>Ahoy, World!</Say></Response>',
                        to='+12762027141',
                        from_='+19719839257'
                    )

print(call.sid)

call = client.calls.get("CAf3e085a5192a15857f2956cca2424bb5")
print(call)
